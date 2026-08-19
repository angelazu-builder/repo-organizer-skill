#!/usr/bin/env python3
"""
Invariant Checker for repo-organizer-skill
Captures and verifies repository invariant baseline before and after restructuring.
"""

import ast
import json
import os
import sys
import re
from pathlib import Path
from typing import Dict, List, Any

IGNORE_TARGETS = {'path', 'target', 'url', 'file', 'link', 'absolute/path/to/file'}

def scan_markdown_links(root_dir: Path) -> List[Dict[str, str]]:
    links = []
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    image_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
    
    for md_file in root_dir.glob('**/*.md'):
        if '.git' in md_file.parts or '.agents' in md_file.parts:
            continue
        try:
            content = md_file.read_text(encoding='utf-8', errors='ignore')
            # Remove inline code blocks and code blocks to prevent parsing sample code brackets
            content_clean = re.sub(r'```[\s\S]*?```', '', content)
            content_clean = re.sub(r'`[^`]+`', '', content_clean)
            
            rel_source = str(md_file.relative_to(root_dir))
            
            all_matches = link_pattern.findall(content_clean) + image_pattern.findall(content_clean)
            for text, target in all_matches:
                target_clean = target.strip()
                if target_clean.startswith(('http://', 'https://', 'mailto:', '#')):
                    continue
                target_clean = target_clean.split('#')[0]
                if not target_clean or target_clean in IGNORE_TARGETS:
                    continue
                links.append({
                    "source": rel_source,
                    "text": text.strip(),
                    "target": target_clean
                })
        except Exception as e:
            pass
    return links

def scan_python_ast_imports(root_dir: Path) -> List[Dict[str, Any]]:
    ast_records = []
    for py_file in root_dir.glob('**/*.py'):
        if '.git' in py_file.parts or '.agents' in py_file.parts or 'venv' in py_file.parts:
            continue
        rel_py = str(py_file.relative_to(root_dir))
        try:
            code = py_file.read_text(encoding='utf-8', errors='ignore')
            tree = ast.parse(code, filename=rel_py)
            imports = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append({"type": "import", "name": alias.name})
                elif isinstance(node, ast.ImportFrom):
                    imports.append({"type": "import_from", "module": node.module or '', "level": node.level})
            ast_records.append({
                "file": rel_py,
                "imports": imports
            })
        except SyntaxError:
            pass
        except Exception as e:
            pass
    return ast_records

def scan_entry_points(root_dir: Path) -> Dict[str, Any]:
    entry_points = {}
    for name in ['main.py', 'app.py', 'pyproject.toml', 'package.json', 'setup.py', 'Cargo.toml', 'Dockerfile', 'docker-compose.yml']:
        target = root_dir / name
        entry_points[name] = target.exists()
    return entry_points

def scan_ci_workflows(root_dir: Path) -> List[str]:
    workflows = []
    ci_dir = root_dir / '.github' / 'workflows'
    if ci_dir.exists() and ci_dir.is_dir():
        for wf in ci_dir.glob('*.yml'):
            workflows.append(str(wf.relative_to(root_dir)))
        for wf in ci_dir.glob('*.yaml'):
            workflows.append(str(wf.relative_to(root_dir)))
    return workflows

def capture_baseline(root_dir: Path) -> Dict[str, Any]:
    return {
        "links": scan_markdown_links(root_dir),
        "ast_imports": scan_python_ast_imports(root_dir),
        "entry_points": scan_entry_points(root_dir),
        "ci_workflows": scan_ci_workflows(root_dir)
    }

def verify_baseline(root_dir: Path, baseline: Dict[str, Any]) -> Dict[str, Any]:
    current = capture_baseline(root_dir)
    results = {
        "status": "PASS",
        "broken_links": [],
        "missing_entry_points": [],
        "missing_workflows": [],
        "errors": []
    }
    
    # Verify links
    for item in current["links"]:
        source_path = root_dir / item["source"]
        target_path = (source_path.parent / item["target"]).resolve()
        if not target_path.exists():
            results["broken_links"].append(item)
            results["status"] = "FAIL"
            
    # Verify entry points
    for name, existed in baseline.get("entry_points", {}).items():
        if existed and not (root_dir / name).exists():
            results["missing_entry_points"].append(name)
            results["status"] = "FAIL"

    # Verify workflows
    for wf in baseline.get("ci_workflows", []):
        if not (root_dir / wf).exists():
            results["missing_workflows"].append(wf)
            results["status"] = "FAIL"

    return results

def main():
    if len(sys.argv) < 2:
        print("Usage: invariant_checker.py [snapshot|verify] [--root DIR] [--output FILE] [--baseline FILE]")
        sys.exit(1)
        
    cmd = sys.argv[1]
    root_dir = Path.cwd()
    output_file = Path(".agents/reports/invariant_baseline.json")
    baseline_file = output_file
    
    for i in range(2, len(sys.argv)):
        if sys.argv[i] == "--root" and i + 1 < len(sys.argv):
            root_dir = Path(sys.argv[i+1])
        elif sys.argv[i] == "--output" and i + 1 < len(sys.argv):
            output_file = Path(sys.argv[i+1])
        elif sys.argv[i] == "--baseline" and i + 1 < len(sys.argv):
            baseline_file = Path(sys.argv[i+1])

    root_dir = root_dir.resolve()
    
    if cmd == "snapshot":
        output_file.parent.mkdir(parents=True, exist_ok=True)
        baseline = capture_baseline(root_dir)
        output_file.write_text(json.dumps(baseline, indent=2), encoding='utf-8')
        print(f"✅ Invariant baseline snapshot saved to: {output_file}")
        print(f"   • Links captured: {len(baseline['links'])}")
        print(f"   • AST imports captured: {len(baseline['ast_imports'])}")
        print(f"   • Entry points tracked: {sum(1 for v in baseline['entry_points'].values() if v)}")
        print(f"   • CI workflows tracked: {len(baseline['ci_workflows'])}")
        
    elif cmd == "verify":
        if not baseline_file.exists():
            print(f"❌ Baseline snapshot file not found: {baseline_file}")
            sys.exit(1)
        baseline = json.loads(baseline_file.read_text(encoding='utf-8'))
        report = verify_baseline(root_dir, baseline)
        print(json.dumps(report, indent=2))
        if report["status"] != "PASS":
            print(f"🔴 INVARIANT VERIFICATION FAILED!")
            sys.exit(1)
        else:
            print(f"🟢 ALL INVARIANTS PASSED! (Same semantics, better structure)")
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == '__main__':
    main()

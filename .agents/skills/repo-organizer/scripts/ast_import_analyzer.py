#!/usr/bin/env python3
"""
AST Import Analyzer for repo-organizer-skill
Parses Python AST across the target repository to construct dependency graph and check import integrity.
"""

import ast
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any

def analyze_ast(root_dir: Path) -> Dict[str, Any]:
    file_reports = []
    total_imports = 0
    broken_imports = []
    
    for py_file in root_dir.glob('**/*.py'):
        if '.git' in py_file.parts or '.agents' in py_file.parts or 'venv' in py_file.parts:
            continue
            
        rel_path = str(py_file.relative_to(root_dir))
        try:
            content = py_file.read_text(encoding='utf-8', errors='ignore')
            tree = ast.parse(content, filename=rel_path)
            
            imports = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append({"type": "import", "name": alias.name, "line": node.lineno})
                        total_imports += 1
                elif isinstance(node, ast.ImportFrom):
                    imports.append({"type": "import_from", "module": node.module or '', "level": node.level, "line": node.lineno})
                    total_imports += 1
                    
                    # Check relative import existence
                    if node.level > 0:
                        target_dir = py_file.parent
                        for _ in range(node.level - 1):
                            target_dir = target_dir.parent
                        mod_parts = (node.module or '').split('.')
                        expected_py = target_dir.joinpath(*mod_parts).with_suffix('.py')
                        expected_pkg = target_dir.joinpath(*mod_parts) / '__init__.py'
                        if not expected_py.exists() and not expected_pkg.exists():
                            broken_imports.append({
                                "file": rel_path,
                                "line": node.lineno,
                                "module": node.module,
                                "level": node.level
                            })

            file_reports.append({
                "file": rel_path,
                "import_count": len(imports),
                "imports": imports
            })
        except SyntaxError as se:
            file_reports.append({
                "file": rel_path,
                "syntax_error": str(se)
            })
        except Exception as e:
            file_reports.append({
                "file": rel_path,
                "error": str(e)
            })

    return {
        "total_files_analyzed": len(file_reports),
        "total_imports": total_imports,
        "broken_relative_imports": broken_imports,
        "files": file_reports
    }

def main():
    root_dir = Path.cwd()
    output_file = Path(".agents/reports/ast_import_report.json")
    
    if len(sys.argv) > 1 and sys.argv[1] == "--root" and len(sys.argv) > 2:
        root_dir = Path(sys.argv[2])
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_file = Path(sys.argv[idx + 1])

    output_file.parent.mkdir(parents=True, exist_ok=True)
    report = analyze_ast(root_dir.resolve())
    output_file.write_text(json.dumps(report, indent=2), encoding='utf-8')
    
    print(f"✅ AST Import Analysis completed:")
    print(f"   • Files analyzed: {report['total_files_analyzed']}")
    print(f"   • Total imports: {report['total_imports']}")
    print(f"   • Broken relative imports: {len(report['broken_relative_imports'])}")
    print(f"   • Report written to: {output_file}")
    
    if report["broken_relative_imports"]:
        sys.exit(1)

if __name__ == '__main__':
    main()

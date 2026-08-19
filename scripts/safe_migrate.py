#!/usr/bin/env python3
"""
Safe Migration Pipeline for repo-organizer-skill
Executes migration plans via git mv, runs invariant verification, and enforces automatic rollback on failure.
"""

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict

def run_cmd(cmd: list) -> tuple:
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, p.stdout.strip(), p.stderr.strip()

def execute_migration(plan: Dict[str, str], dry_run: bool = False, root_dir: Path = None) -> bool:
    if root_dir is None:
        root_dir = Path.cwd()
        
    print(f"📦 Processing migration plan ({len(plan)} actions)...")
    
    # Validation phase
    errors = []
    for src_rel, dst_rel in plan.items():
        src_path = root_dir / src_rel
        dst_path = root_dir / dst_rel
        if not src_path.exists():
            errors.append(f"Source file does not exist: {src_rel}")
        if dst_path.exists() and src_path.resolve() != dst_path.resolve():
            errors.append(f"Destination target already exists: {dst_rel}")

    if errors:
        print("❌ Migration validation failed:")
        for err in errors:
            print(f"   • {err}")
        return False

    if dry_run:
        print("🔍 DRY-RUN MODE: Simulating file relocations:")
        for src_rel, dst_rel in plan.items():
            print(f"   [DRY-RUN] git mv '{src_rel}' ──► '{dst_rel}'")
        print("✅ Dry-run completed successfully.")
        return True

    # Execution phase
    executed_moves = []
    for src_rel, dst_rel in plan.items():
        src_path = root_dir / src_rel
        dst_path = root_dir / dst_rel
        
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        
        ret, out, err = run_cmd(["git", "mv", str(src_rel), str(dst_rel)])
        if ret != 0:
            # Fallback to os.rename + git add
            try:
                os.rename(src_path, dst_path)
                run_cmd(["git", "add", str(dst_rel)])
                run_cmd(["git", "rm", "--cached", str(src_rel)])
            except Exception as ex:
                print(f"❌ Failed to move '{src_rel}' to '{dst_rel}': {ex}")
                print("🔴 Triggering rollback...")
                run_cmd(["git", "reset", "--hard", "HEAD"])
                return False
        executed_moves.append((src_rel, dst_rel))
        print(f"   ✔ Moved: '{src_rel}' ──► '{dst_rel}'")

    # Invariant verification phase
    print("🛡️ Running post-migration invariant verification...")
    checker_script = root_dir / "scripts" / "invariant_checker.py"
    if checker_script.exists():
        ret, out, err = run_cmd([sys.executable, str(checker_script), "verify", "--root", str(root_dir)])
        print(out)
        if ret != 0:
            print("🔴 INVARIANT VERIFICATION FAILED! Triggering automatic rollback...")
            run_cmd(["git", "reset", "--hard", "HEAD"])
            return False
            
    print("🟢 MIGRATION & VERIFICATION PASSED SUCCESSFULLY!")
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: safe_migrate.py --plan PLAN_FILE [--dry-run] [--root DIR]")
        sys.exit(1)
        
    plan_file = None
    dry_run = "--dry-run" in sys.argv
    root_dir = Path.cwd()
    
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "--plan" and i + 1 < len(sys.argv):
            plan_file = Path(sys.argv[i+1])
        elif sys.argv[i] == "--root" and i + 1 < len(sys.argv):
            root_dir = Path(sys.argv[i+1])
            
    if not plan_file or not plan_file.exists():
        print(f"❌ Migration plan file not found: {plan_file}")
        sys.exit(1)
        
    plan = json.loads(plan_file.read_text(encoding='utf-8'))
    success = execute_migration(plan, dry_run=dry_run, root_dir=root_dir.resolve())
    if not success:
        sys.exit(1)

if __name__ == '__main__':
    main()

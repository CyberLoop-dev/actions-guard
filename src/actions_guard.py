#!/usr/bin/env python3
"""Static checks for common GitHub Actions workflow security footguns."""
import argparse,re,sys
from pathlib import Path
SHA=re.compile(r"^[0-9a-fA-F]{40}$")
def audit(path):
 text=path.read_text(encoding="utf-8"); findings=[]
 if not re.search(r"(?m)^permissions\s*:",text): findings.append(("warning","No explicit permissions block; set least-privilege permissions"))
 if re.search(r"(?m)^\s*pull_request_target\s*:",text): findings.append(("high","pull_request_target needs careful handling of untrusted code"))
 for line_no,line in enumerate(text.splitlines(),1):
  match=re.search(r"\buses:\s*([^\s#]+)",line)
  if match:
   ref=match.group(1).rsplit("@",1)
   if len(ref)==2 and "/" in ref[0] and not SHA.fullmatch(ref[1]): findings.append(("warning",f"Line {line_no}: action is not pinned to a full commit SHA"))
  if "persist-credentials: true" in line: findings.append(("warning",f"Line {line_no}: checkout credentials persist in the worktree"))
  if "secrets: inherit" in line: findings.append(("warning",f"Line {line_no}: reusable workflow inherits all caller secrets"))
 return findings
def main():
 ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("path",type=Path); args=ap.parse_args()
 files=sorted(args.path.glob("*.yml"))+sorted(args.path.glob("*.yaml")) if args.path.is_dir() else [args.path]; total=0
 for path in files:
  try: findings=audit(path)
  except OSError as exc: print(f"{path}: {exc}"); total+=1; continue
  for level,message in findings: print(f"{path}: {level.upper()}: {message}"); total+=1
  if not findings: print(f"{path}: OK")
 print(f"{total} finding(s) across {len(files)} workflow file(s)")
 return 1 if total else 0
if __name__=="__main__": sys.exit(main())

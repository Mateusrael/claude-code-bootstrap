"""PostToolUse hook: run rustfmt on .rs files after Edit/Write."""

import json
import subprocess
import sys

data = json.load(sys.stdin)
file_path = data.get("tool_input", {}).get("file_path", "")

if not file_path or not file_path.endswith(".rs"):
    sys.exit(0)

try:
    subprocess.run(["rustfmt", file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except FileNotFoundError:
    pass

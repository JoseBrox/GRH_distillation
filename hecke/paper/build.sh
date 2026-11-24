#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
python3 - "$tmp/input.md" <<'PY'
import re, pathlib, sys
s=pathlib.Path("main.md").read_text()
s=re.sub(r"(?ms)^\x60\x60\x60math\s*\n(.*?)^\x60\x60\x60\s*$",lambda m:"$$\n"+m.group(1).strip()+"\n$$\n",s)
# Avoid duplicating the YAML title in the body of the PDF.
s=re.sub(r"(?m)^# Arithmetic reductions toward Hecke GRH\s*$","",s,count=1)
pathlib.Path(sys.argv[1]).write_text(s)
PY
pandoc "$tmp/input.md" -f markdown+tex_math_dollars -s -t latex \
  -V geometry:margin=26mm -V fontsize=11pt -o main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory="$tmp" main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory="$tmp" main.tex
cp "$tmp/main.pdf" main.pdf

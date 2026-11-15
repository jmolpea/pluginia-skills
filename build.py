"""Empaqueta una skill de cliente en dist/NOMBRE.zip y comprueba que no lleva código del plugin.

Uso:  python _skills/build.py NOMBRE-SKILL
      python _skills/build.py --all
El zip lleva la carpeta NOMBRE-SKILL/ como raíz y rutas con '/'.
"""
import re
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ALLOWED = {".md", ".yaml", ".yml", ".svg"}
# Indicios de código fuente o secretos que nunca deben ir en una skill pública.
LEAKS = [
    (r"<\?php", "código PHP"),
    (r"\bfunction\s+\w+\s*\(", "definición de función"),
    (r"\$DB->|\$CFG->|\$PAGE->|\$USER->", "variables internas de Moodle"),
    (r"\bSELECT\s+.+\s+FROM\s+\{", "SQL"),
    (r"github\.com/jmolpea", "URL del repositorio"),
    (r"\bsk-[A-Za-z0-9_-]{20,}", "clave de API"),
    (r"\bclasses/[\w/]+\.php|\b\w+\.php\b", "ruta de archivo del plugin"),
]


def build(name: str) -> Path:
    src = HERE / name
    if not (src / "SKILL.md").is_file():
        raise SystemExit(f"No existe {src / 'SKILL.md'}")
    files = sorted(p for p in src.rglob("*") if p.is_file())
    problems = []
    for p in files:
        rel = p.relative_to(src).as_posix()
        if p.suffix.lower() not in ALLOWED:
            problems.append(f"{rel}: tipo de archivo no permitido")
            continue
        raw = p.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            problems.append(f"{rel}: tiene BOM")
        text = raw.decode("utf-8")
        for n, line in enumerate(text.splitlines(), 1):
            for pattern, what in LEAKS:
                if re.search(pattern, line, re.IGNORECASE):
                    problems.append(f"{rel}:{n}: posible {what}: {line.strip()[:90]}")
    head = (src / "SKILL.md").read_text(encoding="utf-8")
    m = re.search(r"^name:\s*(\S+)\s*$", head, re.MULTILINE)
    if not m or m.group(1) != name:
        problems.append("SKILL.md: el campo name no coincide con la carpeta")

    out = HERE / "dist" / f"{name}.zip"
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            z.write(p, f"{name}/{p.relative_to(src).as_posix()}")
    print(f"{name}: {out} ({len(files)} archivos, {out.stat().st_size // 1024} KB)")
    for pr in problems:
        print("  REVISAR ->", pr)
    return out


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    if sys.argv[1] == "--all":
        for d in sorted(p.parent.name for p in HERE.glob("*/SKILL.md")):
            build(d)
    else:
        build(sys.argv[1])

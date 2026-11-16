import subprocess
import sys
from pathlib import Path


def test_suite_bdd():
    raiz_proyecto = Path(__file__).resolve().parents[2]

    comando = [
        sys.executable,
        "-m",
        "behave",
        "Clase14/features/",
        "--format",
        "json",
        "--outfile",
        "Clase14/reports/reporte_bdd.json",
    ]

    resultado = subprocess.run(
        comando,
        cwd=raiz_proyecto,
        capture_output=True,
        text=True,
        check=False,
    )

    assert resultado.returncode == 0, (
        "La suite BDD presentó errores.\n"
        f"Salida:\n{resultado.stdout}\n"
        f"Errores:\n{resultado.stderr}"
    )

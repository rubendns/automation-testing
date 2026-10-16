from pathlib import Path

import pytest

from Clase10.utils.datos import leer_csv_login


# Construimos la ruta del CSV a partir de la ubicación del test
RUTA_CSV = Path(__file__).resolve().parents[1] / "datos" / "login.csv"

#Antes escribíamos los datos directamente en el archivo Python:
#CASOS_LOGIN = [
#    ("standard_user", "secret_sauce", True),
#    # ...
#]

# Ahora cargamos los casos desde el archivo externo
CASOS_LOGIN = leer_csv_login(RUTA_CSV)



@pytest.mark.parametrize(
    "usuario, clave, debe_funcionar",
    CASOS_LOGIN
)
def test_datos_login(usuario, clave, debe_funcionar):
    print(f"\nUsuario: {usuario}")
    print(f"Clave: {clave}")
    print(f"¿Debe funcionar?: {debe_funcionar}")

    assert isinstance(usuario, str)
    assert isinstance(clave, str)
    assert isinstance(debe_funcionar, bool)
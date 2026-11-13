import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


# Crear la carpeta de logs si no existe
carpeta_logs = Path("logs")
carpeta_logs.mkdir(parents=True, exist_ok=True)


def obtener_logger(nombre="automatizacion"):
    logger = logging.getLogger(nombre)
    logger.setLevel(logging.INFO)

    # Evitar agregar handlers duplicados
    if not logger.handlers:
        archivo_log = carpeta_logs / "suite.log"

        handler = RotatingFileHandler(
            archivo_log, maxBytes=1024 * 1024, backupCount=5, encoding="utf-8"
        )

        formato = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        handler.setFormatter(formato)
        logger.addHandler(handler)

    return logger

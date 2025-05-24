from enum import Enum

class EstadoPrenda(str, Enum):
    DISPONIBLE = "disponible"
    EN_USO = "en_uso"
    EN_REPARACION = "en_reparacion"
    DANADO = "danado"

class TipoReparacion(str, Enum):
    LIMPIEZA = "limpieza"
    REPARACION = "reparacion"
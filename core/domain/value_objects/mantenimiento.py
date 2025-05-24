from datetime import datetime
from pydantic import BaseModel
from ..enums import TipoReparacion

class Mantenimiento(BaseModel):
    fecha: datetime
    tipo: TipoReparacion
    observaciones: str
from datetime import datetime
from pydantic import BaseModel, Field

class Asignacion(BaseModel):
    bailarin_id: str
    evento_id: str
    fecha_asignacion: datetime = Field(default_factory=datetime.now)
    fecha_devolucion: datetime = None
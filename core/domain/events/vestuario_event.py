from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DomainEvent(BaseModel):
    event_type: str
    timestamp: datetime = datetime.utcnow()

class VestuarioAsignado(DomainEvent):
    vestuario_id: str
    evento_id: str
    event_type: str = "vestuario_asignado"

class PrendaDanada(DomainEvent):
    vestuario_id: str
    observaciones: str
    event_type: str = "prenda_danada"
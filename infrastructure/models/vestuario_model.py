from sqlalchemy import Column, String, Enum, JSON
from sqlalchemy.ext.declarative import declarative_base
from core.domain.enums import EstadoPrenda

Base = declarative_base()

class VestuarioDB(Base):
    __tablename__ = "vestuarios"
    id = Column(String, primary_key=True)
    tipo = Column(String(50))
    talla = Column(String(10))
    estado = Column(Enum(EstadoPrenda))
    historial_uso = Column(JSON)
    historial_mantenimiento = Column(JSON)
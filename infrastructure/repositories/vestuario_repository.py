from sqlalchemy.orm import Session
from core.application.interfaces.repositories import IVestuarioRepository
from core.domain.aggregates.vestuario import Vestuario
from infrastructure.models.vestuario_model import VestuarioDB
from core.domain.value_objects.asignacion import Asignacion
from core.domain.value_objects.mantenimiento import Mantenimiento
from pydantic import parse_obj_as
from typing import List

class SQLAlchemyVestuarioRepository(IVestuarioRepository):
    def __init__(self, db: Session):
        self.db = db

    def get(self, vestuario_id: str) -> Vestuario:
        db_vestuario = self.db.query(VestuarioDB).filter_by(id=vestuario_id).first()
        if not db_vestuario:
            return None
        return Vestuario(
            id=db_vestuario.id,
            tipo=db_vestuario.tipo,
            talla=db_vestuario.talla,
            estado=db_vestuario.estado,
            historial_uso=parse_obj_as(List[Asignacion], db_vestuario.historial_uso),
            historial_mantenimiento=parse_obj_as(List[Mantenimiento], db_vestuario.historial_mantenimiento)
        )

    def save(self, vestuario: Vestuario):
        db_vestuario = self.db.query(VestuarioDB).filter_by(id=vestuario.id).first()
        if db_vestuario:
            db_vestuario.tipo = vestuario.tipo
            db_vestuario.talla = vestuario.talla
            db_vestuario.estado = vestuario.estado
            db_vestuario.historial_uso = [a.dict() for a in vestuario.historial_uso]
            db_vestuario.historial_mantenimiento = [m.dict() for m in vestuario.historial_mantenimiento]
        else:
            nuevo_vestuario = VestuarioDB(
                id=vestuario.id,
                tipo=vestuario.tipo,
                talla=vestuario.talla,
                estado=vestuario.estado,
                historial_uso=[a.dict() for a in vestuario.historial_uso],
                historial_mantenimiento=[m.dict() for m in vestuario.historial_mantenimiento]
            )
            self.db.add(nuevo_vestuario)
        self.db.commit()
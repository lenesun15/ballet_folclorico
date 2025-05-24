from datetime import datetime
from typing import List
from pydantic import BaseModel
from enums import EstadoPrenda, TipoReparacion
from value_objects.asignacion import Asignacion
from value_objects.mantenimiento import Mantenimiento

class Vestuario(BaseModel):
    id: str
    tipo: str
    talla: str
    estado: EstadoPrenda = EstadoPrenda.DISPONIBLE
    historial_uso: List[Asignacion] = []
    historial_mantenimiento: List[Mantenimiento] = []

    def asignar_a_evento(self, bailarin_id: str, evento_id: str):
        if self.estado != EstadoPrenda.DISPONIBLE:
            raise ValueError("La prenda no está disponible")
        self.estado = EstadoPrenda.EN_USO
        self.historial_uso.append(
            Asignacion(bailarin_id=bailarin_id, evento_id=evento_id)
        )

    def devolver(self):
        if self.estado != EstadoPrenda.EN_USO:
            raise ValueError("La prenda no está en uso")
        self.estado = EstadoPrenda.DISPONIBLE
        ultima_asignacion = self.historial_uso[-1]
        ultima_asignacion.fecha_devolucion = datetime.now()

    def marcar_como_danado(self, observaciones: str):
        self.estado = EstadoPrenda.DANADO
        self.historial_mantenimiento.append(
            Mantenimiento(
                fecha=datetime.now(),
                tipo=TipoReparacion.REPARACION,
                observaciones=observaciones
            )
        )
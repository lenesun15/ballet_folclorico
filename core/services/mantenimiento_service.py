from core.domain.aggregates.vestuario import Vestuario
from core.domain.enums import TipoReparacion, EstadoPrenda
from core.domain.value_objects.mantenimiento import Mantenimiento
from datetime import datetime

class MantenimientoService:
    def programar_mantenimiento_preventivo(self, vestuario: Vestuario):
        if vestuario.estado != EstadoPrenda.DISPONIBLE:
            raise ValueError("La prenda debe estar disponible para mantenimiento preventivo")
        
        vestuario.historial_mantenimiento.append(
            Mantenimiento(
                fecha=datetime.utcnow(),
                tipo=TipoReparacion.LIMPIEZA,
                observaciones="Mantenimiento programado automáticamente"
            )
        )
import json
import logging
from typing import Dict, Type
from core.domain.events.vestuario_event import VestuarioAsignado, PrendaDanada

logger = logging.getLogger(__name__)

class EventPublisher:
    def __init__(self):
        self.handlers: Dict[str, Type[BaseEventHandler]] = {
            VestuarioAsignado.__name__: VestuarioAsignadoHandler,
            PrendaDanada.__name__: PrendaDanadaHandler
        }

    def publish(self, event):
        """Publica eventos de dominio a través del handler correspondiente"""
        event_type = type(event).__name__
        handler_class = self.handlers.get(event_type)
        
        if not handler_class:
            logger.error(f"No handler registrado para el evento: {event_type}")
            return
        
        try:
            handler = handler_class()
            handler.handle(event)
            logger.info(f"Evento {event_type} publicado exitosamente")
        except Exception as e:
            logger.error(f"Error publicando evento {event_type}: {str(e)}")
            raise

class BaseEventHandler:
    """Clase base para handlers de eventos"""
    def handle(self, event):
        raise NotImplementedError

class VestuarioAsignadoHandler(BaseEventHandler):
    def handle(self, event: VestuarioAsignado):
        message = {
            "vestuario_id": event.vestuario_id,
            "evento_id": event.evento_id,
            "timestamp": event.timestamp.isoformat()
        }
        self._send_to_broker("vestuario.asignado", message)

    def _send_to_broker(self, topic: str, message: dict):
        print(f"Enviando a {topic}: {json.dumps(message)}")

class PrendaDanadaHandler(BaseEventHandler):
    def handle(self, event: PrendaDanada):
        message = {
            "vestuario_id": event.vestuario_id,
            "observaciones": event.observaciones,
            "timestamp": event.timestamp.isoformat()
        }
        self._send_to_broker("prenda.danada", message)

    def _send_to_broker(self, topic: str, message: dict):
        print(f"Enviando a {topic}: {json.dumps(message)}")
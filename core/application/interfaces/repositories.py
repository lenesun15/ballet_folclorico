from abc import ABC, abstractmethod
from core.domain.aggregates.vestuario import Vestuario

class IVestuarioRepository(ABC):
    @abstractmethod
    def get(self, vestuario_id: str) -> Vestuario:
        pass

    @abstractmethod
    def save(self, vestuario: Vestuario):
        pass
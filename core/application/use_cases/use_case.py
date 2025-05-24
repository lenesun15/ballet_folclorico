from core.domain.aggregates.vestuario import Vestuario
from core.application.interfaces.repositories import IVestuarioRepository

class VestuarioUseCase:
    def __init__(self, repo: IVestuarioRepository):
        self.repo = repo

    def asignar_vestuario_a_evento(self, vestuario_id: str, bailarin_id: str, evento_id: str):
        vestuario = self.repo.get(vestuario_id)
        vestuario.asignar_a_evento(bailarin_id, evento_id)
        self.repo.save(vestuario)
        return vestuario.pull_domain_events()

    def devolver_vestuario(self, vestuario_id: str):
        vestuario = self.repo.get(vestuario_id)
        vestuario.devolver()
        self.repo.save(vestuario)
        return vestuario.pull_domain_events()

    def reportar_dano(self, vestuario_id: str, observaciones: str):
        vestuario = self.repo.get(vestuario_id)
        vestuario.marcar_como_danado(observaciones)
        self.repo.save(vestuario)
        return vestuario.pull_domain_events()
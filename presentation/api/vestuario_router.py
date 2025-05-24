from fastapi import APIRouter, Depends, HTTPException
from core.application.use_cases.use_case import VestuarioUseCase
from core.domain.aggregates.vestuario import Vestuario
from presentation.api.dependencies import get_vestuario_use_case

router = APIRouter()

@router.post("/vestuarios/{vestuario_id}/asignar")
def asignar_vestuario(
    vestuario_id: str,
    bailarin_id: str,
    evento_id: str,
    use_case: VestuarioUseCase = Depends(get_vestuario_use_case)
):
    try:
        events = use_case.asignar_vestuario_a_evento(vestuario_id, bailarin_id, evento_id)
        return {"message": "Vestuario asignado", "events": [e.dict() for e in events]}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/vestuarios/{vestuario_id}/devolver")
def devolver_vestuario(
    vestuario_id: str,
    use_case: VestuarioUseCase = Depends(get_vestuario_use_case)
):
    try:
        events = use_case.devolver_vestuario(vestuario_id)
        return {"message": "Vestuario devuelto", "events": [e.dict() for e in events]}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
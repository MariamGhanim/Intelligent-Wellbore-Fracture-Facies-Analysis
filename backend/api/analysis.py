from fastapi import APIRouter

router = APIRouter()


@router.post("/{well_id}/start")
def start_analysis(well_id: int):
    return {"well_id": well_id, "status": "idle"}


@router.get("/{well_id}/status")
def analysis_status(well_id: int):
    return {"well_id": well_id, "status": "idle"}

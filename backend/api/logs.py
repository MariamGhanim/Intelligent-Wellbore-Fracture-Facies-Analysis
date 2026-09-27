from fastapi import APIRouter

router = APIRouter()


@router.get("/{well_id}")
def list_logs(well_id: int):
    return {"well_id": well_id, "curves": []}

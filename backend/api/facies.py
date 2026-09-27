from fastapi import APIRouter

router = APIRouter()


@router.get("/{well_id}")
def list_facies(well_id: int):
    return {"well_id": well_id, "available": False, "zones": []}

from fastapi import APIRouter

router = APIRouter()


@router.get("/{well_id}")
def list_fractures(well_id: int, depth_min: float | None = None, depth_max: float | None = None):
    return {"well_id": well_id, "depth_min": depth_min, "depth_max": depth_max, "fractures": []}

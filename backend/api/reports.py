from fastapi import APIRouter

router = APIRouter()


@router.get("")
def list_reports():
    return []


@router.get("/{report_id}")
def get_report(report_id: int):
    return {"id": report_id, "status": "not_implemented"}


@router.get("/{report_id}/download")
def download_report(report_id: int):
    return {"id": report_id, "status": "not_implemented"}

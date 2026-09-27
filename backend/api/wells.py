from fastapi import APIRouter, UploadFile

router = APIRouter()


@router.get("")
def list_wells():
    return []


@router.post("/upload")
def upload_well(fmi: UploadFile | None = None, logs: UploadFile | None = None):
    return {
        "status": "not_implemented",
        "fmi": fmi.filename if fmi else None,
        "logs": logs.filename if logs else None,
    }

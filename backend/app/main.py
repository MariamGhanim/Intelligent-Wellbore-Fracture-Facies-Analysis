from fastapi import FastAPI

from app.database.connection import get_connection


app = FastAPI(
    title="Intelligent Wellbore Fracture & Facies Analysis API",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    connection = get_connection()
    connection.close()

    return {
        "status": "ok",
        "database": "connected",
    }
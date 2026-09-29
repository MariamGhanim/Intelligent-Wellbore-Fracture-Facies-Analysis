from fastapi import FastAPI

from app.database.connection import get_connection
from app.database.init_db import create_users_table
from app.api.routes.auth import router as auth_router


app = FastAPI(
    title="Intelligent Wellbore Fracture & Facies Analysis API",
    version="1.0.0",
)


create_users_table()

app.include_router(auth_router)

@app.get("/health")
def health_check():
    connection = get_connection()
    connection.close()

    return {
        "status": "ok",
        "database": "connected",
    }
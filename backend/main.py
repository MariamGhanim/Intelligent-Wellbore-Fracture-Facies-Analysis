from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api import agent, analysis, auth, facies, fractures, logs, reports, wells
from backend.database.database import init_db

app = FastAPI(title="Intelligent Wellbore Fracture & Facies Analysis")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(wells.router, prefix="/api/wells", tags=["wells"])
app.include_router(analysis.router, prefix="/api/analysis", tags=["analysis"])
app.include_router(fractures.router, prefix="/api/fractures", tags=["fractures"])
app.include_router(facies.router, prefix="/api/facies", tags=["facies"])
app.include_router(logs.router, prefix="/api/logs", tags=["logs"])
app.include_router(reports.router, prefix="/api/reports", tags=["reports"])
app.include_router(agent.router, prefix="/api/agent", tags=["agent"])

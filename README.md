# Intelligent Wellbore Fracture & Facies Analysis

An AI-based web app for interpreting FMI wellbore images and conventional well logs. This repository currently holds the initial application structure: a FastAPI backend, a React dashboard shell, and empty modules for fracture detection, geometry, facies, and the assistant.

## Run the backend

From the project root:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload
```

The API is at http://127.0.0.1:8000 and the health check is http://127.0.0.1:8000/health.

## Run the frontend

```bash
cd frontend
npm install
npm run dev
```

The dashboard is at http://localhost:5173.

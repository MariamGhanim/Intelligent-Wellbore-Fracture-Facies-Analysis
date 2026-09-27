from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class SignupRequest(BaseModel):
    name: str
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


class ResetPasswordRequest(BaseModel):
    email: str
    new_password: str


@router.post("/signup")
def signup(body: SignupRequest):
    return {"status": "not_implemented", "email": body.email}


@router.post("/login")
def login(body: LoginRequest):
    return {"status": "not_implemented", "email": body.email}


@router.post("/logout")
def logout():
    return {"status": "not_implemented"}


@router.get("/me")
def current_user():
    return {"status": "not_implemented", "user": None}


@router.post("/reset-password")
def reset_password(body: ResetPasswordRequest):
    return {"status": "not_implemented", "email": body.email}

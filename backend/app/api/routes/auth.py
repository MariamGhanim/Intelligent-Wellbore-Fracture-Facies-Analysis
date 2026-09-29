from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.auth import (
    SignupRequest,
    LoginRequest,
    ResetPasswordRequest,
)

from app.services.auth_service import (
    signup_user,
    login_user,
    reset_password,
)

from app.core.dependencies import get_current_user


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(request: SignupRequest):
    try:
        user = signup_user(
            name=request.name,
            email=request.email,
            password=request.password,
        )

        return {
            "message": "User registered successfully",
            "user": user,
        }

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        )


@router.post("/login")
def login(request: LoginRequest):
    try:
        result = login_user(
            email=request.email,
            password=request.password,
        )

        return {
            "message": "Login successful",
            **result,
        }

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(error),
        )


@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return {
        "user": dict(current_user),
    }


@router.post("/logout")
def logout():
    return {
        "message": "Logout successful"
    }


@router.post("/reset-password")
def reset_user_password(request: ResetPasswordRequest):
    try:
        result = reset_password(
            email=request.email,
            new_password=request.new_password,
        )

        return result

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error),
        )

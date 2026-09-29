from app.core.security import hash_password, verify_password, create_access_token
from app.database.user_repository import (
    create_user,
    get_user_by_email,
    update_user_password,
)

def signup_user(name: str, email: str, password: str):
    existing_user = get_user_by_email(email)

    if existing_user:
        raise ValueError("Email already registered")

    password_hash = hash_password(password)

    user_id = create_user(
        name=name,
        email=email,
        password_hash=password_hash,
    )

    return {
        "id": user_id,
        "name": name,
        "email": email,
    }


def login_user(email: str, password: str):
    user = get_user_by_email(email)

    if not user:
        raise ValueError("Invalid email or password")

    if not verify_password(password, user["password_hash"]):
        raise ValueError("Invalid email or password")

    access_token = create_access_token(user["id"])

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
        },
    }


def reset_password(email: str, new_password: str):
    user = get_user_by_email(email)

    if not user:
        raise ValueError("User not found")

    password_hash = hash_password(new_password)

    update_user_password(
        user_id=user["id"],
        password_hash=password_hash,
    )

    return {
        "message": "Password reset successfully"
    }
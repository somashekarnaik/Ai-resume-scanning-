from fastapi import (
    APIRouter,
    HTTPException
)

from ..schemas import (
    RegisterRequest,
    LoginRequest
)

from ..database import (
    create_user,
    get_user
)


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    data: RegisterRequest
):
    user_id = create_user(
        data.name,
        data.email,
        data.password
    )

    if user_id is None:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    return {
        "message": "Registration successful.",
        "user_id": user_id
    }


@router.post("/login")
def login(
    data: LoginRequest
):
    user = get_user(
        data.email,
        data.password
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    return {
        "message": "Login successful.",
        "user_id": user["id"],
        "name": user["name"]
    }
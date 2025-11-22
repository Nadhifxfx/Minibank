from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    pin: str

class LoginResponse(BaseModel):
    status: str
    data: dict
    message: str | None = None

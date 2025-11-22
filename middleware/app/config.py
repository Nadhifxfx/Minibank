from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "MiniBank Middleware"
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # JWT
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # Services (internal)
    SERVICE_BASE_URL: str = "http://services:8001"

    # Redis for rate limiter & blacklist
    REDIS_URL: str = "redis://redis:6379/0"

    # Security
    CORS_ORIGINS: list = ["*"]  # adjust in production

    class Config:
        env_file = "../.env"

settings = Settings()

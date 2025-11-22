from fastapi import FastAPI
from app.routers import auth, account, transaction
from app.logging_config import logger
from app.config import settings
from app.security.rate_limiter import init_rate_limiter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.APP_NAME)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers
app.include_router(auth.router)
app.include_router(account.router)
app.include_router(transaction.router)

@app.on_event("startup")
async def startup():
    logger.info("Starting middleware...")
    await init_rate_limiter(app)

@app.get("/health")
async def health():
    return {"status": "ok"}

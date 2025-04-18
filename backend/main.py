from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.core.cache import cache
from src.core.logger import logger
from src.core.config import settings
from src.core.middleware import middlewares
from src.modules.sales.interfaces.api.sales_router import sales_router
from src.modules.ai_prompt.interfaces.api.prompt_router import prompt_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await cache.connect()
    yield
    await cache.disconnect()

app = FastAPI(lifespan=lifespan)

for list in middlewares:
    app.add_middleware(list["middleware_class"], **list["options"])


# app.include_router(router)
app.include_router(sales_router, prefix="/api/sales-reps", tags=["Sales"])
app.include_router(prompt_router, prefix="/api/ai", tags=["Prompt"])

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}

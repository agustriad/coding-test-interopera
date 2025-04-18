import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "InterOpera Test Service"
    PROJECT_VERSION: str = "1.0.0"
    ENV: str = os.getenv("ENV", "development")
    PORT: int = int(os.getenv("PORT", 8080))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")

    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))

    # POSTGRES_USER: str = os.getenv("postgres")
    # POSTGRES_PASSWORD = os.getenv("postgres")
    # POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    # POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)  # default postgres port is 5432
    # POSTGRES_DB: str = os.getenv("POSTGRES_DB", "test")
    # DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()


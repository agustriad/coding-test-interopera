import logging
from src.core.config import settings

logger = logging.getLogger(settings.PROJECT_NAME)
logger.setLevel("INFO")

handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)

logger.addHandler(handler)
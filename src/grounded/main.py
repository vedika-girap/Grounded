import logging

from fastapi import FastAPI

from grounded.api import health
from grounded.config import get_settings
from grounded.logging import setup_logging

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    settings = get_settings()
    setup_logging(settings.log_level)

    app = FastAPI(title=settings.app_name)
    app.include_router(health.router)

    logger.info("app created", extra={"environment": settings.environment})
    return app


app = create_app()

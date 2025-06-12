# src/scrap_generator/app.py

from fastapi import FastAPI

from .config import settings
from .generator.generator import MetricsGenerator
from .generator.churn import ChurnManager
from .routes.metrics import router as metrics_router


def create_app() -> FastAPI:
    app = FastAPI()

    generator = MetricsGenerator(settings)
    ChurnManager(generator, settings.churn_interval)

    app.state.generator = generator

    app.include_router(metrics_router)

    return app

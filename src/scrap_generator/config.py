# src/scrap_generator/config.py

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    series_count: int = Field(10, description="Number of series to generate")
    metric_name: str = Field(
        "test_metric", description="Metric name to use")
    port: int = Field(9001, description="Port to run the server on")
    labels_count: int = Field(3, description="Number of labels to generate")
    churn_interval: int = Field(
        0, description="Churn interval in seconds, 0 means no churn")
    static_values: bool = Field(
        False, description="Use static values on /metrics (disable randomization)")

    class Config:
        env_prefix = "SG_"


settings = Settings()

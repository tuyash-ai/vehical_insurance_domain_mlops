"""Configuration module for loading environment variables."""

import os
from pathlib import Path

from dotenv import load_dotenv

from app.core import ConfigurationError, logger

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    """Application settings loaded from environment variables."""

    def __init__(self):
        """Initialize settings with environment variables and defaults."""
        # Database
        self.MONGODB_URL = os.getenv("MONGODB_URL")
        self.DB_NAME = os.getenv("DB_NAME", "vehicle_insurance")

        # API
        self.API_HOST = os.getenv("API_HOST", "localhost")
        try:
            self.API_PORT = int(os.getenv("API_PORT", "8000"))
        except ValueError:
            logger.error("API_PORT must be an integer")
            raise ConfigurationError("Invalid API_PORT configuration")

        self.DEBUG = os.getenv("DEBUG", "false").lower() == "true"

        # Model
        self.MODEL_PATH = os.getenv("MODEL_PATH")
        try:
            self.BATCH_SIZE = int(os.getenv("BATCH_SIZE", "32"))
        except ValueError:
            logger.error("BATCH_SIZE must be an integer")
            raise ConfigurationError("Invalid BATCH_SIZE configuration")

        # Logging
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

        self._validate()

    def _validate(self) -> None:
        """Validate critical settings."""
        if not self.MODEL_PATH:
            logger.warning("MODEL_PATH not set in environment variables")
        if not self.MONGODB_URL:
            logger.warning("MONGODB_URL not set in environment variables")

        logger.debug(
            f"Settings loaded: API={self.API_HOST}:{self.API_PORT}, "
            f"Debug={self.DEBUG}, LogLevel={self.LOG_LEVEL}"
        )


settings = Settings()
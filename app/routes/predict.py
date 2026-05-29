"""Prediction routes."""

from app.core.logger import logger


def predict():
    """Handle prediction endpoint."""
    logger.info("Prediction endpoint called")
    return {"status": "ok", "message": "Prediction endpoint"}

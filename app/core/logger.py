"""Logger configuration using loguru."""

import sys
from loguru import logger
from pathlib import Path

Path("logs").mkdir(exist_ok=True)  # Ensure logs directory exists


# Remove default handler
logger.remove()

# Add console handler with custom format
logger.add(
    sys.stdout, # Log to standard output
    format="<level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="DEBUG",
)

# Add file handler for persistent logging
logger.add(
    "logs/app.log",
    enqueue=True,  # Use a queue to avoid blocking
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="INFO",
    rotation="500 MB",
    retention="7 days",
)

__all__ = ["logger"]

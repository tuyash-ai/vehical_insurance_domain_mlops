"""Custom exceptions for the application."""


class AppException(Exception):
    """Base exception for the application."""

    pass


class PredictionError(AppException):
    """Raised when prediction fails."""

    pass


class ModelLoadError(AppException):
    """Raised when model loading fails."""

    pass


class DataValidationError(AppException):
    """Raised when data validation fails."""

    pass


class ConfigurationError(AppException):
    """Raised when configuration is invalid."""

    pass

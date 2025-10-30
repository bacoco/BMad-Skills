#!/usr/bin/env python3
"""
BMAD Skills - Structured Logging Module

Provides consistent logging across all Python scripts with:
- Standard log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Uniform timestamp format
- Color-coded terminal output
- Optional verbose mode
- Structured error reporting
"""

import sys
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional

# ANSI color codes for terminal output
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'

    # Foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Background colors
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'


class ColoredFormatter(logging.Formatter):
    """Custom formatter with color-coded log levels"""

    LEVEL_COLORS = {
        logging.DEBUG: Colors.CYAN,
        logging.INFO: Colors.GREEN,
        logging.WARNING: Colors.YELLOW,
        logging.ERROR: Colors.RED,
        logging.CRITICAL: Colors.BG_RED + Colors.WHITE,
    }

    def __init__(self, fmt=None, datefmt=None, use_colors=True):
        super().__init__(fmt, datefmt)
        self.use_colors = use_colors and sys.stdout.isatty()

    def format(self, record):
        if self.use_colors:
            # Color the level name
            levelname = record.levelname
            if record.levelno in self.LEVEL_COLORS:
                colored_levelname = (
                    f"{self.LEVEL_COLORS[record.levelno]}"
                    f"{levelname:8s}"
                    f"{Colors.RESET}"
                )
                record.levelname = colored_levelname

        return super().format(record)


class BMadLogger:
    """
    Structured logger for BMAD Skills

    Usage:
        from logger import get_logger

        logger = get_logger(__name__)
        logger.info("Starting workflow")
        logger.error("Failed to process", exc_info=True)
    """

    _loggers = {}
    _default_level = logging.INFO
    _verbose_mode = False

    @classmethod
    def get_logger(
        cls,
        name: str,
        level: Optional[int] = None,
        log_file: Optional[str] = None,
    ) -> logging.Logger:
        """
        Get or create a logger instance

        Args:
            name: Logger name (usually __name__)
            level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            log_file: Optional file path for file logging

        Returns:
            Configured logger instance
        """
        if name in cls._loggers:
            return cls._loggers[name]

        logger = logging.getLogger(name)

        # Set level (verbose mode overrides)
        if cls._verbose_mode:
            logger.setLevel(logging.DEBUG)
        elif level is not None:
            logger.setLevel(level)
        else:
            logger.setLevel(cls._default_level)

        # Prevent duplicate handlers
        if logger.handlers:
            return logger

        # Console handler with color formatting
        console_handler = logging.StreamHandler(sys.stdout)
        console_formatter = ColoredFormatter(
            fmt='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            use_colors=True
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        # File handler (optional)
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_formatter = logging.Formatter(
                fmt='%(asctime)s [%(levelname)8s] %(name)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

        cls._loggers[name] = logger
        return logger

    @classmethod
    def set_verbose(cls, verbose: bool = True):
        """Enable/disable verbose (DEBUG) mode for all loggers"""
        cls._verbose_mode = verbose
        level = logging.DEBUG if verbose else cls._default_level

        for logger in cls._loggers.values():
            logger.setLevel(level)

    @classmethod
    def set_default_level(cls, level: int):
        """Set default log level for new loggers"""
        cls._default_level = level


# Convenience function for getting loggers
def get_logger(
    name: str,
    level: Optional[int] = None,
    log_file: Optional[str] = None,
    verbose: bool = False,
) -> logging.Logger:
    """
    Get a configured logger instance

    Args:
        name: Logger name (usually __name__)
        level: Log level (default: INFO)
        log_file: Optional file path for file logging
        verbose: Enable DEBUG level logging

    Returns:
        Configured logger

    Example:
        logger = get_logger(__name__, verbose=True)
        logger.debug("Debug information")
        logger.info("Processing started")
        logger.warning("Unusual condition detected")
        logger.error("Failed to complete task", exc_info=True)
    """
    if verbose:
        BMadLogger.set_verbose(True)

    return BMadLogger.get_logger(name, level, log_file)


# Convenience functions for one-off logging
def debug(message: str, *args, **kwargs):
    """Log debug message"""
    logger = get_logger('bmad')
    logger.debug(message, *args, **kwargs)


def info(message: str, *args, **kwargs):
    """Log info message"""
    logger = get_logger('bmad')
    logger.info(message, *args, **kwargs)


def warning(message: str, *args, **kwargs):
    """Log warning message"""
    logger = get_logger('bmad')
    logger.warning(message, *args, **kwargs)


def error(message: str, *args, **kwargs):
    """Log error message"""
    logger = get_logger('bmad')
    logger.error(message, *args, **kwargs)


def critical(message: str, *args, **kwargs):
    """Log critical message"""
    logger = get_logger('bmad')
    logger.critical(message, *args, **kwargs)


# Example usage
if __name__ == '__main__':
    # Test logger
    logger = get_logger(__name__, verbose=True)

    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    # Test with exception
    try:
        raise ValueError("Test exception")
    except Exception:
        logger.error("Caught exception", exc_info=True)

    print("\n--- Testing convenience functions ---\n")

    debug("Debug via convenience function")
    info("Info via convenience function")
    warning("Warning via convenience function")
    error("Error via convenience function")
    critical("Critical via convenience function")

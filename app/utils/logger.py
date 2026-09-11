import logging
import os


def setup_logger(app):
    """Configure Python's logging module to write app events to a file.

    Captures, per the assignment spec:
      1. successful logins
      2. failed logins
      3. new job posts created
      4. job posts edited/deleted
      5. external API request errors
    """
    log_path = app.config["LOG_FILE"]
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    logger = logging.getLogger("jobboard")
    logger.setLevel(logging.INFO)

    if not logger.handlers:  # avoid duplicate handlers on reload
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


# Module-level logger instance other files can import directly.
job_logger = logging.getLogger("jobboard")

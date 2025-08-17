import logging, datetime
from pathlib import Path


def configure_logger(lgr):
    """
    This function configures the given logger

    :param lgr: logger
    """
    # Make directory
    p = Path("./LOG")
    directory_exists = p.exists()
    p.mkdir(exist_ok=True)

    if not lgr.hasHandlers():
        # Set log file
        current_date = datetime.date.today().strftime("%d-%m-%Y")
        handler = logging.FileHandler(f"./LOG/{current_date}-{lgr.name}.log")

        # Set level and format
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setLevel(logging.INFO)
        lgr.setLevel(logging.INFO)

        # Add handler to logger
        handler.setFormatter(formatter)
        lgr.addHandler(handler)

        # Log changes and initialization
        if not directory_exists:
            logger.info("LOG directory added")
        lgr.info("logger setup completed")


# Initialize logger
logger = logging.getLogger(__name__)
configure_logger(logger)

import logging
import datetime

current_datetime = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M")

from pathlib import Path

def make_directory(directory):
    """
    This function creates a given directory if it does not already exist

    :param directory: given directory
    """
    p = Path(f"./{directory}/")
    directory_exists = p.exists()
    p.mkdir(exist_ok=True)

def configure_logger(lgr):
    """
    This function configures the given logger.

    :param lgr: The given logger.
    """

    # Make LOG directory
    dir_name = "LOG"
    make_directory(dir_name)

    if not lgr.hasHandlers():
        # Set log file name
        handler = logging.FileHandler(f"./{dir_name}/{current_datetime}.log")

        # Set level and format
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setLevel(logging.INFO)
        lgr.setLevel(logging.INFO)

        # Add handler to logger
        handler.setFormatter(formatter)
        lgr.addHandler(handler)

        lgr.info("Logger setup completed")

logger = logging.getLogger(__name__)
configure_logger(logger)
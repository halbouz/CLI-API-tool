import logging
import datetime
from directory_maker import make_directory

# Set current datetime, this will be used for naming the log
current_datetime = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M")

def configure_logger(lgr):
    """
    This function configures the given logger.

    :param lgr: The given logger.
    """

    # Create LOG directory
    dir_name = "LOG"
    directory_exists = make_directory(dir_name)

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

        # Log changes
        if not directory_exists:
            lgr.info(f"{dir_name} directory created.")
        lgr.info("Logger setup completed")

# Initialize logger
logger = logging.getLogger(__name__)
configure_logger(logger)
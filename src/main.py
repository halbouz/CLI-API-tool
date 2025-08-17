import logging
import logger_setup

logger = logging.getLogger(__name__)
logger_setup.configure_logger(logger)
logger.info("starting program")
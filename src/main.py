import logging
import logger_setup
import requests
from requests.exceptions import MissingSchema, InvalidURL, InvalidSchema


def main():
    # Initialize logger
    logger = logging.getLogger(__name__)
    logger_setup.configure_logger(logger)
    logger.info("Program started.")

    # Initialize variables
    valid_url = False
    response = ""
    url = ""

    # Continue asking the user for a URL until a valid one is retrieved
    while not valid_url:
        try:
            # Ask user to enter URL
            url = input("Please enter the URL you want to fetch data from: ").strip()

            # Try to get the URL, will raise exception if it is invalid
            response = requests.get(url)

            # Handle the case where a valid URL is retrieved
            valid_url = True
            logger.info("Valid URL retrieved.")

        except (InvalidSchema, MissingSchema):
            logger.error("User entered a URL with an invalid scheme.")
            print(f"The URL entered has an invalid scheme. It must start with http:// or https://")
        except (InvalidURL,requests.exceptions.ConnectionError):
            logger.error("User entered an invalid URL.")
            print(f"The URL entered is invalid. Please try again.")

if __name__ == "__main__":
    main()
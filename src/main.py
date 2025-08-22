import logging
import requests
from logger_setup import configure_logger
from requests.exceptions import MissingSchema, InvalidURL, InvalidSchema, Timeout
from directory_maker import make_directory


# Initialize logger
logger = logging.getLogger(__name__)
configure_logger(logger)
logger.info("Program started.")

def output_to_file(res):
    """
    This function outputs the content of the response to a file,
    depending on the type of content

    :param res: The given response
    """
    content_type = res.headers["Content-Type"]

    # Create OUT directory
    dir_name = "OUT"
    directory_exists = make_directory(dir_name)
    if not directory_exists:
        logger.info(f"{dir_name} directory created.")

    if "text" in content_type:
        with open(f"./{dir_name}/output.txt", "w") as f:
            f.write(res.text)


def handle_response_code(res):
    """
    This function switches on the response code of the request
    and handles whether it is valid or invalid.

    :param res: The given response.
    :return: True if the response code was successful (200-OK), False otherwise.
    """
    code = res.status_code
    match code:
        case 200:
            output_to_file(res)
            return True
        case 401:
            print("Unauthorized.")
        case 404:
            print("Page not found.")
        case _:
            print("Invalid response code.")
    return False

def main():
    # Initialize variables
    response = ""
    url = ""

    # Continue asking the user for a URL until a valid one is retrieved
    while True:
        try:
            # Ask user to enter URL
            url = input("Please enter the URL you want to fetch data from: ").strip()

            # Check if URL contains schema, if not, default to https
            if "://" not in url:
                url = f"https://{url}"

            # Try to get the URL with a timeout of 10 seconds,
            # will raise exception if it is invalid
            response = requests.get(url, timeout=5)

            # Handle the case where a valid URL is retrieved
            logger.info("Valid URL retrieved.")
            if not handle_response_code(response):
                continue

            # Exit loop if successfully finished
            break

        # Handle exceptions
        except Timeout:
            logger.warning("URL request timed out.")
            print(f"The request for the URL timed out.")
        except (InvalidSchema, MissingSchema):
            logger.warning("User entered a URL with an invalid scheme.")
            print(f"The URL entered has an invalid scheme. It must start with http:// or https://")
        except (InvalidURL,requests.exceptions.ConnectionError):
            logger.warning("User entered an invalid URL.")
            print(f"The URL entered is invalid.")

    logger.info("Program ended.")

if __name__ == "__main__":
    main()
from pathlib import Path

def make_directory(directory):
    """
    This function creates a given directory if it does not already exist.

    :param directory: Given directory
    :return True if directory exists, False otherwise
    """
    p = Path(f"./{directory}/")
    directory_exists = p.exists()
    p.mkdir(exist_ok=True)

    return directory_exists
from pathlib import Path
from typing import List
import mimetypes

def is_text_file(file_path):
    """
    Check if a file is a text file.

    :param file_path: Path to the file.
    :return: True if the file is text, False if it's binary.
    """
    mime = mimetypes.guess_type(file_path)[0]
    if mime is None:
        return False
    return mime.startswith("text")

def filter_code_files(files: List[Path]) -> List[Path]:
    """
    Filter out non-code files from the list of files.

    :param files: List of files to filter.
    :return: List of code files.
    """
    code_files = [f for f in files if is_text_file(f)]
    return code_files

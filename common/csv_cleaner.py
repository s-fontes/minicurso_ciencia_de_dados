import re
import os
import logging

logger = logging.getLogger("common")

PATTERNS = [
    # Internal double quotes → single quote
    (re.compile(r'(?<!^)(?<![\n;])"(?![\n;$])'), "'"),
    # Spaces before and after double quotes → remove
    (re.compile(r'(?<=\")\s+(?=\w)|(?<=\w)\s+(?=\")'), ''),
    # Multiple spaces → single space (excluding newlines)
    (re.compile(r'[^\S\n]+'), ' '),
    # Decimals like "123,45" → "123.45"
    (re.compile(r'(\")(\d+),(\d+)(\")'), r'\1\2.\3\4'),
    # Decimals like ",12" → "0.12"
    (re.compile(r'(\"),(\d+)(\")'), r'\g<1>0.\2\3'),
    # Remove forward slashes and backslashes
    (re.compile(r'([\/])'), '')
]


def clean_csv(file_path: str, source_encoding: str = "latin1", target_encoding: str = "utf-8") -> None:
    logger.info(f"Cleaning CSV file: {file_path}")
    temp_path = file_path + ".tmp"

    try:
        with (
            open(file_path, "r", encoding=source_encoding) as infile,
            open(temp_path, "w", encoding=target_encoding) as tempfile
        ):

            for line in infile.readlines():
                original_line = line
                for pattern, replacement in PATTERNS:
                    line = pattern.sub(replacement, line)

                if logger.isEnabledFor(logging.DEBUG) and original_line != line:
                    logger.debug(f"Original: {original_line.strip()}")
                    logger.debug(f"Cleaned : {line.strip()}")

                tempfile.write(line)

        os.replace(temp_path, file_path)
        logger.info(
            f"CSV file cleaned successfully: {file_path}"
        )

    except Exception:
        logger.exception(f"Error cleaning CSV file: {file_path}")

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
            logger.debug(f"Temporary file removed: {temp_path}")

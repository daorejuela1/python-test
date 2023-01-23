#!/usr/bin/env python3
"""
Normalize csv file
"""
import csv
import argparse
from typing import Optional, Tuple
DEFAULT_DELIMITER = "|"
DEFAULT_QUOTECHAR = '"'


def detect_delimiter_and_quotechar(csv_content: str) -> Tuple[str, str]:
    """
    Detect delimiter and quotechar of the file

    :param csv_first_line: First line of the csv file
    """
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(csv_content)
    return(dialect.delimiter, dialect.quotechar)


def normalize_to_csv(
        file_name: str,
        delimiter: Optional[str] = None,
        quotechar: Optional[str] = None,
) -> None:
    """
    Normalize delimited file to comma delimited file

    :param file_name: Name of the file to normalize

    :param delimiter: Delimiter of the file

    :param quotechar: Quote char of the file
    """
    with open(file_name, "r") as csv_file:
        if not delimiter and not quotechar:
            # Auto detect delimiter and quotechar if both are not provided
            delimiter, quotechar = detect_delimiter_and_quotechar(csv_file.read())
            csv_file.seek(0)
        else:
            # Use provided delimiter and quotechar or default values
            delimiter = delimiter or DEFAULT_DELIMITER
            quotechar = quotechar or DEFAULT_QUOTECHAR
        print(f"Reading file with delimiter: {delimiter} and quotechar: {quotechar}")
        # Read file with provided delimiter and quotechar
        reader = csv.reader(csv_file, delimiter=delimiter, quotechar=quotechar)
        with open(f"normalized_{file_name}", "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=",", quotechar='"')
            for row in reader:
                writer.writerow(row)


if __name__ == "__main__":
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description="Normalize csv file")
    parser.add_argument("file_name", help="Name of the csv file to normalize")
    parser.add_argument("-d", "--delimiter", help="Delimiter of the csv file", default=None)
    parser.add_argument("-q", "--quote-char", help="Quote char of the csv file", default=None)
    args = parser.parse_args()
    normalize_to_csv(args.file_name, args.delimiter, args.quote_char)

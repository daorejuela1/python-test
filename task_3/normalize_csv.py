#!/usr/bin/env python3
"""
Normalize csv file
"""
import argparse
from typing import Optional, Tuple
DEFAULT_DELIMITER = "|"
DEFAULT_QUOTECHAR = '"'
QUOTECHAR_FORBIDDEN_CHARS = ["\n", " ", ",", "-"] # quotechar not allowed characters


def normalize_rules(word: str, quote_character: str) -> str:
    """
    It's valid for a comma to be in your input data. You'll need to surround 
    strings with commas in them with double quotes when writing your output file.

    It's also valid for double quote characters to be in your input - you will 
    need to double up quotes.

    :param word: Word to normalize

    :param quote_character: Quote character of the csv line
    """
    if "," in word or quote_character in word:
        word = word.replace(quote_character, quote_character*2)
        word = f'{quote_character}{word}{quote_character}'
    return word


def _split_csv_line(csv_line: str, delimiter: str) -> list:
    """
    Split csv line by delimiter and apply rules for quotes and commas

    :param csv_line: CSV line to split

    :param delimiter: Delimiter of the csv line

    :param quotechar: Quote char of the csv line
    """
    # split csv words by delimiter and apply rules for quotes and commas
    start = 0
    end = 0
    words_list = []
    for index, char in enumerate(csv_line):
        if char == delimiter:
            end = index
            words_list.append(csv_line[start:end])
            start = index + 1
        elif index == len(csv_line) - 1:
            words_list.append(csv_line[start:])
    return words_list


def csv_normalizer(csv_data: str, delimiter: str, quotechar: str) -> str:
    """
    Normalize csv data

    :param csv_data: CSV data to normalize

    :param delimiter: Delimiter of the csv data

    :param quotechar: Quote char of the csv data
    """
    # split csv words by delimiter and apply rules for quotes and commas
    words_list = _split_csv_line(csv_data, delimiter)
    words_list = [normalize_rules(word, quotechar) for word in words_list]
    return ",".join(words_list)+"\n"


def detect_delimiter_and_quotechar(csv_content: str) -> Tuple[str, str]:
    """
    Detect delimiter and quotechar of the file

    :param csv_first_line: First line of the csv file

    Returns:
        Tuple[str, str]: Delimiter and quotechar
    """
    csv_lines = csv_content.split('\n')
    char_frequency = [dict() for _ in range(len(csv_lines))]
    for line, content in enumerate(csv_lines):
        for char in content:
            if char not in char_frequency[line]:
                char_frequency[line][char] = 1
            else:
                char_frequency[line][char] += 1
    # get delimiter from char_frequency if frequency is same for all lines
    delimiter, frequency = DEFAULT_DELIMITER, 0
    headers_dict = char_frequency[0].items()
    for header_key, header_frequency in headers_dict:
        data = [
                [True for key, value in line.items() if key == header_key and value == header_frequency]
                for line in char_frequency[1:]
            ]
        data_in_all_lines = [x for x in data if x]
        # if there is data in all lines pick the delimiter with highest frequency
        if len(data_in_all_lines) == len(csv_lines) - 1:
            if header_frequency > frequency:
                delimiter, frequency = header_key, header_frequency

    # get quotechar from csv_data if appears near delimiter else use default
    quotechar = DEFAULT_QUOTECHAR
    possible_quote_frequency = [
        [char for char in word if not char.isalnum() and not char in QUOTECHAR_FORBIDDEN_CHARS]
         for word in csv_content.split(delimiter)
    ]
    possible_quote_frequency = [ x for x in possible_quote_frequency if x]
    if possible_quote_frequency:
        quotechar = max(possible_quote_frequency, key=possible_quote_frequency.count)[0]

    return (delimiter, quotechar)


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
        normalized_data = csv_normalizer(csv_file.read(), delimiter=delimiter, quotechar=quotechar)
    with open(f"normalized_{file_name.split('/')[-1]}", "w") as csv_file:
        csv_file.write(normalized_data)


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

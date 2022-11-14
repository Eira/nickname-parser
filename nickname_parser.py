"""
This is module for parse @nickname from the .txt file.

To start the script you should write in terminal:
```python -X utf8 nickname_parser.py input.txt output.txt```
where:
```input.txt``` - path to the source file
```output.txt``` - path to the file, where you want see the results
"""
import argparse
import logging
import re
from typing import List


def get_file_content(input_file_address: str) -> str:
    """Get all text from the .txt file. Return string with all text."""
    with open(input_file_address) as text:
        text_str = text.read()

    return text_str


def parse_nickname(text_str: str) -> List[str]:
    """Get string with all text. Return list of nicknames."""
    nickname_pattern = r'@[.\w]+'

    return re.findall(nickname_pattern, text_str)


def save_nicknames(nickname_list: List[str], output_file_address: str) -> None:
    """Get list of all nicknames. Return a file with nicknames."""
    with open(output_file_address, 'w') as fd:
        for nickname in nickname_list:
            fd.write('{0}\n'.format(nickname))


def main(input_file_path: str, output_file_path: str) -> None:
    """
    Do the main runner of nickname parser.

    Get all nicknames from the clients file.
    Save it to the txt file.
    """
    try:
        file_content = get_file_content(input_file_path)
    except FileNotFoundError:
        logging.warning(f'Sorry, the file {input_file_path} does not exist.')
        return

    nickname_list = parse_nickname(file_content)
    if nickname_list:
        try:
            save_nicknames(nickname_list, output_file_path)
        except FileNotFoundError:
            logging.warning(f'Sorry, there no such directory: {output_file_path}.')
            return
        logging.info('Your file is ready!')

    else:
        logging.info('No nicknames was found.')


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',
    )
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file_path', help='Path of file you need to parse.')
    parser.add_argument('output_file_path', help='Path of file with the results.')
    args = parser.parse_args()

    main(args.input_file_path, args.output_file_path)

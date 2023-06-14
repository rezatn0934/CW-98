from typing import List
from contextlib import contextmanager


def process_data(input_str: str) -> List[str]:
    output_data = input_str.split(".")
    return output_data


@contextmanager
def file_opener(fil_path: str, mode: str) -> any:
    try:
        file = open(fil_path, mode)
        yield file
    finally:
        file.close()


input_file_path = "input.txt"
output_file_path = "output.txt"

with file_opener(fil_path=input_file_path, mode='r') as input_file:
    input_data = input_file.readlines()
    output_data = []
    for line in input_data:
        processed = process_data(line)
        for index in range(len(processed)):
            output_data.append(processed[index])

with file_opener(fil_path=output_file_path, mode='w') as output_file:
    for s in output_data:
        output_file.write(s.strip())
        if "\n" not in s:
            output_file.write('\n')


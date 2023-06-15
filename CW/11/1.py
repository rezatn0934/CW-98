import sys
import os


def read_file(file_name, mod):
    with open(file_name, mod) as file:
        content = file.read()
    return content



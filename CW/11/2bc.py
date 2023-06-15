import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('-p', "--path")
parser.add_argument('-s', "--size")
arg = parser.parse_args()

if arg.size:
    for entry in os.listdir(arg.size):
        if os.path.isfile(entry):
            entry_size = os.path.getsize(entry)
            print(f"{entry}, (Size: {entry_size} KB)")
        else:
            print(entry)
else:
    for entry in os.listdir(arg.path):
        print(entry)




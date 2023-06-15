import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', "--number", nargs="+", type=int, required=True)
args = parser.parse_args()
print("Sum : ", sum(args.n))

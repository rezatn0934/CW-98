import sys
import os


def read_file(file_name, mod):
    with open(file_name, mod) as file:
        content = file.read()
    return content


if len(sys.argv) == 1:
    print("Hello word")
elif os.path.exists(sys.argv[1]):
    string = read_file(sys.argv[1], mod= "r")
    lst1 = string.split()
    dic1 = dict()
    for word in lst1:
        dic1[word] = dic1.get(word, 0) + 1
    print(dic1)
else:
    print(sys.argv[1][::-1])



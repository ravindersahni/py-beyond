__author__ = 'instancetype'

import sys


def read_upto(file, end):
    with open(file, 'rt') as f:
        for line in iter(lambda: f.readline().strip(), end):
            print(line)

if __name__ == '__main__':
    read_upto(sys.argv[1], sys.argv[2])
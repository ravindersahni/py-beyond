__author__ = 'instancetype'


def hypervolume(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v
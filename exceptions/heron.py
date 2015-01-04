__author__ = 'instancetype'

import math


class TriangleError(Exception):
    pass


def triangle_area(a, b, c):
    sides = sorted((a, b ,c))
    if sides[2] > sides[0] + sides[1]:
        raise TriangleError('Illegal triangle')

    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p- b) * (p - c))

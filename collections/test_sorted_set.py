__author__ = 'instancetype'


import unittest

from sorted_set import SortedSet


class TestConstruction(unittest.TestCase):

    def test_empty(self):
        s = SortedSet([])

    def test_from_sequence(self):
        s = SortedSet([4, 5, 3, 2])

    def test_with_duplicates(self):
        s = SortedSet([5, 5, 5,])

    def test_from_iterable(self):
        def gen4621():
            yield 4
            yield 6
            yield 2
            yield 1

        g = gen4621()
        s = SortedSet(g)

    def test_default_empty(self):
        s = SortedSet()
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


class TestContainerProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([5, 6, 2, 8])

    def test_positive_contained(self):
        self.assertTrue(5 in self.s)

    def test_negative_contained(self):
        self.assertFalse(7 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(9 not in self.s)

    def test_negative_not_contained(self):
        self.assertFalse(2 not in self.s)


class TestSizedProtocol(unittest.TestCase):

    def test_empty(self):
        s = SortedSet()
        self.assertEqual(len(s), 0)

    def test_one(self):
        s = SortedSet([87])
        self.assertEqual(len(s), 1)

    def test_ten(self):
        s = SortedSet(range(10))
        self.assertEqual(len(s), 10)

    def test_with_duplicates(self):
        s = SortedSet([1, 1, 1])
        self.assertEqual(len(s), 1)


class TestIterableProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([5, 3, 1, 1, 7])

    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i), 1)
        self.assertEqual(next(i), 3)
        self.assertEqual(next(i), 5)
        self.assertEqual(next(i), 7)
        self.assertRaises(StopIteration, lambda: next(i))

    def test_for_loop(self):
        index = 0
        expected = [1, 3, 5, 7]
        for item in self.s:
            self.assertEqual(item, expected[index])
            index += 1
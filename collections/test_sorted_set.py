__author__ = 'instancetype'


import unittest
from collections.abc import Container, Sized, Iterable, Sequence

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

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Container))


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

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Sized))


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

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Iterable))

class TestSequenceProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([1, 4, 9, 13, 15])

    def test_index_zero(self):
        self.assertEqual(self.s[0], 1)

    def test_index_four(self):
        self.assertEqual(self.s[4], 15)

    def test_index_one_beyond_last(self):
        with self.assertRaises(IndexError):
            self.s[5]

    def test_index_minus_one(self):
        self.assertEqual(self.s[-1], 15)

    def test_index_minus_five(self):
        self.assertEqual(self.s[-5], 1)

    def test_index_one_before_beginning(self):
        with self.assertRaises(IndexError):
            self.s[-6]

    def test_slice_from_start(self):
        self.assertEqual(self.s[:3], SortedSet([1, 4, 9]))

    def test_slice_to_end(self):
        self.assertEqual(self.s[3:], SortedSet([13, 15]))

    def test_slice_empty(self):
        self.assertEqual(self.s[10:], SortedSet())

    def test_slice_arbitrary(self):
        self.assertEqual(self.s[2:4], SortedSet([9, 13]))

    def test_slice_full(self):
        self.assertEqual(self.s[:], self.s)

    def test_reversed(self):
        s = SortedSet([2, 4, 6, 8])
        r = reversed(s)
        self.assertEqual(next(r), 8)
        self.assertEqual(next(r), 6)
        self.assertEqual(next(r), 4)
        self.assertEqual(next(r), 2)
        with self.assertRaises(StopIteration):
            next(r)

    def test_index_positive(self):
        s = SortedSet([1, 3, 5, 7])
        self.assertEqual(s.index(3), 1)

    def test_index_negative(self):
        s = SortedSet([1, 3, 5, 7])
        with self.assertRaises(ValueError):
            s.index(50)

    def test_count_one(self):
        s = SortedSet([1, 2, 3])
        self.assertEqual(s.count(3), 1)

    def test_count_zero(self):
        s = SortedSet([1, 2, 3])
        self.assertEqual(s.count(5), 0)

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Sequence))

    def test_concatenate_disjoint(self):
        s = SortedSet([1, 2, 3])
        t = SortedSet([4, 5, 6])
        self.assertEqual(s + t, SortedSet([1, 2, 3, 4, 5, 6]))

    def test_concatenate_equal(self):
        s = SortedSet([1, 2, 3])
        self.assertEqual(s + s, s)

    def test_concatenate_intersecting(self):
        s = SortedSet([1, 2, 3, 4])
        t = SortedSet([3, 4, 5, 6])
        self.assertEqual(s + t, SortedSet([1, 2, 3, 4, 5, 6]))

    def test_repetition_zero(self):
        s = SortedSet([1, 2, 3])
        self.assertEqual(0 * s, SortedSet())

    def test_repetition_nonzero(self):
        s = SortedSet([2, 3, 4])
        self.assertEqual(100 * s, s)

class TestReprProtocol(unittest.TestCase):

    def test_repr_empty(self):
        s = SortedSet()
        self.assertEqual(repr(s), "SortedSet()")

    def test_repr_some(self):
        s = SortedSet([42, 40, 19])
        self.assertEqual(repr(s), "SortedSet([19, 40, 42])")


class TestEqualityProtocol(unittest.TestCase):

    def test_positive_equal(self):
        self.assertTrue(SortedSet([2, 3, 4]) == SortedSet([2, 3, 4]))

    def test_negative_equal(self):
        self.assertFalse(SortedSet([1, 2, 3]) == SortedSet([4, 5, 6]))

    def test_type_mismatch(self):
        self.assertFalse(SortedSet([1, 2, 3]) == [1, 2, 3])

    def test_identical(self):
        s = SortedSet([2, 4, 6])
        self.assertTrue(s == s)


class TestInequalityProtocol:

    def test_positive_unequal(self):
        self.assertTrue(SortedSet([2, 3, 4]) != SortedSet([3, 4, 5]))

    def test_negative_unequal(self):
        self.assertFalse(SortedSet([1, 2, 3]) != SortedSet([1, 2, 3]))

    def test_type_mismatch(self):
        self.assertTrue(SortedSet([1, 2, 3]) != [1, 2, 3])

    def test_identical(self):
        s = SortedSet([2, 4, 6])
        self.assertFalse(s != s)


class TestRelationalSetProtocol(unittest.TestCase):

    def test_lt_positive(self):
        s = SortedSet({1, 2})
        t = SortedSet({1, 2, 3})
        self.assertTrue(s < t)

    def test_lt_negative(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({1, 2, 3})
        self.assertFalse(s < t)

    def test_lte_positive(self):
        s = SortedSet({1, 2})
        r = SortedSet({1, 2, 3})
        t = SortedSet({1, 2, 3})
        self.assertTrue(s <= t)
        self.assertTrue(r <= t)

    def test_lte_negative(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({1, 2})
        self.assertTrue(s <= t)

    def test_gt_positive(self):
        s = SortedSet({1, 2, 3})
        t = SortedSet({1, 2})
        self.assertTrue(s > t)

    def test_gt_negative(self):
        s = SortedSet({1, 2})
        t = SortedSet({1, 2, 3})
        self.assertFalse(s > t)

    def test_gte_positive(self):
        s = SortedSet({1, 2, 3})
        r = SortedSet({1, 2})
        t = SortedSet({1, 2})
        self.assertTrue(s >= t)
        self.assertTrue(r >= t)

    def test_gte_negative(self):
        s = SortedSet({1, 2})
        t = SortedSet({1, 2, 3})
        self.assertFalse(s >= t)
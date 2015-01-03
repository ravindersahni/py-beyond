__author__ = 'instancetype'


from bisect import bisect_left
from collections.abc import Sequence


class SortedSet(Sequence):
    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        return item in self._items

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __repr__(self):
        return 'SortedSet({})'.format(
            repr(self._items) if self._items else ''
        )

    def __eq__(self, other):
        if not isinstance(other, SortedSet):
            return NotImplemented
        return self._items == other._items

    def __ne__(self, other):
        if not isinstance(other, SortedSet):
            return NotImplemented
        return self._items != other._items

    def count(self, value):
        index = bisect_left(self._items, value)
        found = (index != len(self._items)) and (self._items[index] == value)
        return int(found)
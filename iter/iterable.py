__author__ = 'instancetype'


class AnIterator:

    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration()

        next = self.data[self.index]
        self.index += 1
        return next


class AnIterable:

    def __init__(self):
        self.data = [1, 2, 3]

    def __iter__(self):
        return AnIterator(self.data)
__author__ = 'instancetype'


class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Point2D(x={}, y={})'.format(self.x, self.y)

    def __format__(self, format_spec):
        return '[formatted point: {}, {}, {}]'.format(self.x, self.y, format_spec)
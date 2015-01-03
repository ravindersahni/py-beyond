__author__ = 'instancetype'


class Base:

    def __init__(self):
        print('Base initializer')

    def fn(self):
        print('Base.fn()')


class Sub(Base):
    def __init__(self):
        print('Sub initializer')

    def fn(self):
        print('Sub.fn()')
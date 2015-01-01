__author__ = 'instancetype'

class CallCounter:
    def __init__(self, fn):
        self.fn = fn
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.fn(*args, **kwargs)


@CallCounter
def greet(name):
    print('Howdy, {}'.format(name))

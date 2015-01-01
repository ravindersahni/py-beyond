__author__ = 'instancetype'

import functools

def noop(fn):
    def wrapper():
        return fn()

    wrapper.__name__ = fn.__name__
    wrapper.__doc__ = fn.__doc__
    return wrapper

@noop
def hi():
    """Greet the world from stdout."""
    print('Hello, world.')

def cool_noop(fn):
    @functools.wraps(fn)
    def wrapper():
        return fn()
    return wrapper

@cool_noop
def hello():
    """Greet the world from stdout."""
    print('Power to the people.')
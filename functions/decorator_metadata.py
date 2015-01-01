__author__ = 'instancetype'

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
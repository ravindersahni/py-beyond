__author__ = 'instancetype'

def ensure_non_negative(*indices):
    def validator(fn):
        def wrap(*args):
            for index in indices:
                if args[index] < 0:
                    raise ValueError(
                        'Argument {} must be non-negative.'.format(index))
            return fn(*args)
        return wrap
    return validator

@ensure_non_negative(0, 1)
def area_of_triangle(b, h):
    return (b * h) / 2

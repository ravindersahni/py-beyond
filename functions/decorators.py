__author__ = 'instancetype'

def escape_unicode(fn):
    def wrap(*args, **kwargs):
        x = fn(*args, **kwargs)
        return ascii(x)

    return wrap


@escape_unicode
def fancy():
    return 'résumé'
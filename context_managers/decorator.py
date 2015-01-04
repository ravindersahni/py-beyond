__author__ = 'instancetype'

import sys
import contextlib


@contextlib.contextmanager
def logging_context_manager():
    print('logging_context_manager: Enter')

    try:
        yield 'Inside the with-block...'
        print('logging_context_manager: Normal Exit')
    except Exception:
        print('logging_context_manager: Exceptional Exit', sys.exc_info())
        raise


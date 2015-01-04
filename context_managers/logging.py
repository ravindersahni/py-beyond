__author__ = 'instancetype'


class LoggingContextManager:
    def __enter__(self):
        print('LoggingContextManager.__enter__()')
        return 'Inside the width-block...'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('LoggingContextManager.__exit__({}, {}, {})'.format(
            exc_type, exc_val, exc_tb
        ))
        return
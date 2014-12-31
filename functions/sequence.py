__author__ = 'instancetype'

def sequence_class(immutable):
    return tuple if immutable else list
__author__ = 'instancetype'

class AltIterable:

    def __init__(self):
        self.data = ['red', 'yellow', 'green']

    def __getitem__(self, idx):
        return self.data[idx]
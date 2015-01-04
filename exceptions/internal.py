__author__ = 'instancetype'


def modulus_three(n):
    r = n % 3
    if r == 0:
        print('Multiple of 3')
    elif r == 1:
        print('Remainder 1')
    else:
        assert r == 2, 'Remainder is not 2'
        print('Remainder 2')




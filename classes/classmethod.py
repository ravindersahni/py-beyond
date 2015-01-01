__author__ = 'instancetype'


class ShippingContainer:

    next_serial = 0

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty_container(cls, owner_code):
        return cls(owner_code, contents=None)

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial()

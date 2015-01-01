__author__ = 'instancetype'

import iso6346


class ShippingContainer:

    next_serial = 0

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6))

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty_container(cls, owner_code, *args, **kwargs):
        return cls(owner_code, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, *args, **kwargs):
        return cls(owner_code, contents=list(items), *args, **kwargs)

    def __init__(self, owner_code, contents):
        self.contents = contents
        self.bic = self._make_bic_code( # must use self for polymorphic dispatch
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial())


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6),
                              category='R')

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError('Temperature is too hot.')
        self.celsius = celsius
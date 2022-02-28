from classes.product import Product


class Clothes(Product):
    pay_rate = 1 #default

    def __init__(self, name: str, brand: str, price: float, size: str, color: str):
        
        assert size in ["XS", "S", "M", "L", "XL"], f"Wrong size: {size}"

        super().__init__(
            name, brand, price
        )

        self.__size = size
        self.__color = color


    @property
    def size(self):
        return self.__size

    @property
    def color(self):
        return self.__color


    def is_discount(self, date_of_purchase):
        tuesday_to_saturday = [2, 3, 4, 5, 6]
        # 1 - Monday
        # 7 - Sunday

        if date_of_purchase.isoweekday() in tuesday_to_saturday:
            return True

        return False


    def apply_discount(self):
        self.price *= 0.9 #discount = 10%
        self.pay_rate = 0.9
            
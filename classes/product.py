class Product:
    
    def __init__(self, name: str, brand: str, price: float):
        
        assert price >= 0, f"Price should not be negative: {price}$"

        self.__name = name
        self.__brand = brand
        self.__price = price


    @property
    def name(self):
        return self.__name

    @property
    def brand(self):
        return self.__brand

    @property
    def price(self):
        return self.__price
        
    @price.setter
    def price(self, value):
        self.__price = value


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name} {self.name} {self.price}')"

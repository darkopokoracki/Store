from classes.product import Product
import datetime


class Appliance(Product):
    pay_rate = 1 #default

    def __init__(self, name: str, brand: str, price: float, model: str, production_date: datetime.date, weight: float):

        assert weight > 0, f"weight should not be negative: {weight}$"

        super().__init__(
            name, brand, price
        )

        self.__model = model
        self.__production_date = production_date
        self.__weight = weight


    @property
    def model(self):
        return self.__model

    @property
    def production_date(self):
        return self.__production_date

    @property
    def weight(self):
        return self.__weight

    
    def is_discount(self, date_of_purchase):
        weekdays = [6, 7]
        # 6 - Saturday
        # 7 - Sunday

        if date_of_purchase.isoweekday() in weekdays and self.price > 999:
            return True

        return False


    def apply_discount(self):
        self.price *= 0.93 #Discount = 7%
        self.pay_rate = 0.93


            
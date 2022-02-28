from classes.product import Product
import datetime


class Beverage(Product):
    pay_rate = 1 #default

    def __init__(self, name: str, brand: str, price: float, expiration_date: datetime.date):
        super().__init__(
            name, brand, price
        )

        self.__expiration_date = expiration_date


    @property
    def expiration_date(self):
        return self.__expiration_date


    def is_discount(self, date_of_purchase):
        time_delta = datetime.timedelta(days = 5)
        discount_period = self.expiration_date - time_delta

        if date_of_purchase >= discount_period:
            return True

        return False


    def apply_discount(self, date_of_purchase):
        time_delta = datetime.timedelta(days = 5)
        discount_period = self.expiration_date - time_delta

        if date_of_purchase >= discount_period and date_of_purchase < self.expiration_date:
            self.price *= 0.7 #discount = 30%
            self.pay_rate = 0.7
            
        elif date_of_purchase == self.expiration_date:
            self.price *= 0.3 #discount = 70%
            self.pay_rate = 0.3

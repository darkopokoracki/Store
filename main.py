from classes.cashier import Cashier
from classes.food import Food
from classes.beverage import Beverage
from classes.clothes import Clothes
from classes.appliance import Appliance

import datetime


product1 = Food('apples', 'BrandA', 1.50, datetime.date(2021, 6, 14))
product2 = Beverage('milk', 'BrandM', 0.99, datetime.date(2022, 2, 2))
product3 = Clothes('T-shirt', 'BrandT', 15.99, 'M', 'violet')
product4 = Appliance('laptop', 'BrandL', 2345, 'ModelL', datetime.date(2021, 3, 3), 1.125)

cart = [
    #[product, quantity]
    [product1, 2.45],
    [product2, 3],
    [product3, 2],
    [product4, 1]
]

#                                         year mon day ho  min sec
purchase = Cashier(cart, datetime.datetime(2021, 6, 14, 12, 34, 56))
print(purchase)


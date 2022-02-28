class Cashier:
    def __init__(self, cart: list, date_and_time: str):

        assert len(cart) > 0, f"Empty cart: {cart}"

        self.__cart = cart
        self.__date_and_time = date_and_time


    @property
    def cart(self):
        return self.__cart

    @property
    def date_and_time(self):
        return self.__date_and_time


    @staticmethod
    def __calculate_subtotal(cart):
        subtotal = 0

        for i in range(len(cart)):
            subtotal += cart[i][0].price * cart[i][1]

        return subtotal


        #__ = Like private access modifier in C#, Java ...
    def __create_receipt(self, cart):
        date = self.date_and_time.date()
        time = self.date_and_time.time()

        subtotal = self.__calculate_subtotal(self.cart)

        receipt = f"Date: {date} {time}\n\n"
        receipt += f"---Products---"

        total_discount = 0

        # display products
        for i in range(len(cart)):
            receipt += f"\n\n\n{cart[i][0].name} {cart[i][0].brand}\n\n"
            receipt += f"{cart[i][1]} x ${cart[i][0].price} = "
            receipt += f"${round(cart[i][1] * cart[i][0].price, 2)}\n\n"
            
            old_price = cart[i][0].price

            # display discount
            if cart[i][0].is_discount(date) == True:
                cart[i][0].apply_discount(date)
                new_price = cart[i][0].price

                receipt += f"#discount {round((1 - cart[i][0].pay_rate) * 100)}% "
                receipt += f"-${round((old_price - new_price) * cart[i][1], 2)}\n"
                total_discount += round(old_price - new_price, 2) * cart[i][1]


        receipt += "\n-----------------------------------\n\n"

        receipt += f"SUBTOTAL: ${subtotal}\n"
        receipt += f"DISCOUNT: -${round(total_discount, 2)} \n\n"
        receipt += f"TOTAL: ${subtotal - total_discount}"

        return receipt


    def __str__(self):
        return self.__create_receipt(self.cart)

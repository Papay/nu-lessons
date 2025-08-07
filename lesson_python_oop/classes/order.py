from lesson_python_oop.classes.discount import Discount


class Order:
    """
    Класс Order
    Этот класс представляет заказ в интернет-магазине.
    """

    _total_orders = 0
    _total_price = 0

    def __init__(self, products, discount: Discount):
        self.products = products
        self.discount = discount
        Order._total_orders += 1
        Order._total_price += self.calculate_price()

    @classmethod
    def total_orders(cls):
        return cls._total_orders

    @classmethod
    def total_price(cls):
        return cls._total_price

    def calculate_price(self):
        return sum(Discount.calculate_price(product.price, self.discount.discount_percent) for product in self.products)

    def __str__(self):
        return f"Заказ (Общая цена = {self.calculate_price()}, Скидка = {self.discount})"
    
    def __repr__(self):
        return f"Order (products={self.products}, discount={repr(self.discount)}"

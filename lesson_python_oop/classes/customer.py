class Customer:
    """
    Класс Customer
    Этот класс представляет клиента интернет-магазина.
    """

    def __init__(self, name: str):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f"Клиент (Имя={self.name}, Заказы: {self.orders})"

    def __repr__(self):
        return f"Customer(name='{self.name}, orders={self.orders})')"

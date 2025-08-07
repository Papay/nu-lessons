class Product:
    """
    Класс Product
    Этот класс представляет товар в интернет-магазине.
    """

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Продукт (Название={self.name}, Цена={self.price})"

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"

    def __eq__(self, other): return self.price == other.price
    def __ne__(self, other): return not (self == other)

    def __gt__(self, other): return self.price > other.price
    def __le__(self, other): return not (self > other)

    def __lt__(self, other): return self.price < other.price
    def __ge__(self, other): return not (self < other)

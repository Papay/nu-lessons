class Discount:
    """
    Класс Discount
    Этот класс представляет скидку в интернет-магазине.
    """

    def __init__(self, description: str, discount_percent: float):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def calculate_price(price: float, discount):
        return price * (1 - discount / 100)

    def __str__(self):
        return f"Скидка ({self.description}, Размер = {self.discount_percent}%)"

    def __repr__(self):
        return f"Discount(description='{self.description}', discount_percent={self.discount_percent})"

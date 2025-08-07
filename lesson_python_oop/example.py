# Пример использования статических методов и методов класса в интернет-магазине
# Предположим, у нас есть интернет-магазин с классом Product, который представляет товар, и классом Order, который представляет заказ. 
# Мы будем использовать статические методы для расчета скидок и методы класса для подсчета общего количества заказов.
from classes.order import Order
from classes.product import Product
from classes.discount import Discount
from classes.customer import Customer

customer1 = Customer("Dima")
customer2 = Customer("Ira")

# Создаем продукты
product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 400)
product3 = Product("Book", 20)
product4 = Product("Pencil", 5)

# Выводим информацию о товарах
print("Продукты:")
print(product1)
print(product2)
print(product3)
print(product4)
print()

discount1 = Discount("Promo", 10)
discount2 = Discount("Season", 20)

# Создаем заказы
order1 = Order([product1, product3], discount1)
customer1.add_order(order1)

order2 = Order([product2, product4], discount2)
customer2.add_order(order2)

# Выводим информацию о заказах
print("Заказы:")
print(order1)
print(order2)
print()

# Выводим общее количество заказов
print(f"Всего заказов: {Order.total_orders()}")  # Вывод: Всего заказов: 2
print(f"Общая сумма заказов: {Order.total_price()}")  # Вывод: Всего заказов: 2
print()

# Выводим информацию о покупателях
print("Покупатели:")
print(f"Покупатель: {customer1}")
print(f"Покупатель: {customer2}")
print()
import sqlite3

# 1. Создать базу данных и подключиться к ней
connection = sqlite3.connect("hw.db")
cursor = connection.cursor()

# 2-6. Создать таблицу products
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT NOT NULL,
    price REAL NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
""")
connection.commit()


# 7. Добавить 15 товаров
def add_products():
    products = [
        ("Нан 1", 50.0, 10), (" 2", 20.0, 5), ("Чай 3", 150.0, 2),
        ("Эт 4", 75.0, 7), ("Банан 5", 30.0, 12), ("Вода 6", 200.0, 3),
        ("Туз 7", 10.0, 20), ("Арбуз 8", 60.0, 8), ("Сумка 9", 5.0, 15),
        ("Сода 10", 80.0, 4), ("Лимон 11", 120.0, 9), ("Шапка 12", 15.0, 6),
        ("Сыр 13", 90.0, 3), ("Кофе 14", 25.0, 10), ("Бумага 15", 70.0, 11)
    ]
    cursor.executemany("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", products)
    connection.commit()


# 8. Изменить количество товара по id
def update_quantity(product_id, new_quantity):
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    connection.commit()


# 9. Изменить цену товара по id
def update_price(product_id, new_price):
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    connection.commit()


# 10. Удалить товар по id
def delete_product(product_id):
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    connection.commit()


# 11. Вывести все товары
def print_all_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    for product in products:
        print(product)


# 12. Выбрать товары дешевле лимита и с количеством больше указанного
def filter_products(price_limit, quantity_limit):
    cursor.execute("SELECT * FROM products WHERE price < ? AND quantity > ?", (price_limit, quantity_limit))
    products = cursor.fetchall()
    for product in products:
        print(product)


# 13. Искать товары по названию
def search_products(keyword):
    cursor.execute("SELECT * FROM products WHERE product_title LIKE ?", (f"%{keyword}%",))
    products = cursor.fetchall()
    for product in products:
        print(product)


# Тестирование
if __name__ == "__main__":
    add_products()
    print("Все товары:")
    print_all_products()

    print("\nИзменить количество товара с id=1:")
    update_quantity(1, 50)
    print_all_products()

    print("\nИзменить цену товара с id=2:")
    update_price(2, 99.99)
    print_all_products()

    print("\nУдалить товар с id=3:")
    delete_product(3)
    print_all_products()

    print("\nТовары дешевле 100 сом и с количеством больше 5:")
    filter_products(100, 5)

    print("\nПоиск товаров с названием 'Товар 1':")
    search_products("Товар 1")

# Закрыть соединение
connection.close()
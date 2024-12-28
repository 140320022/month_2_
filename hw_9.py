import sqlite3

def initialize_database():
    """Initialize the database with sample data."""
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            code TEXT PRIMARY KEY,
            title TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stores (
            store_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            category_code TEXT NOT NULL,
            unit_price REAL NOT NULL,
            stock_quantity INTEGER NOT NULL,
            store_id INTEGER NOT NULL,
            FOREIGN KEY (category_code) REFERENCES categories (code),
            FOREIGN KEY (store_id) REFERENCES stores (store_id)
        )
    ''')

    # Insert sample data
    cursor.executemany('''INSERT OR IGNORE INTO categories (code, title) VALUES (?, ?)''', [
        ('FD', 'Food products'),
        ('EL', 'Electronics'),
        ('CL', 'Clothing')
    ])

    cursor.executemany('''INSERT OR IGNORE INTO stores (store_id, title) VALUES (?, ?)''', [
        (1, 'Asia'),
        (2, 'Globus'),
        (3, 'Spar')
    ])

    cursor.executemany('''INSERT OR IGNORE INTO products (id, title, category_code, unit_price, stock_quantity, store_id) VALUES (?, ?, ?, ?, ?, ?)''', [
        (1, 'Chocolate', 'FD', 10.5, 129, 1),
        (2, 'Laptop', 'EL', 899.99, 35, 2),
        (3, 'T-Shirt', 'CL', 15.99, 200, 3),
        (4, 'Bread', 'FD', 2.5, 50, 1)
    ])

    conn.commit()
    conn.close()

def display_products(store_id):
    """Display products for the given store ID."""
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT p.title, c.title, p.unit_price, p.stock_quantity
        FROM products p
        JOIN categories c ON p.category_code = c.code
        WHERE p.store_id = ?
    ''', (store_id,))

    products = cursor.fetchall()
    conn.close()

    if not products:
        print("\nNo products found for the selected store.\n")
    else:
        for product in products:
            print(f"\nНазвание продукта: {product[0]}\nКатегория: {product[1]}\nЦена: {product[2]}\nКоличество на складе: {product[3]}\n")

def main():
    """Main program loop."""
    initialize_database()

    while True:
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()

        cursor.execute('SELECT store_id, title FROM stores')
        stores = cursor.fetchall()
        conn.close()

        print("\nВы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
        for store in stores:
            print(f"{store[0]}. {store[1]}")

        try:
            user_input = int(input("\nВведите ID магазина: "))
        except ValueError:
            print("\nПожалуйста, введите корректное число.\n")
            continue

        if user_input == 0:
            print("\nВыход из программы. До свидания!\n")
            break

        if any(store[0] == user_input for store in stores):
            display_products(user_input)
        else:
            print("\nМагазин с таким ID не найден. Пожалуйста, попробуйте снова.\n")

if __name__ == '__main__':
    main()

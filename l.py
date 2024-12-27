def initialize_db():
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    # Создаем таблицы, если они не существуют
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            area REAL DEFAULT 0,
            country_id INTEGER NOT NULL,
            FOREIGN KEY (country_id) REFERENCES countries(id)
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            city_id INTEGER NOT NULL,
            FOREIGN KEY (city_id) REFERENCES cities(id)
        );
    """)
    conn.commit()
    conn.close()

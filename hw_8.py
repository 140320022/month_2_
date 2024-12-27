import sqlite3

def connect_db():
    return sqlite3.connect("hw.db")

def display_cities(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    for city in cities:
        print(f"{city[0]}. {city[1]}")

def display_students(conn, city_id):
    cursor = conn.cursor()
    query = """
        SELECT s.first_name, s.last_name, c.title, co.title, c.area
        FROM students s
        JOIN cities c ON s.city_id = c.id
        JOIN countries co ON c.country_id = co.id
        WHERE c.id = ?
    """
    cursor.execute(query, (city_id,))
    students = cursor.fetchall()
    if students:
        print("Ученики в выбранном городе:")
        for student in students:
            print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[3]}, Город: {student[2]}, Площадь города: {student[4]} км²")
    else:
        print("В этом городе нет учеников.")

def main():
    conn = connect_db()
    while True:
        display_cities(conn)
        try:
            city_id = int(input("Введите ID города: "))
            if city_id == 0:
                print("Выход из программы.")
                break
            display_students(conn, city_id)
        except ValueError:
            print("Пожалуйста, введите корректный номер ID.")

if __name__ == "__main__":
    main()
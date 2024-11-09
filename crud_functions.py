import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    photo_path TEXT,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()


def get_all_products():
    return cursor.execute("SELECT * FROM Products").fetchall()


if __name__ == "__main__":
    initiate_db()
    # for i in range(1, 5):
    #     cursor.execute("INSERT INTO Products (title, description, photo_path, price) VALUES (?, ?, ?, ?)",
    #                    (f"Product{i}", f"Описание продукта{i}. Бла-бла-бла", f"files/{i}.png", str(i*100)))
    # print(get_all_products())

    connection.commit()
    connection.close()


import sqlite3

def initiate_db():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Product(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    img_name TEXT
    )    
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )    
    ''')
    connection.commit()
    connection.close()


def set_product(title,description,price,img_name):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Product (title,description,price, img_name) VALUES (?,?,?,?)",
                   (f'{title}', f'{description}', f'{price}',f'{img_name}'))
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Product")
    total = cursor.fetchall()
    connection.commit()
    connection.close()
    return total


def add_user(username, email, age):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username,email,age,balance) VALUES (?,?,?,?)",
                   (f'{username}', f'{email}', f'{age}',1000))
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    check_user=cursor.execute("SELECT * FROM Users WHERE username=?",(f'{username}',))
    if check_user.fetchone() is None:
        connection.commit()
        connection.close()
        return True
    connection.commit()
    connection.close()
    return False

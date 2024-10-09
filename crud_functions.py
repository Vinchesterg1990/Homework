import sqlite3

def initiate_db():
    connection = sqlite3.connect('initiate.bd')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Products
                 (id INTEGER PRIMARY KEY, 
                 title TEXT NOT NULL, 
                 description TEXT NOT NULL, 
                 price INTEGER NOT NULL)''')
    cursor.execute('DELETE FROM Products')
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('initiate.bd')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products


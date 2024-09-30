import sqlite3

connection = sqlite3.connect('not_telegram.bd')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users1(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users1 (email)')

'''
ДОБАВЛЕНИЕ
'''
# for i in range (1, 11):
#         cursor.execute('INSERT INTO Users1 (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                        (f'User{i}', f'example{i}@gmail.com', str (i * 10) , 1000))
'''
ИЗМЕНЕНИЕ
'''
# for i in range (1, 11, 2):
#     cursor.execute('UPDATE Users1 SET balance = ? WHERE username = ?', (500, f'User{i}'))

'''
УДАЛЕНИЕ
'''
# for i in range (11):
#     cursor.execute('DELETE FROM Users1 WHERE id = ?', (6,))

'''
ФИЛЬТР И ВЫВОД НА КОНСОЛЬ
'''
# cursor.execute('SELECT username, email, age, balance FROM Users1 WHERE age != ?', (60,))
# info = cursor.fetchall()
# for i in info:
#     print(f'Имя: {i[0]} | Почта: {i[1]} | Возраст {i[2]} | Баланс: {i[3]}')
'''
ПОДСЧЕТ ЗАПИСЕЙ
'''
cursor.execute('SELECT COUNT(*) FROM Users1')
total_user = cursor.fetchone()[0]
print(total_user)

'''
ПОДСЧЕТ СУММЫ
'''
cursor.execute('SELECT SUM(balance) FROM Users1')
all_balance = cursor.fetchone()[0]
print(all_balance)

print(f'Средний баланс: {all_balance / total_user}')

connection.commit()
connection.close()
import sqlite3

connection = sqlite3.connect('not_telegram2.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''') #Создаем БД, прописываем условие, что если БД уде существует, то новую создавать не нужно
#Прописываем поля и их характеристики

for num_user in range(1,11): # Добавили 10 пользователей со своими данными
     cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?,?,?,?)',(f'User{num_user}', f'example{num_user}@gmail.com', f'{num_user*10}', '1000'))

cursor.execute('UPDATE Users SET balance=? WHERE id%2=?', (500, True))

def every_number_delete(number): # Ф-я производит удаление каждого порядкового числа указонного в условии начиная с первого
    flag_delete=1
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for i in range(len(users)+1):
        if flag_delete==1:
            cursor.execute('DELETE FROM Users WHERE id=?', (i+1,))
        flag_delete+=1
        if flag_delete==(number+1):
            flag_delete=1

every_number_delete(3) #Удалит каждую третью запись в таблице начиная с первой
cursor.execute('SELECT * FROM Users')


connection.commit()
connection.close()
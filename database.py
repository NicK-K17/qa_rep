# импорт пакета который позволяет соединяться с базой данных
import mysql.connector as mysql

# соединение с базой данных (подключение)
db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True) # создание переменной курсор для удобства обращения (данные в виде словоря)

cursor.execute('SELECT * FROM students') # создание и отправка запроса в базу данных

data = cursor.fetchall() # получение ответа от базы данных
# for student in data:
#     print(student['second_name'])

cursor.execute('SELECT * FROM students WHERE id =  4889 ')
print(cursor.fetchone()) # используем fetchone если нужен один обьект а не список состоящий из одного обьекта


db.close() # отключение от базы данных
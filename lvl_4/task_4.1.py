# Задача 4.1.
# Домашнее задание на SQL
# В базе данных teacher создайте таблицу Students
# Структура таблицы: 
# Student_Id - Integer, 
# Student_Name - Text, 
# School_Id - Integer (Primary key)
# _____
# Наполните таблицу следующими данными:
# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4
# ______________
# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:
# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

#1 сoздание таблицы Students
import sqlite3

connection = sqlite3.connect('C:\\Users\\Пользователь\\envs\\homeworks\\lvl_4\\teatchers.db')
cursor = connection.cursor()
sqlquery = """CREATE TABLE Students (
Student_Id INTEGER NOT NULL, 
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL PRIMARY KEY
);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()

# #2 Заполнение таблицы Students
import sqlite3

connection = sqlite3.connect('C:\\Users\\Пользователь\\envs\\homeworks\\lvl_4\\teatchers.db')
cursor = connection.cursor()
sqlquery = """
INSERT INTO Students (Student_Id, Student_Name, School_Id)
VALUES
('201', 'Иван', 1),
('202', 'Петр', 2),
('203', 'Анастасия', 3),
('204', 'Игорь', 4);
""" 
cursor.execute(sqlquery)
connection.commit()
connection.close()

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.
# Формат вывода:
# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


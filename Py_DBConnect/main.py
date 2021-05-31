import sqlite3
import sys

connection = sqlite3.connect("people.db")
cursor = connection.cursor()

try:
    cursor.execute("CREATE TABLE people (name TEXT, age INTEGER, skills STRING)")
except Exception as e:
    pass

def user_is_unique(name):
    rows = cursor.execute("SELECT name, age, skills FROM people").fetchall()

    for user in rows:
        if user[0] == name:
            return False
    return True

def insert_db():
    name = input("Name >> ")

    if user_is_unique(str(name)):
        age = input("Age >> ")
        skills = input("Skills >> ")

        if name != "" and age != "" and skills != "":
            cursor.execute(f"INSERT INTO people VALUES ('{name}', '{age}', '{skills}')")
            connection.commit()
            print(name + " has been added to the database!")

        else:
            print("One of the fields are empty! Please try again!")
            insert_db()
    else:
        print("Name is already in the database!")



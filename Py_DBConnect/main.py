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



def edit_db():
    name = input("Type the name of the person you'd like to edit >> ")
    field = input("Which field would you like to edit: name, age or skills? >> ")
    updated_field = input("What would you like to update it to ? >> ")

    try:
        cursor.execute(f"Update people SET {field} = ? WHERE name = ?", (updated_field, name))
        connection.commit()
        print("Successfully updated user!")
    except Exception as e:
        print(e)



def get_user_info_db():
    target_name = input("Who do you want to see information about? >> ")
    rows = cursor.execute("SELECT name, age, skills FROM people WHERE name = ?", (target_name),).fetchall()
    # rows [(name, age, skills)]


    name = rows[0][0]
    age = rows[0][1]
    skills = rows[0][2]

    print(f"{name} is {age} years old and works as {skills}.")



def delete_db():
    name = input("Type the name of the person that you would like to delete >> ")
    if name != "":
        cursor.execute("DELETE FROM people WHERE name = ?", (name,))
        connection.commit()
        print("User successfully deleted!")

























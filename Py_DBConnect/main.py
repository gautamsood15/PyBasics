import sqlite3
import sys

connection = sqlite3.connect("people.db")
cursor = connection.cursor()

try:
    cursor.execute("CREATE TABLE people (name TEXT, age INTEGER, skills STRING)")
except Exception as e:
    pass



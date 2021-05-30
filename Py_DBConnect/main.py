import sqlite3
import sys

connection = sqlite3.connect("people.db")
cursor = connection.cursor()

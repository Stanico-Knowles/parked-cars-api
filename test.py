# check if price is passed to database 

import sqlite3 

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

showTables = "SELECT * FROM cars"
cursor.execute(showTables)

for row in cursor.execute(showTables):
    print(row)
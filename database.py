import sqlite3

mydb = sqlite3.connect('user_bank.db')
myCursor = mydb.cursor()
myCursor.execute("""
        CREATE TABLE IF NOT EXISTS user_bank (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            age INTEGER,
            gender TEXT,
            balance INTEGER,
            password TEXT
        )
""")
mydb.commit()

import sqlite3

conn = sqlite3.connect('UsersData.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    matricula TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);
""")

print("connect")

# conn.commit()
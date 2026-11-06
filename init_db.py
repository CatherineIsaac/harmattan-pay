import sqlite3

conn = sqlite3.connect("harmattan.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    balance INTEGER NOT NULL DEFAULT 0
)
""")

cur.execute("INSERT INTO users (username, password, balance) VALUES (?, ?, ?)", ("catherine", "harmattan123", 50000))
cur.execute("INSERT INTO users (username, password, balance) VALUES (?, ?, ?)", ("amaka", "chelsea2020", 125000))

conn.commit()
conn.close()
print("Database created with 2 users.")


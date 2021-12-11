import sqlite3

con = sqlite3.connect('./database.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS teachers(teacher_id INT, name TEXT)")
cur.execute()

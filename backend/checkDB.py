import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# 列出所有表格名稱
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table in tables:
    print(table[0])

conn.close()

import sqlite3
import random
from faker import Faker
from datetime import datetime
import uuid

# 初始化 Faker
faker = Faker()

# 連接到 SQLite3 資料庫
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# 插入 200 筆隨機資料
count = 0
while count < 200:
    userid = faker.user_name()
    password = faker.password()
    useremail = faker.email()
    userloginhost = faker.domain_name()
    totalscore = random.randint(0, 1000)
    last_login_time = faker.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    login_token = uuid.uuid4().hex

    try:
        cursor.execute('''
        INSERT INTO backend_usertab (userid, password, useremail, userloginhost, totalscore, last_login_time, created_at, updated_at, login_token)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (userid, password, useremail, userloginhost, totalscore, last_login_time, created_at, updated_at, login_token))
        count += 1
    except sqlite3.IntegrityError:
        # 如果遇到唯一性約束錯誤，跳過該次插入
        continue

# 儲存變更並關閉連接
conn.commit()
conn.close()

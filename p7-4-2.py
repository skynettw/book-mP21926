import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    database='books',
    user='root',
    password='你設定的密碼'
)

if conn.is_connected():
    print("Successful!")
    conn.close()
else:
    print("Fail to connect!")
    conn.close()
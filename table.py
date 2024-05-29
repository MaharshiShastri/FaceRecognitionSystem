import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Maharshi#20",
    database = "employee_management"
    )
cur = conn.cursor()

cur.execute("select * from employee_resgister")

row = cur.fetchall()

conn.close()


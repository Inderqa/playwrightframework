import mysql.connector
import pymysql
import random

conn = pymysql.connect(
    host="localhost",
    user = "root",
    database = "employeee"
)

cursor = conn.cursor()
names = ["Ronit", "Pric", "Nom", "Medha", "Parul", "Aditya", "Vaid", "Nath", "Dabi", "Parchani"]
depts = ["QA", "Dev", "HR", "Ops"]
designations = ["SDET", "Engineer", "Manager", "Lead"]
try:
    with conn.cursor() as cursor:
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS org (
                        emp_id int AUTO_INCREMENT PRIMARY KEY,
                        emp_name VARCHAR(50),
                        emp_dept VARCHAR(20),
                        emp_desi VARCHAR(30),
                        salary INT
                    );
                """)
        for _ in range(100):
            name=random.choice(names)
            dept = random.choice(depts)
            desg = random.choice(designations)
            salary = random.randint(30000, 100000)
            cursor.execute(
                "INSERT INTO org (emp_name, emp_dept, emp_desi, salary) VALUES (%s, %s, %s, %s)",
                (name, dept, desg, salary)
            )
    conn.commit()
    print("100 records succesfull")

except Exception as e:
    print(e)

finally:
    conn.close()




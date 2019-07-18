import sqlite3
import time
import csv

conn = sqlite3.connect("dw.sqlite")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS SUICIDE(year, sex, age, suicides_no, population, generation);")

def cadastro(a1, a2, a3, a4, a5, a6):
    c.execute("""INSERT INTO SUICIDE VALUES (?,?,?,?,?,?)""", (a1, a2, a3, a4, a5, a6))
    conn.commit()

def suicide_start():
    with open("master.csv") as file:

        reader = csv.DictReader(file)
        cont = 0

        for row in reader:

            year = str(row['year'])
            sex = str(row['sex'])
            age = str(row['age'])
            suicides_no = str(row['suicides_no'])
            population = str(row['population'])
            generation = str(row['generation'])

            print(year + " - " + sex + " - " + age + " - " + suicides_no + " - " + population + " - " + generation)
            cadastro(year, sex, age, suicides_no, population, generation)
        
        c.close()
        conn.close()

create_table()
suicide_start()
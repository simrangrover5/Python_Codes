import sqlite3 as sql

db = sql.connect('grras.db')

c = db.cursor()


cmd = 'select * from student'
c.execute(cmd)

data = c.fetchall()

print("Data of Student Table : ")

for item in data : 
    print(*item)

cmd = 'select * from fees' 

print("Data of Fees Table ")

c.execute(cmd)

data = c.fetchall()

for item in data : 
    print(*item)

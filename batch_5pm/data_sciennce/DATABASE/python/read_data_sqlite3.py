import sqlite3 as sql 
db = sql.connect('c:/users/sachin/desktop/mydatabase.db')


c = db.cursor()

c.execute('select * from data')

data= c.fetchall()

for row in data : 
    print('\t\t',*row,sep='\t\t')

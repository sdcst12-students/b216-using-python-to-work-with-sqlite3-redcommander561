#!python

"""
Create a query to create a table to store customers information into a database for a veterinarian
Each record needs to have the following information:
id unique integer identifier
owner name
owner email
owner phone number
owner customer identification number
owner address
owner balance owing

choose appropriate variable types for each field
create the database and add the following information. Make sure you commit the information to save it:
name            email           phone number    ID      address                 balance
Joe Smith       joe@gmail.com   7783341111      101     1234 Sesame Street      0
Fred Jones      fred@city.com   6045553434      102     75 57 Street            0
Leroy Jenkins   leroy@wow.ca    2342222323      103     65 Blizzard Ave         100     
Jen Mezei       jen@shaw.ca     6042231134      104     891 Cullen Cresc        0
"""

import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
cursor.execute("drop table if exists customers")


query = """
create table if not exists customers (
id integer primary key autoincrement,
name text,
email text,
phoneNum text,
address text,
balance integer
);
"""
cursor.execute(query)

data = [
    ['Joe Smith', 'joe@gmail.com', '7783341111',101,'1234 Sesame Street', 0],
    ['Fred Jones', 'fred@city.com', '6045553434',102, '75 57 Street', 0],
    ['Leroy Jenkins', 'leroy@wow.ca', '2342222323',103, '65 Blizzard Ave', 100],
    ['Jen Mezei', 'jen@shaw.ca', '6042231134',104, '891 Cullen Cresc', 0]
]

for i in data:
    query = f"insert into customers (name, email, phoneNum, id , address, balance) values ('{i[0]}', '{i[1]}', '{i[2]}', {i[3]}, '{i[4]}', {i[5]});"
    cursor.execute(query)

connection.commit()

query = "select * from customers"
cursor.execute(query)
result = cursor.fetchall()
for i in result:
    print(i)

connection.close()
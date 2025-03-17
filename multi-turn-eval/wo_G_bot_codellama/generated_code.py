f = open("file.txt", "r")
while 1:
    line = f.readline()
    if not line:
        break
    print(line)

x = 1
y = 2
z = 3

f = open("file.txt", "r")
while 1:
    line = f.readline()
    if not line:
        break
    print(line)

import psycopg2
conn = psycopg2.connect(
    host="localhost",
    dbname="mydatabase",
    user="myusername",
    password="mypassword",
)
while 1:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mytable")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

import psycopg2
conn = psycopg2.connect(
    host="localhost",
    dbname="mydatabase",
    user="myusername",
    password="mypassword",
)
while 1:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mytable")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
import mysql.connector

con = mysql.connector.connect(host='localhost', database="cat", user='root', password='Server@1234')

# To create table in Python PDBC 
# con =  mysql.connector

# creating the cursor for connection
cursor = con.cursor()

# create a table
create = 'create table employee(eno int, ename varchar(40), age int, ecity varchar(40), ecountry varchar(40))'
print("Table Created")

# using cursor to execute one or more queries
cursor.execute(create)

# closing the cursor object
cursor.close()
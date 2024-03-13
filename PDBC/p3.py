import mysql.connector

con = mysql.connector.connect(host='localhost', database="cat", user='root', password='Server@1234')

# To create table in Python PDBC 
# con =  mysql.connector

# creating the cursor for connection
cursor = con.cursor()

# insert a record
insert = 'insert into employee(eno, ename, age, ecity, ecountry) values (%s, %s, %s, %s, %s)'
values = (101, "Sai Kiran", 28, "Hyd", "India")
print("Data Inserted")

# using cursor to execute one or more queries
cursor.execute(insert, values)

# commit the record
con.commit()

# closing the cursor object
cursor.close()

# close the connection object
con.close()
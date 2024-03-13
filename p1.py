import mysql.connector


con = mysql.connector.connect(host='localhost', database="cat", user='root', password='Server@1234')

print("Connection Tested")  
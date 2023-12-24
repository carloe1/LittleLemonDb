import mysql.connector as connector

connection = connector.connect(user="ubuntu", password="negMab-tumhes-pejxi3")

## Standard Cursor
cursor = connection.cursor()

cursor.execute("USE little_lemon")
cursor.execute("SHOW TABLES")

print("Showing Tables in little_lemon")
for table in cursor:
    print(table)


print()
## Buffered Cursor
try:
    print("Buffered cursor")
    cursor = connection.cursor(buffered=True)
    cursor.execute("USE little_lemon")
    cursor.execute("SELECT * FROM Bookings")
    cursor.execute("SELECT * FROM Orders")
    print("Buffered cursor executes success")
    
except Exception as e:
    print("Buffered cursor execute failed:" + str(e))


print()
## Standard Cursor
try:
    print("Standard cursor")
    #cursor = connection.cursor()
    #cursor.execute("USE little_lemon")
    #cursor.execute("SELECT * FROM Bookings")
    #cursor.execute("SELECT * FROM Orders")
    print("Standard cursor executes success")

except Exception as e:
    print("Standard cursor execute failed:" + str(e)) 

print()
## Dictionary Cursor
cursor = connection.cursor(dictionary=True)
cursor.execute("USE little_lemon")
cursor.execute("SHOW TABLES")

print("Dictionary cursor")
for table in cursor:
    print(table)

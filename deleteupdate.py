import mysql.connector as connector
connection = connector.connect(user="ubuntu", password="negMab-tumhes-pejxi3")
cursor = connection.cursor()

cursor.execute("USE little_lemon")

## Task 1 - Select bookings
select_stmt = """SELECT * FROM Bookings """
cursor.execute(select_stmt)

num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]


print(field_names)
for booking in cursor:
    print(booking)


update_stmt = """UPDATE Bookings SET TableNo=10 WHERE GuestFirstName='Diana' AND GuestLastName='Pinto' """

cursor.execute(update_stmt)
cursor.execute(select_stmt)

print(field_names)
for booking in cursor:
    print(booking)


update_stmt = """UPDATE Bookings SET TableNo=11, EmployeeID=6 WHERE GuestFirstName='Joakim' AND GuestLastName='Iversen' """
cursor.execute(update_stmt)
cursor.execute(select_stmt)

print(field_names)
for booking in cursor:
    print(booking)


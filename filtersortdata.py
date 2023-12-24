import mysql.connector as connector

connection = connector.connect(user="ubuntu", password="negMab-tumhes-pejxi3")
cursor = connection.cursor()

cursor.execute("USE little_lemon")

print("Task 1 =====================================================")
task1_select_stmt = """SELECT TableNo, GuestFirstName, GuestLastName, EmployeeID FROM Bookings WHERE TableNo=12 """
cursor.execute(task1_select_stmt)

field_names = [i[0] for i in cursor.description]
print(field_names)
for booking in cursor:
    print(booking)


print()
print("Task 2 =====================================================")
task2_select_stmt = """SELECT BookingID, BillAmount FROM Orders WHERE BillAmount>40 """

cursor.execute(task2_select_stmt)
field_names=[i[0] for i in cursor.description]
print(field_names)
for orders in cursor:
    print(orders)

print()
print("Task3 =====================================================")
task3_select_stmt = """select * from MenuItems where Type in ('Starters', 'Desserts') ORDER BY Price """


cursor.execute(task3_select_stmt)
field_names=[i[0] for i in cursor.description]
print(field_names)
for item in cursor:
    print(item)

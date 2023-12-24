import mysql.connector as connector

connection = connector.connect(user="ubuntu", password="negMab-tumhes-pejxi3")

cursor = connection.cursor()
cursor.execute("USE little_lemon")

print("Task 1 ==============================================================")
join_query = "SELECT Name AS Item_Name, Type AS Item_Type, Price, Cuisine FROM Menus m INNER JOIN MenuItems i ON m.ItemID=i.ItemID;"
cursor.execute(join_query)

field_names = [i[0] for i in cursor.description]
print(field_names)
for item  in cursor:
    print(item)

print()
print("Task 2 =============================================================")
task2_query = "SELECT Name as Item_Name, Type as Item_Type, Price FROM MenuItems WHERE ItemID NOT IN (SELECT DISTINCT ItemID FROM Menus);"
cursor.execute(task2_query)

field_names = [i[0] for i in cursor.description]
print(field_names)
for item in cursor:
    print(item)

print()
print("Task 3 ============================================================")
task3_query = "SELECT b.BookingID, b.TableNo, b.GuestFirstName, o.BillAmount FROM Orders o INNER JOIN Bookings b ON o.BookingID=b.BookingID;"
cursor.execute(task3_query)

field_names = [i[0] for i in cursor.description]
print(field_names)
for item in cursor:
    print(item)

import mysql.connector as connector
connection = connector.connect(user="ubuntu", password="negMab-tumhes-pejxi3")

cursor = connection.cursor()
cursor.execute("USE little_lemon")

print("Task 1 =============================================================")
task1_query = "SELECT HOUR(BookingSlot) Hour, COUNT(*) TotalBookings FROM Bookings GROUP BY HOUR(BookingSlot) ORDER BY HOUR(BookingSlot)"

cursor.execute(task1_query)
field_names = [i[0] for i in cursor.description]
print(field_names)
for item in cursor:
    print(item)

print("Task 2 =============================================================")

import mysql.connector as connector
connection = connector.connect(user="ubuntu", password="negMab-tumhes-pejxi3")

# Creating cursor object
cursor = connection.cursor()

# Setting the databse for use
cursor.execute("USE little_lemon")

print("Task 1 ==============================================================")
task1_query = "SELECT BookingID ID, CONCAT(GuestFirstName, ' ', GuestLastName) as GuestFullName FROM Bookings;"
cursor.execute(task1_query)

field_names = [i[0] for i in cursor.description]
print(field_names)
for item in cursor:
    print(item)

print("Task 2 =============================================================")
task2_query = "SELECT * FROM Bookings"

print("Today's statistics:")

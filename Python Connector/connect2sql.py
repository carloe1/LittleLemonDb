import mysql.connector as connector
connection = connector.connect(user="ubuntu", password="negMab-tumhes-pejxi3")
cursor = connection.cursor()

print("Showing Databases")
cursor.execute("show databases")
for database in cursor:
    print(database)

print()
print("Creating Tables")
# checking to which database we are connected to now
cursor.execute("use little_lemon")
print("DB in use: " + connection.database)

## Create MenuItems table using the string statement below
create_menuitem_table = """CREATE TABLE IF NOT EXISTS MenuItems (
ItemID INT AUTO_INCREMENT,
Name VARCHAR(200),
Type VARCHAR(100),
Price INT,
PRIMARY KEY (ItemID)
);"""

create_menu_table = """CREATE TABLE IF NOT EXISTS Menus (
MenuID INT,
ItemID INT,
Cuisine VARCHAR(100),
PRIMARY KEY (MenuID,ItemID)
);"""

create_booking_table = """CREATE TABLE IF NOT EXISTS  Bookings (
BookingID INT AUTO_INCREMENT,
TableNo INT,
GuestFirstName VARCHAR(100) NOT NULL,
GuestLastName VARCHAR(100) NOT NULL,
BookingSlot TIME NOT NULL,
EmployeeID INT,
PRIMARY KEY (BookingID)
);"""

create_orders_table = """CREATE TABLE IF NOT EXISTS Orders (
OrderID INT,
TableNo INT,
MenuID INT,
BookingID INT,
BillAmount INT,
Quantity INT,
PRIMARY KEY (OrderID,TableNo)
);"""


cursor.execute(create_menuitem_table)
print("Table Created: MenuItems")

cursor.execute(create_menu_table)
print("Table Created: Menu")

cursor.execute(create_booking_table)
print("Table created: Bookings")

cursor.execute(create_orders_table)
print("Table created: Orders")

# Confirming
print()
print("Showing tables in DB")
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

print()

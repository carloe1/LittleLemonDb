import mysql.connector as connector
connection=connector.connect(user="ubuntu",password="negMab-tumhes-pejxi3")

cursor = connection.cursor()
cursor.execute("USE little_lemon")



all_bookings = """SELECT GuestFirstName, GuestLastName, TableNo FROM Bookings"""
cursor.execute(all_bookings)

for booking in cursor:
    print(booking)


all_bookings = """SELECT GuestFirstName, GuestLastName, TableNo FROM Bookings"""
cursor.execute(all_bookings)

for booking in cursor:
    print(booking)


all_bookings = """SELECT GuestFirstName, GuestLastName, TableNo FROM Bookings"""
cursor.execute(all_bookings)

for booking in cursor:
    print(booking)


all_bookings = """SELECT GuestFirstName, GuestLastName, TableNo FROM Bookings"""
cursor.execute(all_bookings)

for booking in cursor:
    print(booking)


all_bookings = """SELECT GuestFirstName, GuestLastName, TableNo FROM Bookings"""
cursor.execute(all_bookings)

for booking in cursor:
    print(booking)


all_bookings = """SELECT GuestFirstName, GuestLastName, TableNo FROM Bookings"""
cursor.execute(all_bookings)

for booking in cursor:
    print(booking)


all_bookings = """SELECT GuestFirstName, GuestLastName, TableNo FROM Bookings"""
cursor.execute(all_bookings)

for booking in cursor:
    print(booking)



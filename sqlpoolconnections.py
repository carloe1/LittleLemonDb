import os
import mysql.connector as connector

##
## Database Configuration and Connection
dbconfig={
        "host": "localhost",
        "database": "little_lemon_db",
        "user": os.environ.get("MYSQL_USER"),
        "password": os.environ.get("MYSQL_PASSWORD")
}

connection=connector.connect(**dbconfig)
cursor=connection.cursor()


## Task 1
peak_hours_query = """CREATE PROCEDURE IF NOT EXISTS PeakHours()
BEGIN
SELECT HOUR(BookingSlot) BookingHour, COUNT(*) Bookings FROM Bookings GROUP BY HOUR(BookingSlot) ORDER BY Bookings DESC;
END;"""

cursor.execute(peak_hours_query)
cursor.callproc("PeakHours")
dataset=cursor.fetchall()
for row in dataset:
    print(row)

## Task 2
guest_status_query = """CREATE PROCEDURE IF NOT EXISTS GuestStatus()
BEGIN
SELECT 
    CONCAT(GuestFirstName, ' ', GuestLastName) AS FullName 
    ,CASE
        WHEN e.Role IN ('Manager', 'Assistant Manager') THEN 'Ready to pay'
        WHEN e.Role IN ('Head Chef') THEN 'Ready to serve'
        WHEN e.Role IN ('Assistant Chef') THEN 'Preparing'
        WHEN e.Role IN ('Head Waiter') THEN 'Order served'
    ELSE 'N/A' END as Status
FROM Bookings b 
    LEFT JOIN Employees e 
        ON b.EmployeeID=e.EmployeeID;
END;"""

cursor.execute(guest_status_query)
cursor.callproc("GuestStatus")
dataset=cursor.fetchall()


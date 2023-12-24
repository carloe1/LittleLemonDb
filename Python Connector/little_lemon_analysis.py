import os
import mysql.connector as connector
from  mysql.connector import Error

## Guest Data
guest_connections = dict()
guests = {
    1: {
        'Table Number': 8,
        'First Name': 'Anees',
        'Last Name': 'Java',
        'Booking Time': '18:00',
        'EmployeeID': 6
    },
    2: {
        'Table Number': 5,
        'First Name': 'Bald',
        'Last Name': 'Vin',
        'Booking Time': '19:00',
        'EmployeeID': 6
    },
    3: {
        'Table Number': 12,
        'First Name': 'Jay',
        'Last Name': 'Kon',
        'Booking Time': '19:30',
        'EmployeeID': 6
    }
}

## SQL queries
insert_booking = "INSERT INTO Bookings (TableNo, GuestFirstName, GuestLastName, BookingSlot, EmployeeID) VALUES(%s, %s, %s, %s, %s)"



##
## Database Configuration and Connection
dbconfig={
        "host": "localhost",
        "database": "little_lemon_db",
        "user": os.environ.get("MYSQL_USER"),
        "password": os.environ.get("MYSQL_PASSWORD")
        }
##
## Establish connection pool
try:

    ## Task 1 =========================================================================
    print("Task 1 ==========================================================")
    pname="pool_b"
    psize=2
    connection_pools = connector.pooling.MySQLConnectionPool(pool_name=pname, pool_size=psize, **dbconfig)

    print("The connection pool is creatred with name: " + pname)
    print("The pool size is: ", str(psize))
    print()

    print("Task 2 ==========================================================")
    ## Insert the guest data, add connections to pool as needed
    for guest in guests:
        
        guest_dict = guests[guest]

        try:
            guest_connections[guest] = connection_pools.get_connection()
            

        except Exception as e:
            print("No more connections are available.")
            print("Adding new connection to the pool.")
            psize += 1
            connection_pools = connector.pooling.MySQLConnectionPool(pool_name=pname, pool_size=    psize, **dbconfig)
            print("The pool size is: ", str(psize))
            #new_connection = connector.connect(**dbconfig)
            #connection_pools.add_connection(new_connection)
            guest_connections[guest] = connection_pools.get_connection()


        print("Guest " + str(guest) + " is connected.")
        print("Booking Guest " + str(guest) + ".")
        
        guest_data = (guest_dict["Table Number"], guest_dict["First Name"], guest_dict["Last Name"], guest_dict["Booking Time"], guest_dict["EmployeeID"])
        
        #print(guest_data)
        for key in guest_dict:
            print("\t" + str(key) + ": " + str(guest_dict[key]))

        cursor = guest_connections[guest].cursor()
        cursor.execute(insert_booking, guest_data)
        guest_connections[guest].commit()
        
        
        print()

    print("Closing all guest connections.")
    for connection in guest_connections:
        guest_connections[connection].close()
    print("All connections returned to pool.")
    print()

    ## Task 3 =============================================================
    print("Task 3 ===========================================================")

    manager_query = """SELECT EmployeeID, Name FROM Employees WHERE Role='Manager';"""
    highest_salary_query = """SELECT Name, Role FROM Employees ORDER BY Annual_Salary DESC LIMIT 1;"""
    bookings_between_range_query = """SELECT COUNT(*) NumberOfBookings FROM Bookings WHERE BookingSlot>='18:00:00' AND BookingSlot<='20:00:00';"""
    waiting_to_be_seated_query = """SELECT CONCAT(GuestFirstName, ' ', GuestLastName) FullName, BookingID FROM Bookings b INNER JOIN Employees e on b.EmployeeID=e.EmployeeID WHERE e.Role='Receptionist' ORDER BY BookingSlot;"""

    connection = connection_pools.get_connection()
    cursor = connection.cursor()
    
    print("Manager Query")
    cursor.execute(manager_query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    print()

    print("Highest Salary")
    cursor.execute(highest_salary_query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    print()

    print("Total Bookings Between 18:00 and 20:00")
    cursor.execute(bookings_between_range_query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    print()

    print("Guests waiting to be seated by Receptionist")
    cursor.execute(waiting_to_be_seated_query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    print()
    print()

    ## Task 4 ==============================================================
    print("Task 4 ===========================================================")
    # Create a stored procedure named BasicSalesReport. 
    cursor.execute("DROP PROCEDURE IF EXISTS BasicSalesReport;")

    stored_procedure_query="""
        CREATE PROCEDURE BasicSalesReport()

        BEGIN
        SELECT 
        SUM(BillAmount) AS Total_Sale,
        AVG(BillAmount) AS Average_Sale,
        MIN(BillAmount) AS Min_Bill_Paid,
        MAX(BillAmount) AS Max_Bill_Paid
        FROM Orders;
        END
        """
    # Execute the query
    cursor.execute(stored_procedure_query)

    #********************************************#

    # Call the stored procedure with its name
    cursor.callproc("BasicSalesReport")

    # Retrieve records in "dataset"
    results = next(cursor.stored_results())
    results = results.fetchall()

    # Retrieve column names using list comprehension in a for loop 
    for column_id in cursor.stored_results():
        cols = [column[0] for column in column_id.description]

    
    print("Baisc Sales Report:")
    for result in results:
        print(cols[0],":",result[0])
        print(cols[1],":",result[1])
        print(cols[2],":",result[2])
        print(cols[3],":",result[3])


    ## Task 5 ==========================================================
    print("Task 5 ======================================================")
    sql_query="""SELECT 
        Bookings.BookingSlot,
        CONCAT(Bookings.GuestFirstName," ",Bookings.GuestLastName) AS Guest_Name,
        Employees.Name AS Emp_Name,
        Employees.Role AS Emp_Role
        FROM Bookings 
        INNER JOIN 
        Employees ON Bookings.EmployeeID=Employees.EmployeeID
        ORDER BY Bookings.BookingSlot ASC;"""
    cursor.execute(sql_query)
    results=cursor.fetchmany(size=3)
    
    print("Next 3 upcomming Bookings:")
    for result in results:
        print("BookingSlot",result[0])
        print("Guest_name:",result[1])
        print("Assigned to:",result[2],"[{}]".format(result[3]))


## Connection failed, raise the error
except Exception as e:
    print(e)

import mysql.connector as connector

dbconfig = {"database": "little_lemon", "user": "ubuntu", "password":"negMab-tumhes-pejxi3"}

print("Task 1 =================================================================")
try:
    pname = "ll_pool_a"
    psize = 3
    connection_pools = connector.pooling.MySQLConnectionPool(pool_name=pname,pool_size=psize, **dbconfig)
    print("The connection pool is created with name: " + pname)
    print("The pool size is: " + str(psize))
    
    print()
    print("Task 2 ============================================================")
    print("Gettinga connection from the pool.")
    connection1 = connection_pools.get_connection()
    
    print("Gettinga cursor object.")
    connection1_cursor = connection1.cursor()
    
    print("Executing the SQL Query.")
    task2_query = "SELECT BookingID, GuestFirstName, GuestLastName FROM Bookings"
    connection1_cursor.execute(task2_query)

    print("Fetching the query results.")
    results = [item for item in connection1_cursor]

    print("Retrieving the column names.")
    column_names = [i[0] for i in connection1_cursor.description]

    print("Printing the results.")
    print("Upcoming Bookings are:")
    print()
    print(column_names)
    for result in results:
        print(result)

    print()
    print("Returning the connection back to the pool.")
    connection1_cursor.close()
    connection1.close()

    print("The connection is placed back into the pool for the next user to connect.")

    print()
    print("Task 3 =========================================================")
    guests = ["Anna", "Marcos", "Diana", "Joakim", "Hiroki"]
    guest_connections = dict()
    for guest in guests:
        
        try:
            guest_connections[guest] = connection_pools.get_connection()
            print(guest + " is connected.")
            print()
        
        except Exception as e:
            print("No more connections are avaiable.")
            print("Adding new connection in the pool.")
            new_connection = connector.connect(**dbconfig)
            connection_pools.add_connection(new_connection)

            guest_connections[guest] = connection_pools.get_connection()
            print(guest + " is connected.")
            print()

except Exception as e:
    print(e)
    


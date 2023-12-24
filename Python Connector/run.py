# Print a message to guide the user
# Import MySQL Connector/Python
print("Importing MySQL Connector/Python API")
import mysql.connector as connector
print("MySQL Connector/Python API is imported successfully.\n")

# Establish connection with authorized user/password
print("Establishing a new connection between MySQL and Python")
#connection=connector.connect(user="ubuntu",password="negMab-tumhes-pejxi3")

try:
    connection=connector.connect(user="ubuntu",password="negMab-tumhes-pejxi3")
    print("A connection between MySQL and Python is successfully extablished")

    cursor = connection.cursor()
    create_database_query="CREATE DATABASE IF NOT EXISTS little_lemon"
    cursor.execute(create_database_query)
    use_database_query="USE little_lemon"
    cursor.execute(use_database_query)
    
    create_menu_item_table="CREATE TABLE IF NOT EXISTS MenuItems(ItemID INT AUTO_INCREMENT, Name VARCHAR(200), Type VARCHAR(100), Price INT, PRIMARY KEY(ItemID))"
    cursor.execute(create_menu_item_table)



except connector.Error as er:
    print("Error code:", er.errno)
    print("Error message:", er.msg)

except Exception as e:
    logger.error("Failed connect to MySQL Server: " + str(e))





# Close the Connection if the Connection is made
if connection.is_connected():
    connection.close()
    print("MySQL connection is closed.")
else:
    print("Connection is already close")

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

pname = "ll_pool_a"
psize = 2
try:
    connection_pools = connector.pooling.MySQLConnectionPool(pool_name=pname,pool_size    =psize, **dbconfig)
    
    new_connection = connector.connect(**dbconfig)
    connection_pools.add_connection(new_connection)

except:
    raise(connector.Error)

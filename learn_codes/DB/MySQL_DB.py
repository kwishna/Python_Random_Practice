import mysql.connector as db
#   https://www.datacamp.com/community/tutorials/mysql-python
d = db.connect( host = "localhost",
                user = "root",
                port = 3306,
                passwd = "********",
                database = None
              )

if not d.is_connected():
    assert False
cursor = d.cursor()
## executing the statement using 'execute()' method
cursor.execute("SHOW DATABASES")
## 'fetchall()' method fetches all the rows from the last executed statement
databases = cursor.fetchall() ## it returns a list of all databases present
## printing the list of databases
print(databases)
## showing one by one database
for database in databases:
    print(database)
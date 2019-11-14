import sqlite3
from sqlite3.dbapi2 import Connection

connect: Connection = sqlite3.connect("first1.db")
print("DATABASE OPENED SUCCESSFULLY")
cursor = connect.cursor()
cursor.execute(
                    '''CREATE TABLE COMPANY
                    (   ID         INT     PRIMARY KEY     NOT NULL,
                        NAME       TEXT                    NOT NULL,
                        AGE        INT                     NOT NULL,
                        ADDRESS    CHAR(50),
                        SALARY     REAL                            
                    );'''
               )

print("TABLE CREATED SUCCESSFULLY")

cursor.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES (4, 'Paul4', 32, 'California4', 20000.00);")

data = [(1, 'Paul1', 32, 'California1', 20000.00),
        (2, 'Paul2', 32, 'California2', 20000.00),
        (3, 'Paul3', 32, 'California3', 20000.00)]

cursor.executemany("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES (?, ?, ?, ?, ?);", data)

print("DATA INSERTED SUCESSFULLY\n")
connect.commit()    # Commit Is Done On Connection
# connect.close()
# print("CONNECTION CLOSED")


# conn = sqlite3.connect('hi.db')
# print("DATABASE OPENED SUCCESSFULLY")

cur = cursor.execute("SELECT id, name, address, salary from COMPANY")
for row in cur:
    print("ID   = ",    row[0])
    print("NAME = ",    row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ",  row[3], "\n")

#  Since The For Loop Has Printed All The Values. Cursor Has Reached To Its End. Hence, No Row Data Is Left To Be Printed Further.

print('Fetch All - \n', cur.fetchall())
print('Fetch Many 2 - \n', cur.fetchmany(2))
print('Fetch One - \n', cur.fetchone())


print("OPERATION DONE SUCCESSFULLY")
cur.close()
connect.close()
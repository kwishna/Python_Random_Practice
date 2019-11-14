import sqlite3

conn = sqlite3.connect('sqlite2DB.db')
cur = conn.cursor()

# cur.execute('''
#             CREATE TABLE FIRSTTABLE(
#             SERIAL_NO INTEGER,
#             NAME VAR(30),
#             DATA BLOB
#             );
#             ''')
# conn.commit()
# conn.close()
'''
    Writing And Reading BLOB File In Sqlite.
'''
with open('LinuxDirectories.png', 'rb') as f: # file Must Be Read In Binary Only

    p = f.read()

    # else,
    # pic = f.buffer
    # p = pic.read()

data = (None, 'This Pic', p)

cur.execute('INSERT INTO FIRSTTABLE VALUES(?, ?, ?)', data)
conn.commit()

cur2 = cur.execute('SELECT * FROM FIRSTTABLE')
for row in cur2.fetchall():
    h = row[2]
    print(h)
    with open(str(row[0])+'.png', 'wb') as a:
        a.write(h)

conn.close()
import sqlite3

conn = sqlite3.connect('test.db')
#print ("Opened database successfully")

try:
    conn.execute('''CREATE TABLE Employee
              (ID INT PRIMARY KEY     NOT NULL,
              NAME           TEXT    NOT NULL,
              AGE            INT     NOT NULL,
              ADDRESS        CHAR(50),
              SALARY         REAL);''')
except sqlite3.OperationalError:
    pass
    print ("Table created successfully")
try:
    conn.execute("INSERT INTO Employee (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (1, 'Paul', 32, 'California', 20000.00 )");

    conn.execute("INSERT INTO Employee (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (2, 'Minty', 25, 'Texas', 15000.00 )");

    conn.execute("INSERT INTO Employee (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

    conn.execute("INSERT INTO Employee (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (4, 'Mark', 25, 'Zurich', 65000.00 )");

except sqlite3.IntegrityError:
    pass

conn.commit()


cursor = conn.execute("SELECT id, name, address, salary from Employee")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")
print ("Records created successfully")

conn.execute("UPDATE Employee set SALARY = 25000.00 where ID = 1")
conn.execute("UPDATE Employee set NAME = 'Apeksha' where ID = 1")
conn.execute("UPDATE Employee set NAME = 'Minty' where ID = 2")
conn.execute("UPDATE Employee set NAME = 'Teddy' where ID = 3")
conn.execute("UPDATE Employee set NAME = 'Zayn' where ID = 4")
conn.commit()


print ("TOTAL NUMBER OF ROWS UPDATED :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from Employee")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

conn.execute("DELETE from Employee where ID = 2;")
conn.commit()
print ("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from Employee")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")
conn.close()


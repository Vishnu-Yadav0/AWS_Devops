# sudo pip3 install mysql-connector-python
import mysql.connector

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host='192.168.29.4',
    user='tom',
    password='Redhat@123456',
    database='cloudbinary'
)

cursor = conn.cursor()

# Execute a query
cursor.execute('SELECT * FROM students')

# Fetch all results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the connection
conn.close()

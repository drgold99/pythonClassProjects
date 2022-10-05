# mysql_24101_foster	0 / 25 MB	
# mysql_24101_goebel	0 / 25 MB	
# mysql_24101_kapp		0 / 25 MB	
# mysql_24101_landis	0 / 25 MB	
# mysql_24101_parson	0 / 25 MB	
# mysql_24101_schultz	0 / 25 MB	
# mysql_24101_taylor	0 / 25 MB	

# python -m pip install mysql-connector-python
import mysql.connector

#Connect to the database at Winhost 'mysql_24101_sdev220'
mydb = mysql.connector.connect(
	host = "my05.winhost.com",
	user = "kapp1",
	password = "user",
	database="mysql_24101_kapp"
	)

print(mydb)
print ()

mycursor = mydb.cursor(buffered=True)

#mycursor.execute("CREATE DATABASE test")
#mycursor.execute("SHOW DATABASES")
#for x in mycursor:
#  print(x)

sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)

mycursor.execute("CREATE TABLE if not exists customers (name VARCHAR(255), address VARCHAR(255))")
  
mycursor.execute("SHOW TABLES")

for x in mycursor:
	print(x)
	
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# mydb.commit()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted.")
  
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
	('Peter', 'Lowstreet 4'),
	('Amy', 'Apple st 652'),
	('Hannah', 'Mountain 21'),
	('Michael', 'Valley 345'),
	('Sandy', 'Ocean blvd 2'),
	('Betty', 'Green Grass 1'),
	('Richard', 'Sky st 331'),
	('Susan', 'One way 98'),
	('Vicky', 'Yellow Garden 2'),
	('Ben', 'Park Lane 38'),
	('William', 'Central st 954'),
	('Chuck', 'Main Road 989'),
	('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

# View contents
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
	
# Update 
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

# Select
mycursor.execute("SELECT * FROM customers where name = 'Michael'")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)


import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","238604","testdb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * FROM courses")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

# print "Database version : %s " % data
print data
# disconnect from server
db.close()
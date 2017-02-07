#!/usr/bin/python
# Demonstrating how to connect to MySQL and execute MySQL queries in Python
# This relies on the MySQLdb library
#
# https://www.tutorialspoint.com/python/python_database_access.htm

import MySQLdb

varHost = raw_input("MySQL Host:\n")
varUser = raw_input("MySQL User:\n")
varPassword = raw_input("MySQL Password:\n")
varDB = raw_input("Database Name\n")

db = MySQLdb.connect(varHost,varUser,varPassword,varDB)
cursor = db.cursor()

# Dropping tables
cursor.execute("drop table if exists demo;")


# Creating tables
sql = """create table demo (
	first_name varchar(30),
	last_name varchar(30),
	id varchar(10));"""

cursor.execute(sql)


# Inserting values
try:
	sql = "insert into demo (first_name,last_name,id) values \
		('%s','%s','%s');" % ('John','Doe','X10001')
	cursor.execute(sql)
	db.commit()
except:
	rollback()


# Reading values
try:
	cursor.execute("select * from demo;")
	results = cursor.fetchall()
	for i in results:
		for j in i:
			print j
except:
	print "Error: unable to fetch data"


# Update values
try:
	cursor.execute("update demo set id='X10010' where id='X10001'")
	db.commit()
except:
	print "Error performing update"


# Delete values
try:
	cursor.execute("delete from demo where id='X10010'")
	db.commit()
except:
	print "Error deleting values"

db.close()

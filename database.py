
import os, sys
import sqlite3
from sqlite3 import Error
from flask import Flask
app = Flask(__name__)

def create_conn(db_file):
	""" create a database connection to a SQLite database """
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		print("Connection successful")
	except Error as e:
		print(e)

	return conn


def create_user(conn, user):
	# insert user with user data
	id 		= ''' SELECT count(id) FROM users'''
	sql 	= ''' INSERT INTO users(id, first_name, last_name, email, gender, age) VALUES(?,?,?,?,?,?)'''
	cur 	= conn.cursor()
	cur.execute(sql, user)
	return cur.lastrowid


def update_user(conn, data):
	# update user with user data
	cur 	= conn.cursor()
	cur.execute( "DELETE FROM users WHERE id = ?", (data, ) )
	conn.commit()




def select_user_by_id(conn, id):
	# get user by id
	cur 	= conn.cursor()
	cur.execute( "SELECT id, first_name, last_name, email, gender, age FROM users WHERE id = ?", (id, ) )
	# cur.execute("select * from users where id = ?", ( id, ) )
	rows 	= cur.fetchall()

	for row in rows:
		print(row)



def select_user_by_first_name(conn, name):
	# get user by first_name
	cur 	= conn.cursor()
	cur.execute( "SELECT id, first_name, last_name, email, gender, age FROM users WHERE first_name = ?", (name, ) )
	rows 	= cur.fetchall()

	for row in rows:
		print(row)


def select_user_by_last_name(conn, name):
	# get user by first_name
	cur 	= conn.cursor()
	cur.execute( "SELECT id, first_name, last_name, email, gender, age FROM users WHERE last_name = ?", (name, ) )
	rows 	= cur.fetchall()

	for row in rows:
		print(row)


def select_user_by_email(conn, email):
	# get user by first_name
	cur 	= conn.cursor()
	cur.execute( "SELECT id, first_name, last_name, email, gender, age FROM users WHERE email = ?", (email, ) )
	rows 	= cur.fetchall()

	for row in rows:
		print(row)



def select_user_by_ages(conn, start, end = -1):
	# get user by first_name
	cur 	= conn.cursor()
	if end == -1 :
		sql = ' SELECT id, first_name, last_name, email, gender, age FROM users WHERE age = ? '
		cur.execute( sql, ( start, ) )
		rows 	= cur.fetchall()
	else:
		sql = ' SELECT id, first_name, last_name, email, gender, age FROM users WHERE age BETWEEN ? = ? '
		cur.execute( sql, ( start, end, ) )
		rows 	= cur.fetchall()
	# cur.execute( sql, ( start, end, ) )
	# rows 	= cur.fetchall()

	for row in rows:
		print(row)


def select_user_by_gender(conn, gender):
	# get user by first_name
	cur 	= conn.cursor()
	cur.execute( "SELECT id, first_name, last_name, email, gender, age FROM users WHERE gender = ?", (gender, ) )
	rows 	= cur.fetchall()

	for row in rows:
		print(row)


# ============================================
# == main
def main():
	conn = create_conn( "user.db" )
	with conn:
		# print("2. Query by id")
		# id 	= 10
		# select_user_by_id( conn, id )

		# print("2. Query by email")
		# email = 'delhamr2@technorati.com'
		# select_user_by_email( conn, email )

		print("3. Query by age")
		age 	= 12
		select_user_by_ages( conn, age )



if __name__ == '__main__':
	main()




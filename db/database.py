
import os.path, sys
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


def create_user(conn, first_name = '', last_name = '', email = '', gender = '', age = 0):
	# insert user with user data
	cur 	= conn.cursor()
	# get id
	cur.execute(" SELECT count(id) FROM users ")
	user_id 		= cur.fetchone()[0]

	sql 	= ''' INSERT INTO users(id, first_name, last_name, email, gender, age) VALUES(?,?,?,?,?,?)'''

	user 	= (user_id, first_name, last_name, email, gender, age)

	conn.cursor()
	cur.execute(sql, user)
	return cur.lastrowid


def update_user(conn, id, first_name = '', last_name = '', email = '', gender = '', age = 0):
	# update user with user data
	sql 	= ''' UPDATE users 
					SET 
						first_name = ?,
						last_name = ?,
						email = ?,
						gender = ?,
						age = ?
					WHERE id = ?
						'''
	user 	= (first_name, last_name, email, gender, age, id)

	cur 	= conn.cursor()
	cur.execute(sql, user)
	conn.commit()
	cur.close()



def delete_user(conn, id):
	# delete user with user id
	sql 	= ''' DELETE FROM users WHERE id = ? '''

	cur 	= conn.cursor()
	cur.execute(sql, ( id, ))
	conn.commit()
	cur.close()



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
	if end < 0 :
		sql = " SELECT id, first_name, last_name, email, gender, age FROM users WHERE age = ? "
		cur.execute( sql, ( start, ) )
		rows 	= cur.fetchall()
	else:
		sql = " SELECT id, first_name, last_name, email, gender, age FROM users WHERE age BETWEEN ? AND ? "
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

	dir 	= os.path.dirname( os.path.abspath(__file__))
	db_path = os.path.join( dir, "user.db" )
	conn = create_conn( db_path )
	with conn:
		# print("2. Query by id")
		# id 	= 10
		# select_user_by_id( conn, id )

		# print("2. Query by email")
		# email = 'delhamr2@technorati.com'
		# select_user_by_email( conn, email )

		# print("3. Query by age")
		# age 	= 15
		# end 	= 18
		# select_user_by_ages( conn, age, 18 )

		# print("4. Insert user")
		# create_user(conn, first_name = 'beerz', last_name = 'srzn', email = 'beerz@mail.com', gender = 'female', age = 30)

		# update_user(conn, id = 1000, first_name = 'beerz', last_name = 'srzn', email = 'beerz@mail.com', gender = 'female', age = 27)

		# select_user_by_email( conn, "beerz@mail.com" )
		delete_user(conn, 1000)



if __name__ == '__main__':
	main()




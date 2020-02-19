
import os.path
import sys
import json
import sqlite3
from sqlite3 import Error
from flask import Flask, jsonify, g, request, escape, make_response
from flask_cors import CORS
app = Flask(__name__)

# CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

dir 		= os.path.dirname( os.path.abspath(__file__))
db_path 	= os.path.join( dir, "user.db" )


def create_conn():
	""" create a database connection to a SQLite database """
	db 	= getattr(g, '_database', None)
	if db is None:
		db 	= g._database 	= sqlite3.connect( db_path )
	return db


@app.teardown_appcontext
def close_conn(exception):
	db 	= getattr(g, '_database', None)
	if db is not None:
		db.close()



@app.route( '/api/v1/list', methods = ["GET"] )
def home():

	# args
	limit 	= request.args.get( "limit", 20 )
	offset 	= request.args.get( "offset", 0 )

	cur 	= create_conn().cursor()
	res 	= cur.execute("SELECT id, first_name, last_name, email, gender, age FROM users LIMIT ? OFFSET ? ", ( limit, offset, ) )
	rows 	= cur.fetchall()
	cur.close()

	result 	= []
	for row in rows:
		data = {
			'id': 			row[0],
			'first_name': 	row[1],
			'last_name': 	row[2],
			'email': 		row[3],
			'gender': 		row[4],
			'age': 			row[5]
		}
		result.append( data )
	
	
	return jsonify({ 'data': result })


@app.route('/api/v1/test', methods = ["GET"])
def list_users():
	first_name 		= request.args.getlist("first_name" )
	last_name 		= request.args.getlist("last_name")

	data 	= {
		"first_name": first_name,
		"last_name": last_name
	}

	return jsonify( data=data )


@app.route('/api/v1/users', methods = ["GET"])
def get_users():
	# get users with args
	cur 	= create_conn().cursor()

	id 			= request.args.get( "id", None )
	first_name 	= request.args.get( "first_name", None )
	last_name 	= request.args.get( "last_name", None )
	email 		= request.args.get( "email", None )
	gender 		= request.args.get( "gender", None )
	age 		= request.args.get( "age", None )

	gt 			= request.args.get( "gt", None )
	# lt 			= request.args.get( "lt", None )

	result 		= []

	if id != None:
		# select users by id
		cur.execute( "SELECT id, first_name, last_name, email, gender, age FROM users WHERE id = ?", (id, ) )

	if first_name != None:
		# select users by fist_name
		cur.execute( "SELECT id, first_name, last_name, email, gender, age FROM users WHERE first_name = ?", (first_name, ) )

	if last_name != None:
		# select users by last_name
		cur.execute( "SELECT id, first_name, last_name, email, gender, age FROM users WHERE last_name = ?", (last_name, ) )

	if email != None:
		# select users by email
		cur.execute( "SELECT id, first_name, last_name, email, gender, age FROM users WHERE email = ?", (email, ) )

	if gender != None:
		# select users by gender
		cur.execute( "SELECT id, first_name, last_name, email, gender, age FROM users WHERE gender = ?", (gender, ) )

	if age != None:
		# select users by age
		cur.execute( "SELECT id, first_name, last_name, email, gender, age FROM users WHERE age = ?", (age, ) )

	if gt != None and age != None:
		# select users by age range
		cur.execute( "SELECT id, first_name, last_name, email, gender, age FROM users WHERE age BETWEEN ? AND ?", (age, gt) )

	rows 	= cur.fetchall()
	for row in rows:
		data = {
			'id': 			row[0],
			'first_name': 	row[1],
			'last_name': 	row[2],
			'email': 		row[3],
			'gender': 		row[4],
			'age': 			row[5]
		}
		result.append( data )
	
	
	return jsonify({ 'data': result })
	


@app.route('/api/v1/users', methods = [ "POST" ])
def create_user():
	# insert user with user data
	cur 	= create_conn().cursor()

	first_name 	= request.args.get( "first_name", None )
	last_name 	= request.args.get( "last_name", None )
	email 		= request.args.get( "email", None )
	gender 		= request.args.get( "gender", None )
	age 		= request.args.get( "age", None )

	# get id
	cur.execute(" SELECT count(id) FROM users ")
	user_id 		= cur.fetchone()[0]

	sql 	= ''' INSERT INTO users(id, first_name, last_name, email, gender, age) VALUES(?,?,?,?,?,?)'''

	user 	= (user_id, first_name, last_name, email, gender, age)

	cur.execute(sql, user)
	return cur.lastrowid


@app.route('/api/v1/users', methods = [ "PUT" ])
def update_users():
	# update user with user data
	cur 	= create_conn().cursor()

	id 			= request.args.get( "id", None )
	first_name 	= request.args.get( "first_name", None )
	last_name 	= request.args.get( "last_name", None )
	email 		= request.args.get( "email", None )
	gender 		= request.args.get( "gender", None )
	age 		= request.args.get( "age", None )

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

	result 	= cur.execute(sql, user)
	create_conn().commit()
	cur.close()

	return make_response( jsonify({"data": result}), 200 )


@app.route('/api/v1/users', methods = [ "DELETE" ])
def delete_user():
	# delete user with user id
	cur 		= create_conn().cursor()

	sql 		= ''' DELETE FROM users WHERE id = ? '''

	id 			= request.args.get( "id", None )

	result 	= cur.execute(sql, ( id, ))
	create_conn().commit()
	cur.close()

	return make_response( jsonify({"data": result}), 200 )



if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=True)

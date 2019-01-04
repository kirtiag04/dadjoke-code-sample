#!flask/bin/python
from app import app
from flask import render_template, jsonify, request
import requests
from app import db
from .models import User
import sqlite3 as sql

""" Route to display homepage """
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


""" Route to generate a random joke """
@app.route('/generate', methods=['GET'])
def generate():
	# Prepare API get request for generating random joke
    headers = {
	    'Accept': 'application/json',
	}
    r = requests.get('https://icanhazdadjoke.com/', headers=headers)
    
    json_obj = r.json()
    print json_obj
    return jsonify(result=json_obj['joke'])


""" Route to save user opinion to SQLite database """
@app.route('/save-opinion', methods=['POST'])
def save_opinion():
	joke = request.form['joke']
	opinion = request.form['opinion']
	print joke, opinion

	# Connection to the database
	con = sql.connect("app.db")
	cur = con.cursor()

	# Check if opinion on the joke already exists
	cur.execute("SELECT id FROM user WHERE joke=?", (joke,))
	row = cur.fetchone()

	# If yes, update the opinion otherwise
	# insert new one
	if row is None :

		# Adding the user opinion to the database
		u = User(username="John", joke=joke, opinion=opinion)
		db.session.add(u)
		db.session.commit()
	else:

		# Update the user opinion
		uid = row[0]
		cur.execute("UPDATE user SET opinion=? WHERE id=?", (opinion, uid))
		con.commit()
	return ''


""" Route to display summary page """
@app.route('/summary')
def summary():
	# Connecting to the database
	con = sql.connect("app.db")
	con.row_factory = sql.Row
	cur = con.cursor()

	# Fetching the opinions of the user
	cur.execute("SELECT * FROM user WHERE username='John';")
	rows = cur.fetchall()
	print rows

	return render_template('summaries.html', rows=rows)


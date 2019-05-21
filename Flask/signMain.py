from flask import Flask, request, render_template, session, redirect, url_for, jsonify
import pymongo
from datetime import timedelta

mongo_url = 'mongodb+srv://Jieun:kia2009^^*@cluster0-m07mo.mongodb.net/test?retryWrites=true'
client = pymongo.MongoClient(mongo_url)
db = pymongo.database.Database(client, 'Cluster0')
users = pymongo.collection.Collection(db, 'Users')
books = pymongo.collection.Collection(db, 'Books')

app = Flask(__name__)
app.secret_key = "1367"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':
		if not 'userEmail' in session:
			return render_template('signup.html')
		return render_template('welcome.html', info = session['userEmail'])
	elif request.method == 'POST':
		if not 'userEmail' in session:
			users.insert_one(request.form.to_dict(flat='true'))
			session['userEmail'] = request.form['userEmail']
			return render_template('welcome.html', info = session['userEmail'])
		return render_template('welcome.html', info = session['userEmail'])
@app.route('/signin', methods=['GET', 'POST'])
def signin():
	if request.method == 'GET':
		if 'userEmail' in session:
			return render_template('welcome.html', info = session['userEmail'])
		return render_template('signin.html')
	elif request.method == 'POST':
		if users.find_one(request.form.to_dict(flat='true'))is not None:
			session['userEmail'] = request.form['userEmail']
			return render_template('welcome.html', info=session['userEmail'])
		return redirect(url_for('signin'))
@app.route('/logout')
def logout():
	if session['userEmail']:
		session.pop('userEmail')
		return redirect(url_for('signin'))
	return redirect(url_for('signin'))
@app.before_request
def make_session_permanent():
	session.permanent = True
	app.permanent_session_lifetime = timedelta(minutes=60)

@app.route('/register')
def register():
	if 'userEmail' in session:
		return render_template('books.html')
	return redirect(url_for('signin'))
@app.route('/books',methods=['GET','POST'])
def result():
	if request.method == 'POST':
		data = request.form.to_dict(flat='true')
		books.insert_one({"name":data['name'],"price": data['price'], "writer":data['writer'], "publisher":data['publisher']})
	if 'userEmail' in session:
		return render_template('bookInfo.html', result = books.find({}))
	return redirect(url_for('signin'))	

if __name__ =='__main__':
	app.run(host = '0.0.0.0', port = 5000)

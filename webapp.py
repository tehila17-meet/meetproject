from flask import Flask, render_template,url_for,flash,redirect,g,request
from DB import *

from flask import session as login_session
from functools import wraps
import os

from werkzeug.utils import secure_filename
import random
from random import choice, sample
UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "MY_SUPER_SECRET_KEY"

engine = create_engine('sqlite:///fizzBuzz.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()

def login_r(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in login_session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login'))

    return wrap


@app.route('/',methods = ['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else: 
		user_name = request.form['name']
		psd = request.form['password']
		users = session.query(User).filter_by(name = user_name).first()
	error = None
	if request.method == 'POST':

		if users is None or users.password != psd:
			error = "Username or password incorrect"
		else:
			login_session['logged_in'] = True
			login_session['fullname'] = user_name

			return redirect(url_for('places'))
	return render_template('login.html',error = error)


@app.route('/signup',methods = ['GET','POST'])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')
	else:
		fullname = request.form['name']
		pa = request.form['password']
		new_user = User(name = fullname,password=pa)
		session.add(new_user)
		session.commit()
		
	return redirect(url_for('login'))

@app.route('/search', methods = ['GET','POST'])
def search():
	if request.method == 'POST':
		name_place = request.form['search']
		print(name_place)
		places = session.query(Places).all()
		for p in places:
			if name_place == p.name:
				a = p.id
				#return render_template('diveplace.html',place_id = a)
				return redirect(url_for('diveplace',place_id =a))
			else:
				return redirect(url_for('places'))
@app.route('/search1', methods = ['GET','POST'])
def search1():
	if request.method == 'POST':
		name_place = request.form['search']
		print(name_place)
		places = session.query(Boats).all()
		for p in places:
			if name_place == p.name:
				a = p.id
				#return render_template('diveplace.html',place_id = a)
				return redirect(url_for('boatplace',boat_id =a))
			else:
				return redirect(url_for('boats'))
	

@app.route('/profile/<int:user_id>',methods = ['GET','POST'])
@login_r

def profile(user_id):
	if request.method == 'GET':
		user = session.query(User).filter_by(name= login_session['fullname']).first()
		print("we are here")
		print(user.places)
		places = user.places
		return render_template('profile.html',user=user)
	else:
		user = session.query(User).filter_by(name= login_session['fullname']).first()
		for p in user.places:
			print p.name
			user.places.remove(p)
		session.commit()
		return redirect(url_for('profile',user_id =user.id))


@app.route('/places')
@login_r
def places():
	
	
		place = session.query(Places).all()
		user = session.query(User).filter_by(name= login_session['fullname']).first()
		return render_template('places.html', place = place,user=user)


	
@app.route('/boats')
@login_r
def boats():
	boat = session.query(Boats).all()
	user = session.query(User).filter_by(name= login_session['fullname']).first()
	return render_template('boats.html', boat = boat,user=user)


@app.route("/diveplace/<int:place_id>" ,methods = ['GET','POST'])
@login_r
def diveplace(place_id):
	
	dive = session.query(Places).filter_by(id = place_id).first()
	review = session.query(Reviews).all()
	user = session.query(User).filter_by(name = login_session['fullname']).first()
	if request.method == "POST":
		new_review = request.form['review']
		star = request.form['star']


		
		r= Reviews(review = new_review, star = star, what_place = place_id)
		session.add(r)
		session.commit()
		return redirect(url_for('diveplace',place_id = place_id, user=user))
	return render_template('diveplace.html', dive = dive, review = review,user=user,place_id=place_id)
		

@app.route('/divingplace/fav/<int:place_id>',methods = ['GET','POST'])
def fav(place_id):		
		user = session.query(User).filter_by(name = login_session['fullname']).first()
		new_favorite=session.query(Places).filter_by(id=place_id).first()
		
		user.places.append(new_favorite)
		new_favorite.user.append(user)
		print("we made it!")
		session.commit()
		return redirect(url_for('diveplace',place_id = place_id, user=user))

@app.route("/boatplace/<int:boat_id>" ,methods = ['GET','POST'])

@login_r
def boatplace(boat_id):
	
	ship = session.query(Boats).filter_by(id = boat_id).first()
	review = session.query(Reviews).all()
	user = session.query(User).first()
	if request.method == "POST":
		new_review = request.form['review']
		star = request.form['star']


		
		r= Reviews(review = new_review, star = star, what_place = boat_id)
		session.add(r)
		session.commit()
		
		

		return redirect(url_for('boatplace',boat_id = boat_id, star=star))
	
	return render_template('boatplace.html', ship = ship, review = review,user=user)
'''
@app.route('/fav/<int:place_id>',methods= ['GET','POST'])
def fav(place_id):
	user = session.query(User).filter_by(name = login_session['fullname']).first()
	if request.method == 'GET':
		dive = session.query(User).filter_by(id = place_id).first()
		return render_template('profile.html', place = place)

	else:
		
		new_favorite=session.query(User).filter_by(id=place_id).first()
		
		user.places.append(new_favorite)
		new_favorite.places.append(user)
		print("we made it!")
		session.commit()
		return render_template('profile,html',user = user)
	
	





@app.route('/fav', methods = ['GET','POST'])
def fav():

	new_favorite=session.query(Places).filter_by(id=place_id).first()
	
	user.my_favs.append(new_favorite)
	new_favorite.my_favs.append(user)
	session.commit()
	return render_template('places.html')


@app.route("/addplace", methods = ['GET','POST'])

def addplace():
	if request.method == 'POST':
	
		name = request.form['place']
		description = request.form['description']
		location = request.form['location']
		#photo1 = request.form['file1']
		#photo2  = request.form['file2']
		#photo3 = request.form['file3']
		newDiving = Places(name = name, description = description, location=location)
		session.add(newDiving)
		session.commit()
	return redirect(url_for('places'))
#def fav():
'''

'''		
@app.route('/addreview',methods = ['GET','POST'])
def addreview():
	if request.method == 'POST':
		review = request.form['review']
		star = request.form['star']
		newReview = Reviews(review = review, star = star, what_place = place.id)
		session.add(newReview)
		session.commit()
		return redirect(url_for('places'))
	else:
		return render_template('diveplace.html',dive = dive, review = review)
	if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('uploaded_file',
                                    filename=filename))
'''
@app.route('/random')
def random():
 
	places = session.query(Places).all()
	print(places)
	b = choice(places)
	c = b.id 
	return redirect(url_for('diveplace',place_id = c ))
@app.route('/random1')
def random1():
 
	boats = session.query(Boats).all()
	
	d = choice(boats)
	e = d.id 
	return redirect(url_for('boatplace',boat_id = e ))

@app.route('/logout')
@login_r
def logout():
	login_session.pop('logged_in',None)
	
	return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

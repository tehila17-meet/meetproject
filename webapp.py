from flask import Flask, render_template,url_for,flash,redirect,g,request
from DB import *
from flask import session as login_session
from functools import wraps
import os
from werkzeug.utils import secure_filename
import random
from random import choice, sample



app = Flask(__name__)

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
		places = session.query(Places).filter(Places.name.contains(name_place.lower())).first()
		place_id = places.id
				#return render_template('diveplace.html',place_id = a)
		return redirect(url_for('diveplace',place_id = places.id))
			
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
@app.route('/about')
@login_r
def about():
	return render_template('aboutme.html')

@app.route('/profile/<int:user_id>',methods = ['GET','POST'])
@login_r

def profile(user_id):
	if request.method == 'GET':
		user = session.query(User).filter_by(name= login_session['fullname']).first()
		
		places = user.places_been
		all_places = session.query(Places).all()
		counter = 0
		counter1 = 0
		for place in all_places:
			counter += 1
	
		for fav in places:
			counter1 += 1
		
		o = counter1 * 100
		s = o / counter
		
		
		return render_template('profile.html',user=user,s=s)


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
		
@app.route('/divingplace/been/<int:place_id>',methods = ['GET','POST'])
def been(place_id):
		
		user = session.query(User).filter_by(name = login_session['fullname']).first()
		new_been=session.query(Places).filter_by(id=place_id).first()
		
		user.places_been.append(new_been)
		new_been.user_been.append(user)
		
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
		
		

		return redirect(url_for('boatplace',boat_id = boat_id, star=star,ship = ship))
	
	return render_template('boatplace.html', ship = ship, review = review,user=user)

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

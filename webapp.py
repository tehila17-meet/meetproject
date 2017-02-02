from flask import Flask, render_template,url_for,flash,redirect,g,request
from DB import *

from flask import session as login_session
from functools import wraps
import os

from werkzeug.utils import secure_filename

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
			login_session['fullname'] = True

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

@app.route('/profile')
@login_r

def profile():
	
		user = session.query(User).filter_by(name = login_session['fullname']).first()
		favorite = session.query(Favs).all()
		return render_template('profile.html',user=user,favorite=favorite)


@app.route('/places')
@login_r
def places():
	
		place = session.query(Places).all()
		user = session.query(User).filter_by(name= login_session['fullname']).first()
		return render_template('places.html', place = place,user=user)
	


@app.route("/diveplace/<int:place_id>" ,methods = ['GET','POST'])
@login_r
def diveplace(place_id):
	
	dive = session.query(Places).filter_by(id = place_id).first()
	review = session.query(Reviews).all()
	if request.method == "POST":
		new_review = request.form['review']
		star = request.form['star']
		
		r= Reviews(review = new_review, star = star, what_place = place_id)
		session.add(r)
		session.commit()
		
		new_favorite = Favs(place = place_id,name = dive.name)
		session.add(new_favorite)
		session.commit()
		

		return redirect(url_for('diveplace',place_id = place_id))
	global x 
	x = 0
	for i in review:
		if i.what_place == place_id:
			x+=1
	
	print(x)

	return render_template('diveplace.html', dive = dive, review = review,x=x)
'''

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
@app.route('/logout')
@login_r
def logout():
	login_session.pop('logged_in',None)
	
	return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

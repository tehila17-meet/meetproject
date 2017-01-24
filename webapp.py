from flask import Flask, render_template,url_for,flash,redirect,g,request
from DB import *

from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

engine = create_engine('sqlite:///fizzBuzz.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()

@app.route('/')
@app.route('/places')
def places():
	place = session.query(Places).all()
	return render_template('places.html', place = place)


@app.route("/diveplace/<int:place_id>" ,methods = ['GET','POST'])
def diveplace(place_id):
	
	dive = session.query(Places).filter_by(id = place_id).first()

	if request.method == 'GET':
		review = session.query(Reviews).all()
		shops = session.query(Diveshops).all()
		
	else:
		new_review = request.form['review']
		star = request.form['star']
		
		r= Reviews(review= new_review, star = star, what_place = place_id)
		
		session.add(r)
		session.commit()
		shopname = request.form['shopname']
		price = request.form['price']
		address = request.form['address']

		s = Diveshops(shop_name = shopname,price = price,address = address, what_place = place_id)
		
		session.add(s)
		session.commit()
		return render_template(url_for('diveplace', place_id = dive.id))
		
	return render_template('diveplace.html', dive = dive, review = review, shops = shops)
	
	
		
	


@app.route("/addplace", methods = ['GET','POST'])
def addplace():

	if request.method == 'POST':
		name = request.form['place']
		description = request.form['description']
		location = request.form['location']
		newDiving = Places(name = name, description = description, location=location)
		session.add(newDiving)
		session.commit()
		return redirect(url_for('places'))
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
'''
if __name__ == '__main__':
    app.run(debug=True)

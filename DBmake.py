from DB import *


engine = create_engine('sqlite:///fizzBuzz.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()


tehila = User(name ="tehila pelled",password="123")
eilat = Places(name = "Red sea", location="Israel, Eilat",description="The corals are beautiful!",photo1 = "https://www.supercoolbeaches.com/sites/default/files/coral-beach-eilat.jpg",
	photo2 = "https://upload.wikimedia.org/wikipedia/commons/8/8b/Gulf_of_Eilat_(Red_Sea)_coral_reefs.jpg",
	photo3 = "http://www.aqua-sport.com/_Uploads/dbsArticles/17.jpg")
zanzibar = Places(name = "zanzibar", location="Tanzania, Zanzibar", description="wow",photo1 = "https://www.absoluteafrica.com/trip_pix/Kendwa%20328.jpg",
	photo2 = "http://www.thebestbeach.com.au/Images/zanzibar-beach.jpg",
	photo3= "http://www.scubafishzanzibar.com/img/scubafish.jpg")
review1 = Reviews(review = "omg best dive ever", star = 5)
deepsiam = Diveshops(shop_name = "Deep Siam", address = "123", price = "200")
aqua = Diveshops(shop_name = "Aqua", address = "223", price = "300")
session.add(tehila)
session.add(deepsiam)
session.add(aqua)
session.add(zanzibar)
session.add(eilat)
session.add(review1)
session.commit()

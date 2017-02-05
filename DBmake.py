from DB import *


engine = create_engine('sqlite:///fizzBuzz.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()
	

tehila = User(name ="tehila pelled",password="123")
eilat = Places(name = "Red sea", location="Israel, Eilat",description="The corals are beautiful!",photo1 = "https://www.supercoolbeaches.com/sites/default/files/coral-beach-eilat.jpg",
	photo2 = "https://upload.wikimedia.org/wikipedia/commons/8/8b/Gulf_of_Eilat_(Red_Sea)_coral_reefs.jpg",
	photo3 = "http://www.aqua-sport.com/_Uploads/dbsArticles/17.jpg",
	best_time = "", diveshop1="Deep siam",ds1price = "200 per rental", diveshop2="Aqua sport",
	ds2price="250 per rental", narley_fish="abu nafcha")
zanzibar = Places(name = "zanzibar", location="Tanzania, Zanzibar", description="wow"
	,photo1 = "https://www.absoluteafrica.com/trip_pix/Kendwa%20328.jpg",
	photo2 = "http://www.thebestbeach.com.au/Images/zanzibar-beach.jpg",
	photo3= "http://www.scubafishzanzibar.com/img/scubafish.jpg",best_time="",
	 diveshop1="",diveshop2="", ds2price="",ds1price="",narley_fish="Huge turtles and reef sharks")
mexico = Places(name="mexico",location="mexico reef",
 description="ahhh", photo1="http://cozumelcruiseexcursions.net/images/discover-scuba-cozumel/cozumel-introductory-to-scuba-diving.jpg"
	,photo2 = "http://www.aluxdiver.com/cenotes-riviera-maya/wp-content/uploads/2011/07/chac-kukulkan.jpg",
	photo3 = "https://www.diveaventuras.com/wp-content/uploads/2016/03/whaleshark-diving-mexico-playa-1650x650.jpg",
	best_time="", diveshop1="",diveshop2="", ds2price="",ds1price="",narley_fish="Watch out from the great whites!")
maldives = Places(name="maldive islands",location="maldives",description="The water is so clear", photo1= "http://www.diving-world.com/imagescompressed/maldives/MALDIVE3.jpg",
	photo2 = "https://i.ytimg.com/vi/fqzENTUQNi0/maxresdefault.jpg",photo3 = "http://www.lilybeachmaldives.com/wp-content/uploads/2015/06/Lily-Beach-front-page-slide-01.jpg", 
	best_time="", diveshop1="prodivers",diveshop2="", ds2price="",ds1price="",narley_fish="")
indonesia = Places(name = "Indonesia",location="indonesia,asia",description="crazy underwater life", photo1= "http://www.diving-world.com/imagescompressed/maldives/MALDIVE3.jpg",
	photo2 = "http://images.travelpod.com/tripwow/photos/ta-00d2-361c-f30b/dream-beach-indonesia-indonesia+12958113281-tpfil02aw-17900.jpg",photo3 = "", best_time="", diveshop1="",diveshop2="", ds2price="",ds1price="",narley_fish="") 
review1 = Reviews(review = "omg best dive ever", star = 5)


session.add(tehila)
session.add(indonesia)
session.add(zanzibar)
session.add(eilat)
session.add(mexico)
session.add(maldives)
session.add(review1)
session.commit()

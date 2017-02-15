from DB import *

engine = create_engine('postgres://dcksenyhfyqqkm:bdce4b8ad60ef235a6f074e5c5b27c5d1f3e2bbaa078cf8fe3d9f9fe7f84f635@ec2-23-23-223-2.compute-1.amazonaws.com:5432/d5tc1uq8kg2535')

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

USS = Boats(name = "USS Vandenberg", location = "Florida Keys,USA", boat_history = "From world war 2",photo1 = "http://navy.memorieshop.com/VanDenburg/At-Sea.jpg",
	photo2 = "http://www.whats-at-florida-keys.com/images/vandenberg1.gif",photo3 = "http://media0.trover.com/T/536a7edbd809d8615800001f/fixedw_large_4x.jpg",	description = "The Vandenberg rests 7 miles south of Key West Florida. 10 stories high, depth ranges from 39 - 150. visibility ranges from 19 - 98ft")
	
Thistlegorm = Boats(name = "Thistlegorm",location= "Egyptian Red Sea",boat_history = "The SS Thistlegorm was a British armed Merchant Navy ship built in 1940 by Joseph Thompson & Son in Sunderland, England. She was sunk on 6 October 1941 near Ras Muhammad in the Red Sea and is now a well known diving site.",
	photo1 = "http://www.cameldive.com/siteimages/thistlegorm.jpg",
	photo2 = "https://upload.wikimedia.org/wikipedia/commons/8/8c/Thistlegorm_train_parts_minus_red_edit.jpg",photo3 = "http://www.scubatravel.co.uk/photos/socialmedia/thistlegorm-wheels-shells.jpg", description = "Depth: 18 - 30")
Ghiannis = Boats(name = "Ghiannis D",location="north of Sha'ab Abu Nuhas reef", boat_history="greek boat",
	photo1 = "http://c8.alamy.com/comp/B3P954/a-view-of-the-superstructure-of-the-giannis-d-shipwreck-at-shaab-abu-B3P954.jpg",
	photo2 = "https://c1.staticflickr.com/3/2541/4206002602_5dcb20153d_b.jpg", 
	photo3 = "http://cassiopeiasafari.com/wp-content/uploads/2009/11/Giannis_D_nose.jpg", description="depth: 23m")
Kingston = Boats(name = "Kingston", location= "red sea",boat_history="The Kingston ran into the reef at Shag Rock in 1881, with no loss of life. She lies on a sloping reef wall in 4-19 m of water.",
	photo1 ="http://divertrek.com/wp-content/uploads/2016/10/Kingston_Diving-5.jpg ",
	photo2 = "https://lh3.googleusercontent.com/Xz089n1WKwqRFA2Zqp6P0urQqx4Cs8sLIpJdUY2JwELdP29gmcu0zNfKzhXTHvA02JUmIF9K4tywYg=w293-h220-rw",
	photo3="https://lh3.googleusercontent.com/5O4eAsgUkBCvGZCn5U1Y7xyyp3DOdsXIBAbPXSfdp9qR3UZDK8M5Yk3Z70_XGur6swqbcfsWgJwV1g=w165-h220-rw",description ="depth 19m")
session.add(tehila)
session.add(indonesia)
session.add(zanzibar)
session.add(eilat)
session.add(mexico)
session.add(maldives)
session.add(Ghiannis)
session.add(Kingston)
session.add(Thistlegorm)
session.add(review1)
session.add(USS)
session.commit()

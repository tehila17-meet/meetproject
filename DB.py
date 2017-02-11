from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
from passlib.apps import custom_app_context as pwd_context
import random, string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

Base = declarative_base()

'''	
favorite_association = Table('association', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('places_id', Integer, ForeignKey('places.id')))

my_favs = relationship("User", 
							  secondary=favorite_association, 
							  primaryjoin=id==favorite_association.c.user_id,
							  secondaryjoin=id==favorite_association.c.places_id,
							  lazy=True)
'''
favorite_association = Table('association', Base.metadata,
	Column('user_id', Integer, ForeignKey('user.id')),
	Column('places_id', Integer, ForeignKey('places.id'))
	)
favorite_association1 = Table('association1', Base.metadata,
	Column('user_id', Integer, ForeignKey('user.id')),
	Column('boats_id', Integer, ForeignKey('boats.id'))
	)
class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	password= Column(String)
	places = relationship("Places",
		secondary=favorite_association,
		back_populates = "user")
	boats = relationship("Boats",
		secondary=favorite_association1,
		back_populates = "user")
	



class Places(Base):
	__tablename__ = 'places'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	location = Column(String)
	description = Column(String)
	photo1 = Column(String)
	photo2 = Column(String)
	photo3 = Column(String)
	best_time = Column(String)
	diveshop1 = Column(String)
	ds1price = Column(Integer)
	diveshop2 = Column(String)
	ds2price = Column(Integer)
	narley_fish = Column(String)
	user = relationship(
		"User",
		secondary=favorite_association,
		back_populates="places")

class Boats(Base):
	__tablename__ = 'boats'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	location = Column(String) 
	boat_history = Column(String)
	photo1 = Column(String)
	photo2 = Column(String)
	photo3 = Column(String)
	description = Column(String)
	user = relationship(
		"User",
		secondary=favorite_association1,
		back_populates="boats")

class Reefs(Base):
	__tablename__ = 'reefs'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	location = Column(String)
	photo1 = Column(String)
	photo2 = Column(String)
	photo3 = Column(String)





class Reviews(Base):
	__tablename__ = 'reviews'
	id = Column(Integer, primary_key = True)
	what_place = Column(Integer)
	review = Column(String)
	star = Column(Integer)
	name= Column(String)


engine = create_engine('sqlite:///fizzBuzz.db')
#engine = create_engine('postgres:///d5tc1uq8kg2535.db')
Base.metadata.create_all(engine)

	

from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
from passlib.apps import custom_app_context as pwd_context
import random, string

from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

Base = declarative_base()

favorite_association = Table('association', Base.metadata,
	Column('user_id', Integer, ForeignKey('user.id')),
	Column('places_id', Integer, ForeignKey('places.id'))
	)
been_association = Table('been_association', Base.metadata,
	Column('user_been_id', Integer, ForeignKey('user.id')),
	Column('places_been_id', Integer, ForeignKey('places.id'))
	)


class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key = True)
	
	name = Column(String)
	password= Column(String)
	places = relationship("Places",
		secondary=favorite_association,
		back_populates = "user")
	places_been = relationship("Places",
		secondary=been_association,
		back_populates = "user_been")


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
	user_been = relationship(
		"User",
		secondary=been_association,
		back_populates="places_been")


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
	
	

class Reviews(Base):
	__tablename__ = 'reviews'
	id = Column(Integer, primary_key = True)
	what_place = Column(Integer)
	review = Column(String)
	star = Column(Integer)
	name= Column(String)

engine = create_engine('postgres://dcksenyhfyqqkm:bdce4b8ad60ef235a6f074e5c5b27c5d1f3e2bbaa078cf8fe3d9f9fe7f84f635@ec2-23-23-223-2.compute-1.amazonaws.com:5432/d5tc1uq8kg2535')

#engine = create_engine('sqlite:///fizzBuzz.db')

Base.metadata.create_all(engine)

	

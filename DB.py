from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
from passlib.apps import custom_app_context as pwd_context
import random, string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

Base = declarative_base()

class Places(Base):
	__tablename__ = 'places'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	location = Column(String)
	description = Column(String)
	photo1 = Column(String)
	photo2 = Column(String)
	photo3 = Column(String)

class Reviews(Base):
	__tablename__ = 'reviews'
	id = Column(Integer, primary_key = True)
	what_place = Column(Integer)
	review = Column(String)
	star = Column(Integer)
class Diveshops(Base):
	__tablename__ = "diveshops"
	id = Column(Integer, primary_key= True)
	what_place = Column(Integer)
	shop_name = Column(String)
	address = Column(String)
	price = Column(String)


engine = create_engine('sqlite:///fizzBuzz.db')
Base.metadata.create_all(engine)

	

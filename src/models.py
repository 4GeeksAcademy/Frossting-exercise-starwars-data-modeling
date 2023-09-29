import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(256), nullable=False, unique=True)
    

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    full_name = Column(String(300), nullable=False)
    eye_color = Column(String(30), nullable=True)
    hair_color = Column(String(30), nullable=True)                  

class Planets(Base): 
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(180), nullable=False)
    atmosphere = Column(Boolean, nullable = False)

class Vehicles(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    name = Column(String(180), nullable=False)
    model = Column(String(180), nullable=False)
    manufacturer = Column(String(300), nullable=False)    

class Favorite(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)

    User_id = Column(Integer,ForeignKey('user.id'), nullable=False)
    user=relationship(User)

    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    character = relationship(Characters)

    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    planet = relationship(Planets)

    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=True)
    vehicle = relationship(Vehicles)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

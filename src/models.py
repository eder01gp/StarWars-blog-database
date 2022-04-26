import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    userName = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(250))
    population = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer)
    """ created = Column(DateTime) """ 
    """ edited = Column(DateTime)  """
    url = Column(String(250))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(Integer)
    gender = Column(String(250))
    """ created = Column(DateTime)  """
    """ edited = Column(DateTime)  """
    name = Column(String(250))
    homeworld = Column(String(250))
    url = Column(String(250))

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    vehicle_class = Column(String(250))
    maufacturer = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(250))
    films = Column(String(250))
    pilots = Column(String(250))
    """ created = Column(DateTime)  """
    """ edited = Column(DateTime)  """
    name = Column(String(250))
    url = Column(String(250))

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    favorite_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    favorite_char = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    favorite_planet = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    favorite_vehicle = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(Vehicle)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

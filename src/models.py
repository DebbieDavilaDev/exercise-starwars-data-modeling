import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)

    user_favorites = relationship("User_favorites", back_populates="user")
    
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    favorite = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    entitytype = Column(String(250), nullable=False)
    planetid = Column(String(250), nullable=False)
    characterid = Column(String(250), nullable=False)
    
    

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)

    user_favorites = relationship("User_favorites", back_populates="character")

    BirthYear = Column(String(250), nullable=False)
    EyeColor = Column(String(250), nullable=False)
    Homeworld = Column(String(250), nullable=False)
    Films = Column(String(250), nullable=False)
    Species = Column(String(250), nullable=False)
    Height = Column(String(250), nullable=False)
    
    mediatype = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    entity_id = Column(Integer, ForeignKey('favorites.id')) 
    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)

    user_favorites = relationship("User_favorites", back_populates="planets")

    BirthYear = Column(String(250), nullable=False)
    Films = Column(String(250), nullable=False)
    HabitantSpecies = Column(String(250), nullable=False)
    Size = Column(String(250), nullable=False)
    
    mediatype = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id')) 




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

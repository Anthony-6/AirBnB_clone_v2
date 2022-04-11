#!/usr/bin/python3
"""This module defines a class User"""
from msilib.schema import File
from tkinter import CASCADE
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'user'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship('Place', backref="user",
                          cascade="all, delete_orphan")
    reviews = relationship('Review', backref="user",
                           cascade="all, delete_orphan")

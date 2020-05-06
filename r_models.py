'''
Mini Project:
I am a multi-restaurant owner, and need to make a bookeeping system
The following models:
Restaurant:
	id
	number_of_tables
	location
Table:
	id:
	restaurant_id: Restaurant
	number_of_seats
	position: String
Customer:
	id:
	date_of_visit:
	table_id: -> Find the restaurant by looking in the Table table
	consumption: Integer $$$
Using:
	Pymongo
OR
	Pysqlalchemy
Be able to Create Resaturant:
		   Update Restaurant
		   Delete Restaurant and implicit tables
		  	For each REsaturant:
		  		Create Tables
		  		Update Tables
		  		Delete Tables
An employee,
	Create Customer:
	Update Customer
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


Base = declarative_base()


class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True, autoincrement=True)
    num_of_tables = Column(Integer)
    location = Column(String(255))

    def __str__(self):
        return f"<Restaurant #{self.id} {self.num_of_tables} {self.location}>"


class Table(Base):
    __tablename__ = "tables"
    id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant = Column(Integer, ForeignKey(Restaurant.id))
    number_of_seats = Column(Integer)
    position = Column(String(255))

    def __str__(self):
        return f"<Table {self.id} {self.restaurant} {self.number_of_seats} {self.position}>"


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date_of_visit = Column(DateTime)
    table_id = Column(Integer, ForeignKey(Table.id))
    consumption = Column(Integer)

    def __str__(self):
        return f"<Customer #{self.id} {self.date_of_visit} {self.table_id} {self.consumption}>"

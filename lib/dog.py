from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Dog

# Define the create_table function
def create_table(Base, engine):
    '''Creates all tables in the database using Base metadata.'''
    Base.metadata.create_all(engine)

def save(session, dog):
    '''Save a Dog instance to the database.'''
    session.add(dog)
    session.commit()

def get_all(session):
    '''Returns all Dog instances from the database.'''
    return session.query(Dog).all()

def find_by_name(session, name):
    '''Find a Dog instance by name.'''
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, dog_id):
    '''Find a Dog instance by ID.'''
    return session.query(Dog).get(dog_id)

def find_by_name_and_breed(session, name, breed):
    '''Find a Dog instance by name and breed.'''
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, new_breed):
    '''Update a Dog's breed.'''
    dog.breed = new_breed
    session.commit()

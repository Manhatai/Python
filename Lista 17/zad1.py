from sqlalchemy import create_engine, Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base()

# Tablica do relacji wiele-do-wielu między Filmami i Aktorami
film_actor = Table('film_actor', Base.metadata,
    Column('film_id', Integer, ForeignKey('films.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)

class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director_id = Column(Integer, ForeignKey('directors.id'))
    platform_id = Column(Integer, ForeignKey('platforms.id'))

    director = relationship('Director', back_populates='films')
    actors = relationship('Actor', secondary=film_actor, back_populates='films')
    platform = relationship('Platform', back_populates='films')

class Director(Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    films = relationship('Film', back_populates='director')

class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    films = relationship('Film', secondary=film_actor, back_populates='actors')

class Platform(Base):
    __tablename__ = 'platforms'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    films = relationship('Film', back_populates='platform')

# Tworzenie sesji
engine = create_engine('sqlite:///oscar_hits.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Operacje CRUD

# Create
def add_entity(entity):
    session.add(entity)
    session.commit()

# Read
def get_all(entity):
    result = session.query(entity).all()
    return result

# Update
def update_entity():
    session.commit()

# Delete
def delete_entity(entity):
    session.delete(entity)
    session.commit()

# Przykładowe użycie
director = Director(name='Steven Spielberg')
actor = Actor(name='Tom Hanks')
platform = Platform(name='Netflix')
film = Film(title='Saving Private Ryan', director=director, platform=platform)
film.actors.append(actor)

add_entity(film)

#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game,Base

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    platforms = ['Switch', 'Playstation', 'Xbox', 'PC']
    genres = ['Adventure', 'RPG', 'Racing', 'Shooter', 'Puzzle']

    for _ in range(10):
        game = Game(
            title=fake.unique.word().title(),
            platform=random.choice(platforms),
            genre=random.choice(genres),
            price=random.randint(10, 70)
        )
        session.add(game)

    session.commit()
    print("Seed data inserted successfully!")

import pandas as pd
from datetime import date

from flask import Blueprint

from init import db, bcrypt
from models.user import User
from models.visited import Visited
from models.country import Country

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command("seed")
def seed_tables():
    # Read CSV file
    df = pd.read_csv('countries.csv')

    if df['country_name'].isnull().any():
            raise ValueError("CSV file contains null values in 'country_name' column")

    # create a list of User instances
    users = [
        User(
            email="admin@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
            is_admin=True
        ),
        User(
            name="User 1",
            email="user1@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
        )
    ]

    db.session.add_all(users)
    db.session.commit()
    
    admin_user_id = users[0].id

    countries = [Country(name=row['country_name'], visited=False, user_id=admin_user_id) for _, row in df.iterrows()]

    db.session.add_all(countries)
    db.session.commit()

    visiteds = [
        Visited(
            date=date.today(),
            user=users[1],
            country=countries[0]
        ),
        Visited(
            date=date.today(),
            user=users[1],
            country=countries[2]
        ),
        Visited(
            date=date.today(),
            user=users[1],
            country=countries[3]
        )
    ]

    db.session.add_all(visiteds)
    db.session.commit()

    print("Tables seeded")
from sqlalchemy.orm import sessionmaker
from models import User
from crud import create_user, get_user_by_id, update_user, delete_user
from schema import engine

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a new user
create_user(session, 'Galar Nashiruddin', 'galarnashiruddin@example.com')

# Retrieve a user by ID
user = get_user_by_id(session, 1)

# Update a user
update_user(session, user.id, 'Dadap Wijaya','dadapwijaya@example.com')

# Delete a user
delete_user(session, user.id)

# Retrieve all users from the database
users = session.query(User).all()

# Loop through the users and print their properties
for user in users:
    print(f'User ID: {user.id}, Name: {user.name}, Email: {user.email}')

# Close the session
session.close()

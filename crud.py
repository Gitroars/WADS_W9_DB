from sqlalchemy.orm import sessionmaker
from models import User
from schema import engine

Session = sessionmaker(bind=engine)
session = Session() #declare session
#function to create user
def create_user(session, name, email):
    user = User(name=name, email=email)
    session.add(user)
    session.commit()

#function to get user by id
def get_user_by_id(session,user_id):
    return session.query(User).filter_by(id=user_id).first()
#function to get update a user's data
def update_user(session,user_id, name, email):
    user = get_user_by_id(session,user_id)
    if user:
        user.name = name
        user.email = email
        session.commit()

    if not user:
        print(f"User with ID {user_id} not found.")
        return

    if name:
        user.name = name

    if email:
        user.email = email

    session.commit()
    print(f"User with ID {user_id} updated.")
#function to delete a user's data
def delete_user(session,user_id):
    user = get_user_by_id(session,user_id)
    if user:
        session.delete(user)
        session.commit()

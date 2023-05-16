from sqlalchemy import create_engine
from models import Base
import db_credentials
engine = create_engine(f'mysql+mysqlconnector://{db_credentials.MYSQL_USER}:{db_credentials.MYSQL_PASSWORD}@{db_credentials.MYSQL_HOST}/{db_credentials.MYSQL_DB}')
Base.metadata.create_all(engine)

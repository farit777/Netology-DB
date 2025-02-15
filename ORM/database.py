from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_db_session(database_uri):
    engine = create_engine(database_uri)
    Session = sessionmaker(bind=engine)
    return Session

# Можно использовать как дефолтный URI или передавать его динамически
DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/dbname'
DefaultSession = create_db_session(DATABASE_URI)

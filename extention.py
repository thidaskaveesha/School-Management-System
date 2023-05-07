#install sqlalchemy modules using pip install sql alchemy 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Connecting to a database server.
Base = declarative_base()
#Enter your database server link
url = 'mysql+pymysql://root:password@localhost:port/noname'
engine = create_engine(url=url, echo=True)
Base.metadata.create_all(bind = engine)

#making a session
Session = sessionmaker(bind=engine)
session = Session()

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(os.getenv('DB_URI'))
Session = sessionmaker(engine)
Model = declarative_base()

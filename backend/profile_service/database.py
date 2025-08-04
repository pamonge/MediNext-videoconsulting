from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'postgresql://admin:12345@profile_db:5432/profileDB'
#               postgresql://<usuario>:<contraseña>@<host>:<puerto>/<nombre_bd> (Dentro de docker)
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
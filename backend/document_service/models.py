from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.sql import func
from database import Base

class Document_model(Base):
    __tablename__ = "documents"
    dni = Column(String, primary_key=True)
    name = Column(String)

class File_model(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    content_type = Column(String)
    file_path = Column(String)
    upload_date = Column(DateTime, default=datetime.utcnow)
    owner_dni = Column(String, ForeignKey("documents.dni"))
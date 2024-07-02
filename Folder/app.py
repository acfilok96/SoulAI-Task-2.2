from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, declarative_base
from funcDB import *

engine = create_engine('sqlite:///Image_Record_SQLDB.db')
Base = declarative_base()

class ImageSummary(Base):
    __tablename__ = 'Image_Record_SQLDB_TABLE'
    id = Column("image_id", Integer, primary_key=True)
    filename = Column("image_filename", String, unique=True)
    summary = Column("image_summary", Text)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def store_image_summary(database, filename, summary):
    if searchDB(database, str(filename))==[]:
        image_summary = ImageSummary(filename=filename, summary=summary)
        session.add(image_summary)
        session.commit()



# Example usage:
filename = "1.jpg"
summary = "3 Example summary text."
database = "Image_Record_SQLDB.db"
store_image_summary(database, filename, summary)



# sql_query = "SELECT * from Image_Record_SQLDB_TABLE"
# print(read_sql_databse(database, sql_query))
# print("\n\n")
# print(ShowDB())
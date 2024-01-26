from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Link(Base):
    __tablename__ = "link"

    id = Column(Integer, primary_key=True)
    link_id = Column(String, nullable=False)
    origin_link = Column(String, nullable=False)
    shortened_link = Column(String, nullable=False)

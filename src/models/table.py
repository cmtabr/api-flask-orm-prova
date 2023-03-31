from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Boolean
from models.base import Base

class Table(Base):
    __tablename__ = 'table'

    id = Column(Integer, primary_key=True)
    game_name = Column(String(100), nullable=False)
    plataform = Column(String(50), nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)

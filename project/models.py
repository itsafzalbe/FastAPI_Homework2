from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Cars(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key = True, index = True)
    brand = Column(String(50), nullable = False)
    model = Column(String(50), nullable = False)
    year = Column(Integer, nullable = False)
    price = Column(Float, nullable = False)
    mileage = Column(Integer, nullable =True)
    color = Column(String(30), nullable = False)
    fuel_type = Column(String(20), nullable = False)
    transmission = Column(String(20), nullable = False)
    is_available = Column(Boolean, default = True)


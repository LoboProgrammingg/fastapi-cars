from sqlalchemy import Column, Integer, String, Text

from fast_car_api.database import Base


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    color = Column(String, nullable=True)
    factory_year = Column(Integer, nullable=True)
    model_year = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
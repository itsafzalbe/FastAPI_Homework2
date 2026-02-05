from http.client import HTTPException

from sqlalchemy.orm import Session
from models import Cars
from schemas import *



def create_car(db: Session, car: CarCreate):
    db_car = Cars(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


def get_car_by_id(db: Session, car_id: int):
    car = db.query(Cars).filter(Cars.id == car_id).first()
    return car


def get_cars(db: Session, skip: int = 0, limit: int = 100):
    cars = db.query(Cars).offset(skip).limit(limit).all()
    return cars

def update_car(db: Session, car_id: int, car: CarUpdate):
    db_car = get_car_by_id(db, car_id)

    if not db_car:
        raise None

    for attr, value in car.dict().items():
        setattr(db_car, attr, value)

    db.commit()
    db.refresh(db_car)
    return db_car


def delete_car(db: Session, db_car: Cars):
    db.delete(db_car)
    db.commit()



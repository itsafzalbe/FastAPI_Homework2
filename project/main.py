from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, get_db, engine






app = FastAPI(title="Auto Salon")
models.Base.metadata.create_all(bind=engine)

@app.post("/cars", response_model=schemas.CarResponse)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    return crud.create_car(db, car)

@app.get("/cars", response_model=list[schemas.CarResponse])
def read_cars(db: Session = Depends(get_db)):
    return crud.get_cars(db)

@app.get("/cars/{car_id}", response_model=schemas.CarResponse)
def read_car(car_id: int, db: Session = Depends(get_db)):
    return crud.get_car_by_id(db, car_id)


@app.patch("/cars/{car_id}", response_model=schemas.CarResponse)
def update_car(car_id: int, car: schemas.CarUpdate, db: Session = Depends(get_db)):
    updated = crud.update_car(db, car_id, car)
    if not updated:
        raise HTTPException(status_code=404, detail="Not found.")
    return updated


@app.delete("/cars/{car_id}")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_car(db, car_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Not found.")
    return deleted


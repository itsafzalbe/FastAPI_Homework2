from pydantic import BaseModel
from typing import Optional

class CarBase(BaseModel):
    brand: str
    model: str
    year: int
    price: float
    mileage: Optional[ int ]= None
    color: Optional[ str ] =None
    fuel_type: str
    transmission: str



class CarCreate(CarBase):
    pass


class CarUpdate(BaseModel):
    brand: Optional[ str ]
    model: Optional[ str ]
    year: Optional[ int ]
    price: Optional[float] = None
    mileage: Optional[ int ]
    color: Optional[ str ]
    fuel_type: Optional[str]
    transmission: Optional[ str ]


class CarResponse(CarBase):
    id: int
    is_available: bool

    class Config:
        from_attributes = True

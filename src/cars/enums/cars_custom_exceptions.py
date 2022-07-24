from enum import Enum

class CarsCustomExceptions(Enum):
    COLOR_IS_REQUIRED = "Color is required"
    HOURS_IS_REQUIRED = "Hours is required"
    IS_CLEAN_IS_REQUIRED = "State whether the car is clean"
    LICENSE_PLATE_IS_REQUIRED = "License plate is required"
    CAR_ALREADY_EXISTS = "Car already in garage"
    CAR_NOT_IN_GARAGE = "Car not in garage"
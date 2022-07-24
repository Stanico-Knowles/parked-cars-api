from src.cars.cars_model import Car
from src.cars.dto.cars_dto import CarsDto
from src.database.database import db

class CarRepo():
    def __init__(self) -> None:
        self.db = db

    def add_car(self, car: CarsDto) -> CarsDto:
        car = Car(car.license_plate, car.color, car.is_clean, car.hours, car.price)
        self.db.session.add(car)
        self.db.session.commit()
        return self.model_object_to_cars_dto(car=car)
    
    def get_all_cars(self) -> list[CarsDto]:
        return list(map(lambda car: self.model_object_to_cars_dto(car=car), Car.query.all()))
    
    def get_car_by_license_plate(self, license_plate: str) -> CarsDto:
        car: Car = Car.query.filter_by(license_plate=license_plate).first()
        if car:
            return self.model_object_to_cars_dto(car=car)
        return None
    
    def update_car(self, updated_car: CarsDto) -> CarsDto:
        car: Car = Car.query.filter_by(license_plate=updated_car.license_plate).first()
        if car:
            car.color = updated_car.color
            car.is_clean = updated_car.is_clean
            car.hours = updated_car.hours
            car.price = updated_car.price
            self.db.session.commit()
            return self.model_object_to_cars_dto(car=car)
        return None

    def delete_car(self, license_plate: str) -> CarsDto:
        car = Car.query.filter_by(license_plate=license_plate).first()
        self.db.session.delete(car)
        self.db.session.commit()
        return self.model_object_to_cars_dto(car=car)

    def model_object_to_cars_dto(self, car: Car) -> CarsDto:
        return CarsDto(car.license_plate, car.color, car.is_clean, car.hours, car.price)
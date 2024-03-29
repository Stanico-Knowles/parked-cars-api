from typing import List, Tuple, Union
from cars.dto.search_filters_dto import CarSearchFiltersDto
from src.cars.cars_model import Car
from src.cars.dto.cars_dto import CarsDto
from src.database.database import db

class CarRepo():
    def __init__(self) -> None:
        self.db = db

    def add_car(self, car: CarsDto) -> CarsDto:
        car = Car(license_plate=car.license_plate, color=car.color, is_clean=car.is_clean, hours=car.hours, price=car.price)
        self.db.session.add(car)
        self.db.session.commit()
        return self.model_object_to_cars_dto(car=car)
    
    def get_all_cars(self, search_filters: CarSearchFiltersDto, dynamic_filters: dict) -> Tuple[List[CarsDto], int]:
        cars = Car.query.filter_by(**dynamic_filters)
        if search_filters.max_hours:
            cars = cars.filter(Car.hours <= search_filters.max_hours)
        if search_filters.min_hours:
            cars = cars.filter(Car.hours >= search_filters.min_hours)
        if search_filters.max_price:
            cars = cars.filter(Car.price <= search_filters.max_price)
        if search_filters.min_price:
            cars = cars.filter(Car.price >= search_filters.min_price)
            """https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.BaseQuery.paginate"""
        cars = cars.paginate(page=search_filters.page, per_page=search_filters.page_size, error_out=False, max_per_page=20)
        return [self.model_object_to_cars_dto(car=car) for car in cars.items], cars.total
    
    def get_car_by_license_plate(self, license_plate: str) -> Union[CarsDto, None]:
        car: Car = Car.query.filter_by(license_plate=license_plate).first()
        if car:
            return self.model_object_to_cars_dto(car=car)
        return None
    
    def update_car(self, updated_car: CarsDto) -> Union[CarsDto, None]:
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
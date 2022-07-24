from typing import Union
from cars.dto.search_filters_dto import CarSearchFiltersDto
from src.cars.cars_repo import CarRepo
from src.cars.dto.cars_dto import CarsDto
from src.cars.enums.cars_custom_exceptions import CarsCustomExceptions
from src.cars.enums.liked_colors import LikedColors
from werkzeug.exceptions import BadRequest, NotFound


class CarService():
    def __init__(self) -> None:
        self.car_repo = CarRepo()
    
    def build_car_dto(self, car: dict) -> CarsDto:
        return CarsDto(license_plate=car['license_plate'], color=car['color'], is_clean=car['is_clean'], hours=car['hours'])

    def add_car(self, car: CarsDto) -> CarsDto:
        self._check_if_color_is_present(color=car.color)
        self._check_if_is_clean_is_present(is_clean=car.is_clean)
        self._check_if_hours_is_present(hours=car.hours)
        price = self.calculate_price(color=car.color, hours=car.hours, clean=car.is_clean)
        car.price = price
        if self.car_repo.get_car_by_license_plate(license_plate=car.license_plate):
            raise BadRequest(CarsCustomExceptions.CAR_ALREADY_EXISTS.value)
        return self.car_repo.add_car(car=car)
    
    def get_cars(self, search_filters: CarSearchFiltersDto) -> list[CarsDto]:
        dynamic_filters = self.populate_search_filters_dict({
            'color': search_filters.color,
            'is_clean': search_filters.is_clean,
        })
        return self.car_repo.get_all_cars(search_filters=search_filters, dynamic_filters=dynamic_filters)
    
    def get_car_by_license_plate(self, license_plate: str) -> CarsDto:
        self._check_if_license_plate_is_present(license_plate)
        car = self.car_repo.get_car_by_license_plate(license_plate)
        if not car:
            raise NotFound(CarsCustomExceptions.CAR_NOT_IN_GARAGE.value)
        return car

    def update_car(self, car: CarsDto) -> CarsDto:
        self._check_if_license_plate_is_present(car.license_plate)
        self._check_if_color_is_present(car.color)
        self._check_if_is_clean_is_present(car.is_clean)
        self._check_if_hours_is_present(car.hours)
        price = self.calculate_price(car.color, car.hours, car.is_clean)
        car.price = price
        car = self.car_repo.update_car(car)    
        if not car:
            raise NotFound(CarsCustomExceptions.CAR_NOT_IN_GARAGE.value)
        return car
    
    def delete_car(self, license_plate: str) -> CarsDto:
        self._check_if_license_plate_is_present(license_plate)
        car = self.car_repo.get_car_by_license_plate(license_plate)
        if not car:
            raise NotFound(CarsCustomExceptions.CAR_NOT_IN_GARAGE.value)
        return self.car_repo.delete_car(license_plate)
    
    def populate_search_filters_dict(self, search_filters: dict) -> dict:
        return {key : value for key, value in search_filters.items() if value}
    
    def _check_if_license_plate_is_present(self, license_plate: str) -> None:
        if not license_plate:
            raise BadRequest(CarsCustomExceptions.LICENSE_PLATE_IS_REQUIRED.value)
    
    def _check_if_color_is_present(self, color: str) -> None:
        if not color:
            raise BadRequest(CarsCustomExceptions.COLOR_IS_REQUIRED.value)
    
    def _check_if_is_clean_is_present(self, is_clean: bool) -> None:
        if is_clean is None:
            raise BadRequest(CarsCustomExceptions.IS_CLEAN_IS_REQUIRED.value)
        self._check_is_clean_is_type_boolean(is_clean)
    
    def _check_is_clean_is_type_boolean(self, is_clean: str) -> None:
        if not isinstance(is_clean, bool):
            raise BadRequest(CarsCustomExceptions.IS_CLEAN_IS_REQUIRED.value)
    
    def _check_if_hours_is_present(self, hours: int) -> None:
        if not hours:
            raise BadRequest(CarsCustomExceptions.HOURS_IS_REQUIRED.value)
    
    def _check_hours_is_type_int(self, hours: str) -> None:
        if not isinstance(hours, int):
            raise BadRequest(CarsCustomExceptions.INVALID_TYPE_FOR_HOURS.value)

    def calculate_price(self, color: str, hours: int, clean: str) -> Union[float, int]:
        self._check_hours_is_type_int(hours)
        if color in [color.value for color in LikedColors]:
            if clean == True:
                return 0
            return 3.5 * hours
        else:
            if clean == True:
                return 7 * hours
            return 14 * hours
from src.cars.cars_repo import CarRepo
from src.cars.dto.cars_dto import CarsDto
from src.cars.enums.cars_custom_exceptions import CarsCustomExceptions
from src.cars.enums.liked_colors import LikedColors
from werkzeug.exceptions import BadRequest, NotFound


class CarService():
    def __init__(self):
        self.car_repo = CarRepo()
    
    def build_car_dto(self, car: dict) -> CarsDto:
        return CarsDto(license_plate=car['license_plate'], color=car['color'], is_clean=car['is_clean'], hours=car['hours'])

    def add_car(self, car: CarsDto):
        self._check_if_color_is_present(car.color)
        self._check_if_is_clean_is_present(car.is_clean)
        self._check_if_hours_is_present(car.hours)
        price = self.calculate_price(car.color, car.hours, car.is_clean)
        car.price = price
        if self.car_repo.get_car_by_license_plate(car.license_plate):
            raise BadRequest(CarsCustomExceptions.CAR_ALREADY_EXISTS.value)
        return self.car_repo.add_car(car)
    
    def get_cars(self):
        return self.car_repo.get_all_cars()
    
    def get_car_by_license_plate(self, license_plate):
        self._check_if_license_plate_is_present(license_plate)
        car = self.car_repo.get_car_by_license_plate(license_plate)
        if not car:
            raise NotFound(CarsCustomExceptions.CAR_NOT_IN_GARAGE.value)
        return car

    def update_car(self, car: CarsDto):
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
    
    def delete_car(self, license_plate):
        self._check_if_license_plate_is_present(license_plate)
        car = self.car_repo.get_car_by_license_plate(license_plate)
        if not car:
            raise NotFound(CarsCustomExceptions.CAR_NOT_IN_GARAGE.value)
        return self.car_repo.delete_car(license_plate)
    
    def _check_if_license_plate_is_present(self, license_plate):
        if not license_plate:
            raise BadRequest(CarsCustomExceptions.LICENSE_PLATE_IS_REQUIRED.value)
    
    def _check_if_color_is_present(self, color) :
        if not color:
            raise BadRequest(CarsCustomExceptions.COLOR_IS_REQUIRED.value)
    
    def _check_if_is_clean_is_present(self, is_clean) :
        if is_clean is None:
            raise BadRequest(CarsCustomExceptions.IS_CLEAN_IS_REQUIRED.value)
    
    def _check_if_hours_is_present(self, hours) :
        if not hours:
            raise BadRequest(CarsCustomExceptions.HOURS_IS_REQUIRED.value)

    def calculate_price(self, color, hours, clean):
            if color in [color.value for color in LikedColors]:
                if clean == True:
                    return 0
                return 3.5 * hours
            else:
                if clean == True:
                    return 7 * hours
                return 14 * hours
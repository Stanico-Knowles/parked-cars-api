from flask import jsonify, request
from app import app
from cars.dto.search_filters_dto import CarSearchFiltersDto
from src.cars.cars_service import CarService
from src.cars.dto.cars_dto import CarsDto

@app.route('/api/cars', methods=['POST'])
def add_car():
    cars_dto = CarService().build_car_dto(request.json)
    new_car = CarService().add_car(cars_dto)
    return jsonify(new_car), 201

@app.route('/api/cars', methods=['GET'])
def get_cars():
    filters_dto = CarSearchFiltersDto(
        request.args.get('color') if request.args.get('color') else None, 
        request.args.get('is_clean') if request.args.get('is_clean') else None, 
        request.args.get('max_hours') if request.args.get('max_hours') else None, 
        request.args.get('min_hours') if request.args.get('min_hours') else None,
        request.args.get('max_price') if request.args.get('max_price') else None,
        request.args.get('min_price') if request.args.get('min_price') else None,
        request.args.get('page') if request.args.get('page') else 1,
        request.args.get('page_size') if request.args.get('page_size') else 10
    )
    cars: list[CarsDto] = CarService().get_cars(filters_dto)
    return jsonify(cars), 200

@app.route('/api/cars/<string:license_plate>', methods=['GET'])
def get_car_by_license_plate(license_plate):
    car = CarService().get_car_by_license_plate(license_plate)
    return jsonify(car), 200

@app.route('/api/cars/<string:license_plate>/update', methods=['PUT'])
def update_car(license_plate):
    car: CarsDto = CarService().get_car_by_license_plate(license_plate=license_plate)
    req = request.json
    car.color = req['color'] if req['color'] else car.color
    car.is_clean = req['is_clean'] if req['is_clean'] else car.is_clean
    car.hours = req['hours'] if req['hours'] else car.hours
    updated_car = CarService().update_car(car=car)
    return jsonify(updated_car), 200

@app.route('/api/cars/<string:license_plate>/delete', methods=['DELETE'])
def delete_car(license_plate):
    deleted_car = CarService().delete_car(license_plate)
    return jsonify(deleted_car), 200
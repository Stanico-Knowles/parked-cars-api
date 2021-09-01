from flask_restful import Resource, reqparse
from models.car import VehicleRepo, calcPrice


class Car(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('color',
                        type=str.lower,
                        trim=True,
                        required=True,
                        help="This Field Is Required!"
                        )
    parser.add_argument('clean',
                        type=bool,
                        required=True,
                        help="This Field Is Required!"
                        )
    parser.add_argument('hours',
                        type=int,
                        required=True,
                        help="This Field Is Required!"
                        )

    def get(self, licensePlateNumber):
        car = VehicleRepo.findByPlate(licensePlateNumber)
        if car:
            return car.json()
        return {'message': 'That Item Does Not Exist.'}

    def post(self, licensePlateNumber):
        
        try:
            if VehicleRepo.findByPlate(licensePlateNumber):
                return {'message': "Sorry, this car is currently inside the garage."}, 400

            data = Car.parser.parse_args()
            car = VehicleRepo(licensePlateNumber, **data)

            car.saveToDB() 

        except:
            return 

        return car.toJson(), 201

    def delete(self, licensePlateNumber):
        car = VehicleRepo.findByPlate(licensePlateNumber)
        if car:
            car.deleteFromDB()
            return {'message': 'Car was deleted.'}
        return {'message': 'Car not found.'}, 404
    
    def put(self, licensePlateNumber):

        data = Car.parser.parse_args()
        car = VehicleRepo.findByPlate(licensePlateNumber)

        if car:
            car.color = data['color']
            car.hours = data['hours']
            car.clean = data['clean'] 
            car.price = calcPrice(car.color, car.hours, car.clean)

        else:
            car = VehicleRepo(licensePlateNumber, **data)

        car.saveToDB()

        return car.toJson()


class CarsListed(Resource):
    def get(self):
        return {'cars': list(map(lambda x: x.toJson(), VehicleRepo.query.all()))}

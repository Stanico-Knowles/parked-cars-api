from flask_restful import Resource, reqparse
from models.car import CarModel


class Car(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('color',
                        type=str.lower,
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
        car = CarModel.findByPlate(licensePlateNumber)
        if car:
            return car.json()

    def post(self, licensePlateNumber):
        if CarModel.findByPlate(licensePlateNumber):
            return {'message': "That Car Is Already Stored In Our Database."}, 400
        
        data = Car.parser.parse_args()

        car = CarModel(licensePlateNumber, **data)

        """if Car.color == 'red' or 'green' or 'black':
            if Car.clean == True:
                CarModel.price = 0
            elif Car.clean == False:
                CarModel.price == (7 * 0.5) * Car.hours
        elif Car.color != 'red' or 'green' or 'black':
            if Car.clean == True:
                CarModel.price = 7 * Car.hours
            elif Car.clean == False:
                CarModel.price = (7 * 2) * Car.hours
        else:
            return {'message': "Please Enter Valid Information"}, 400"""
        
        try:
            car.saveToDB()
        except:
            return {"message": "An error occurred inserting the car."}, 500

        return car.json(), 201

    def delete(self, licensePlateNumber):
        car = CarModel.findByPlate(licensePlateNumber)
        if car:
            car.deleteFromDB()
            return {'message': 'Car was deleted.'}
        return {'message': 'Car not found.'}, 404
    
    def put(self, licensePlateNumber):
        data = Car.parser.parse_args()

        car = CarModel.findByPlate(licensePlateNumber)

        if car:
            car.price = data['price']
        else:
            car = CarModel(licensePlateNumber, **data)

        car.save_to_db()

        return car.json()


class CarsListed(Resource):
    def get(self):
        return {'cars': list(map(lambda x: x.json(), CarModel.query.all()))}

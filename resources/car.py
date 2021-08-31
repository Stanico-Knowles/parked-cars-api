from flask_restful import Resource, reqparse
from models.car import CarModel

class Car(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('')
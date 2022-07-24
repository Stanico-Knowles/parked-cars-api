from src.database.database import db


class Car(db.Model):
    __tablename__ = 'cars'

    license_plate = db.Column(
        db.String, 
        primary_key=True,
        nullable=False,
        unique=True,
    )
    color = db.Column(
        db.String(40),
        nullable=False,
    )
    is_clean = db.Column(
        db.Boolean,
        nullable=False,
    )
    hours = db.Column(
        db.Integer,
        nullable=False,
    )
    price = db.Column(
        db.Float(precision=2),
        nullable=False,
    )


    def __init__(self, license_plate, color, is_clean, hours, price):
        self.license_plate = license_plate
        self.color = color
        self.is_clean = is_clean
        self.hours = hours
        self.price = price

from db import db

class CarModel(db.Model):
    __tablename__ = 'cars'

    licensePlateNumber = db.Column(db.String, primary_key=True)
    color = db.Column(db.String(40))
    clean = db.Column(db.Boolean)
    hours = db.Column(db.Integer)
    #price = db.Column(db.Float(precision=2))


    def __init__(self, licensePlateNumber, color, clean, hours):
        self.licensePlateNumber = licensePlateNumber
        self.color = color
        self.clean = clean
        self.hours = hours
        #self.price = price

    def json(self):
        return {
            'licensePlateNumber': self.licensePlateNumber, 
            'color': self.color, 
            'clean': self.clean,
            'hours': self.hours
            #'price': self.price
            }

    @classmethod
    def findByPlate(cls,licensePlateNumber):
        return cls.query.filter_by(licensePlateNumber=licensePlateNumber).first()

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()
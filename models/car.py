from db import db

def calcPrice(color, hours, clean):

        if color == 'red' or color == 'green' or color == 'black':
            if clean == True:
                return 0
            elif clean == False:
                return 3.5 * hours
        else:
            if clean == True:
                return 7 * hours
            elif clean == False:
                return 14 * hours


class VehicleRepo(db.Model):
    __tablename__ = 'cars'

    licensePlateNumber = db.Column(db.String, primary_key=True)
    color = db.Column(db.String(40))
    clean = db.Column(db.Boolean)
    hours = db.Column(db.Integer)
    price = db.Column(db.Float(precision=2))


    def __init__(self, licensePlateNumber, color, clean, hours):
        self.licensePlateNumber = licensePlateNumber
        self.color = color
        self.clean = clean
        self.hours = hours
        self.price = calcPrice(color, hours, clean)

    def toJSON(self):
        return {
            'license plate number': self.licensePlateNumber, 
            'color': self.color, 
            'clean': self.clean,
            'hours': self.hours,
            'price': self.price
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
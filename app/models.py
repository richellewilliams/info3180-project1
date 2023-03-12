from . import db


class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    propertyTitle = db.Column(db.String(80))
    description = db.Column(db.String(1000))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price = db.Column(db.Integer)
    propertyType = db.Column(db.String(80))
    location = db.Column(db.String(80))
    photoName = db.Column(db.String(80))

    def __init__(self, propertyTitle, description, bedrooms, bathrooms, price, propertyType, location, photoName):
        self.propertyTitle = propertyTitle
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.propertyType = propertyType
        self.location = location
        self.photoName = photoName

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.propertyTitle)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bus(db.Model):
    __tablename__ = 'bus'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'capacity': self.capacity
        }

class Trajet(db.Model):
    __tablename__ = 'trajets'
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.String(100), nullable=False)
    end = db.Column(db.String(100), nullable=False)
    distance = db.Column(db.Float, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'start': self.start,
            'end': self.end,
            'distance': self.distance
        }

class Horaire(db.Model):
    __tablename__ = 'horaires'
    id = db.Column(db.Integer, primary_key=True)
    bus_id = db.Column(db.Integer, db.ForeignKey('bus.id'), nullable=False)
    trajet_id = db.Column(db.Integer, db.ForeignKey('trajets.id'), nullable=False)
    departure_time = db.Column(db.Time, nullable=False)
    arrival_time = db.Column(db.Time, nullable=False)
    
    bus = db.relationship('Bus', backref=db.backref('horaires', lazy=True))
    trajet = db.relationship('Trajet', backref=db.backref('horaires', lazy=True))

    def serialize(self):
        return {
            'id': self.id,
            'bus_id': self.bus_id,
            'trajet_id': self.trajet_id,
            'departure_time': str(self.departure_time),
            'arrival_time': str(self.arrival_time)
        }

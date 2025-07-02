from app import db

class Event(db.Model):
    __tablename__="events"
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(255))
    image = db.Column(db.String(500))
    address = db.Column(db.String(255))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    date = db.Column(db.String(20))
    time = db.Column(db.String(20))
    info = db.Column(db.Text)
    price = db.Column(db.Float(50))
    genre = db.Column(db.String(100))
    
    bookings = db.relationship('BookingEvent', backref='event', cascade='all, delete-orphan')
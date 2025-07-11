from app import db

class User(db.Model):
    __tablename__="user"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String, nullable=False)
    email=db.Column(db.String, nullable=False, unique=True)
    password=db.Column(db.String, nullable=False)
    
    bookings = db.relationship('BookingEvent', backref='user', cascade='all, delete-orphan')

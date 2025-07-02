from app import db
from datetime import datetime
from app.models.event import Event
from app.models.user import User

class BookingEvent(db.Model):
    __tablename__ = "booking_event"

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.String(355), db.ForeignKey('events.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    event_name = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(255), nullable=False)

    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    tickets = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Numeric(10, 2))

    user_obj = db.relationship('User', backref='user_bookings')
    event_obj = db.relationship('Event', backref='event_bookings')

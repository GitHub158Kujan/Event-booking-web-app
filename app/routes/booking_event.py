from flask import Blueprint, render_template, flash, request, session, redirect, url_for
from app.models.booking import BookingEvent
from app.models.event import Event
from app.models.user import User
from app import db
from datetime import datetime

booking_bp = Blueprint("booking", __name__)


@booking_bp.route("/create_booking/<string:event_id>", methods=["GET", "POST"])
def create_booking(event_id):
    user_id = session.get("user_id")
    if not user_id:
        flash("Please log in first.", "warning")
        return redirect(url_for("auth.login"))

    event = Event.query.get_or_404(event_id)
    user = User.query.get_or_404(user_id)

    if request.method == "POST":
        ticket_count = int(request.form.get("tickets", 1))
        total_price = float(event.price) * ticket_count

        new_booking = BookingEvent(
            event_id=event.id,
            user_id=user.id,
            event_name=event.name,
            username=user.username,
            tickets=ticket_count,
            total_price=total_price,
        )

        db.session.add(new_booking)
        db.session.commit()

        flash("Event has been booked successfully!", "success")
        return redirect(url_for("event.home"))  

    return render_template("book_event.html", event=event, user=user, datetime=datetime)

from flask import Flask, request, render_template, flash, session, redirect, url_for, Blueprint
from app.models.event import Event
from app.models.user import User
from app.models.booking import BookingEvent
from app import db


admin_bp=Blueprint("admin",__name__)

@admin_bp.route("/admin")
def admin_homepage(): 
    events=Event.query.all()
    return render_template("admin/dashboard.html",events=events)

@admin_bp.route("/admin/events")
def events(): 
    events=Event.query.all()
    return render_template("admin/events.html",events=events)


@admin_bp.route("/admin/view_users")
def view_users():
    users=User.query.all()
    return render_template("admin/users.html",users=users)

@admin_bp.route("/admin/delete_user/<int:user_id>")
def delete_user(user_id):
    user_id = User.query.get_or_404(user_id)
    db.session.delete(user_id)
    db.session.commit()
    flash("User has been deleted successfully!", "success")
    return redirect(url_for("admin.view_users"))
    

@admin_bp.route("/admin/view_all_bookings")
def bookings():
    bookings=BookingEvent.query.all()
    return render_template("admin/bookings.html",bookings=bookings)

@admin_bp.route("/admin/delete_event/<string:event_id>")
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    flash("Event has been deleted successfully!", "success")
    return redirect(url_for("admin.admin_homepage"))


@admin_bp.route("/admin/delete_booking/<string:booking_id>")
def delete_booking(booking_id):
    booking = BookingEvent.query.get_or_404(booking_id)
    db.session.delete(booking)
    db.session.commit()
    flash("Booking has been deleted successfully!", "success")
    return redirect(url_for("admin.bookings", booking_id=booking_id))



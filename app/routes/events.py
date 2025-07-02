from flask import Flask, request, render_template, flash, session, redirect, url_for, Blueprint, current_app
from app.models.event import Event
from app import db
from datetime import datetime
import random
import string
from werkzeug.utils import secure_filename
import os



event_bp=Blueprint("event",__name__)


@event_bp.route("/", methods=["GET"])
def home():
    page = request.args.get('page', 1, type=int)
    per_page = 12
    events = Event.query.paginate(page=page, per_page=per_page)
    return render_template("index.html", events=events)

@event_bp.route("/<string:event_id>", methods=["GET"])
def event_details(event_id):
    event = Event.query.get_or_404(event_id) 
    return render_template("event_details.html", event=event, datetime=datetime)
    

@event_bp.route("/add_event", methods=["GET", "POST"])
def add_event():
    
    if 'user_id' not in session:
        flash("Please log in to add an event.", "warning")
        return redirect(url_for("auth.login"))
    
    if request.method == "POST":
        def generate_event_id(length=12):
            return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        
        title = request.form.get("title")
        description = request.form.get("description")
        date = request.form.get("date")
        time_str = request.form.get("time")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        price = request.form.get("price")
        genre=request.form.get("genre")
        time_24 = datetime.strptime(time_str, "%I:%M %p").strftime("%H:%M:%S")
        
        image_file = request.files.get('event_image')
        filename = None
        if image_file and image_file.filename != "":
            filename = secure_filename(image_file.filename)
            upload_path = os.path.join(current_app.root_path, 'static', 'uploads')
            os.makedirs(upload_path, exist_ok=True)
            image_path = os.path.join(upload_path, filename)
            image_file.save(image_path)

        event_id = generate_event_id()
        new_event = Event(
            id=event_id,
            name=title,
            info=description,
            time=time_24,
            date=date,
            address=address,
            city=city,
            state=state,
            image=filename,
            price=price,
            genre=genre
        )

        db.session.add(new_event)
        db.session.commit()

        flash("Event Added Successfully!", "success")
        return redirect(url_for("event.home"))

    return render_template("add_event.html")


@event_bp.route("/search")
def search():
    query = request.args.get("query", "").strip()
    
    if not query:
        flash("Please enter a search term.", "warning")
        return redirect(url_for("event.home"))

    results = Event.query.filter(
        (Event.name.ilike(f"%{query}%")) |
        (Event.city.ilike(f"%{query}%")) |
        (Event.genre.ilike(f"%{query}%"))
    ).all()

    return render_template("search_results.html", events=results, query=query)

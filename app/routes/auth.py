from flask import Flask, Blueprint, url_for, request, render_template, redirect, session, flash
from app.models.user import User
from app import db

auth_bp=Blueprint("auth",__name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == "admin@gmail.com" and password == "@123":
            session.clear()  # Ensure fresh session
            session["admin"] = True
            flash("Admin login successful!", "success")
            return redirect(url_for("admin.admin_homepage"))

        user = User.query.filter_by(email=email).first()
        if user and user.password == password:  
            session.clear()  
            session["user_id"] = user.id
            session["email"] = user.email
            flash("Login successful!", "success")
            return redirect(url_for("event.home"))
        else:
            flash("Invalid credentials", "danger")
            return redirect(url_for("auth.login"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Logged Out!", "info")
    return redirect(url_for("auth.login"))


from app.routes.validator import SignupForm
@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
   
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("Email already registered. Please log in.", "warning")
            return redirect(url_for("auth.login"))

        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data  
        )
        db.session.add(new_user)
        db.session.commit()
        session["user"] = form.email.data
        flash("Signup successful!", "success")
        return redirect(url_for("auth.login"))

    return render_template("signup.html", form=form)
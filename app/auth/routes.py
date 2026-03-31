from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app.auth import auth_bp
from app.auth.forms import RegistrationForm, LoginForm
from app.extensions import db
from app.models import User


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    # If the user is already logged in, they shouldn't see the register page
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if user already exists
        user_exists = User.query.filter_by(email=form.email.data).first()
        if user_exists:
            flash("Email already registered. Please log in.", "danger")
            return redirect(url_for("auth.login"))

        # Create new user and hash their password
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)

        # Save to database
        db.session.add(user)
        db.session.commit()

        flash("Congratulations, you are now a registered user!", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", title="Register", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()
    if form.validate_on_submit():
        # Find the user by email
        user = User.query.filter_by(email=form.email.data).first()

        # Check if user exists AND password is correct
        if user is None or not user.check_password(form.password.data):
            flash("Invalid email or password", "danger")
            return redirect(url_for("auth.login"))

        # Log the user in
        login_user(user, remember=form.remember.data)
        flash(f"Welcome back, {user.username}!", "success")
        return redirect(url_for("main.index"))

    return render_template("auth/login.html", title="Login", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    """Handle user logout."""
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("main.index"))

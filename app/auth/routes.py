from flask import render_template, redirect, url_for, flash, request
from app.auth import auth_bp
from app.auth.forms import RegistrationForm, LoginForm


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """Handle user registration."""
    form = RegistrationForm()

    # validate_on_submit() checks if it's a POST request AND if all form rules pass
    if form.validate_on_submit():
        # TODO: Save the new user to the database here

        # Flash a success message to the user
        flash(
            f"Account created for {form.username.data}! You can now log in.", "success"
        )
        # Redirect them to the login page
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", title="Register", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Handle user login."""
    form = LoginForm()

    if form.validate_on_submit():
        # TODO: Check the database to verify the user's credentials here

        flash("You have successfully logged in!", "success")
        return redirect(url_for("main.index"))

    return render_template("auth/login.html", title="Login", form=form)

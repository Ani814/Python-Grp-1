import os
import uuid
from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from app.extensions import db
from app.forms import ProfileForm
from app.models import User

profile_bp = Blueprint("profile", __name__)


def _allowed_file(filename):
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    return ext in current_app.config["ALLOWED_IMAGE_EXTENSIONS"]


@profile_bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    """Requirement #13: view + edit picture, name, email."""
    form = ProfileForm(obj=current_user)

    if form.validate_on_submit():
        new_email = form.email.data.lower()
        if new_email != current_user.email:
            existing = User.query.filter_by(email=new_email).first()
            if existing:
                flash("That email is already in use by another account.", "danger")
                return render_template("profile.html", form=form)

        current_user.name = form.name.data.strip()
        current_user.email = new_email

        file = form.picture.data
        if file and file.filename and _allowed_file(file.filename):
            filename = secure_filename(f"{uuid.uuid4().hex}_{file.filename}")
            filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            current_user.profile_image = filename

        db.session.commit()
        flash("Profile updated.", "success")
        return redirect(url_for("profile.profile"))

    return render_template("profile.html", form=form)


@profile_bp.route("/user/<int:user_id>")
def public_profile(user_id):
    """Requirement #6: clicking a job author navigates to their public profile."""
    user = User.query.get_or_404(user_id)
    return render_template("public_profile.html", user=user)

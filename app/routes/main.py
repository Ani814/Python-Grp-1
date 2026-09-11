from flask import Blueprint, render_template, request, current_app
from app.models import Job

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    """Public jobs list. Visible with or without login (requirement #3)."""
    category = request.args.get("category", "")
    sort = request.args.get("sort", "newest")

    query = Job.query
    if category:
        query = query.filter_by(category=category)

    if sort == "oldest":
        query = query.order_by(Job.date_posted.asc())
    elif sort == "salary_high":
        query = query.order_by(Job.salary.desc())
    elif sort == "salary_low":
        query = query.order_by(Job.salary.asc())
    else:  # newest (default) — requirement #14
        query = query.order_by(Job.date_posted.desc())

    jobs = query.all()
    categories = current_app.config["JOB_CATEGORIES"]
    return render_template(
        "index.html", jobs=jobs, categories=categories, current_category=category, current_sort=sort
    )


@main_bp.route("/about")
def about():
    """Public About page, visible without login (requirement #3)."""
    return render_template("about.html")

from flask import Blueprint, render_template, redirect, url_for, flash, current_app, abort
from flask_login import login_required, current_user

from app.extensions import db
from app.models import Job
from app.forms import JobForm
from app.utils.logger import job_logger
from app.utils.external_api import convert_salary

jobs_bp = Blueprint("jobs", __name__)


@jobs_bp.route("/job/<int:job_id>")
def job_detail(job_id):
    """Full details view — requirement #7 'Read More'. Viewable by anyone."""
    job = Job.query.get_or_404(job_id)
    converted = convert_salary(job.salary) if job.salary else None
    return render_template("job_detail.html", job=job, converted=converted)


@jobs_bp.route("/job/add", methods=["GET", "POST"])
@login_required
def add_job():
    """Requirement #5: only authenticated users can add a job."""
    form = JobForm()
    form.category.choices = current_app.config["JOB_CATEGORIES"]

    if form.validate_on_submit():
        job = Job(
            title=form.title.data.strip(),
            short_description=form.short_description.data.strip(),
            full_description=form.full_description.data.strip(),
            company=form.company.data.strip(),
            salary=form.salary.data,
            location=form.location.data.strip(),
            category=form.category.data,
            author=current_user,
        )
        db.session.add(job)
        db.session.commit()

        job_logger.info(f"Job created: '{job.title}' (id={job.id}) by {current_user.email}")  # log #3
        flash("Job posted successfully!", "success")
        return redirect(url_for("jobs.job_detail", job_id=job.id))

    return render_template("job_form.html", form=form, title="Add Job")


@jobs_bp.route("/job/<int:job_id>/edit", methods=["GET", "POST"])
@login_required
def edit_job(job_id):
    """Requirement #8: only the owner may edit their own post."""
    job = Job.query.get_or_404(job_id)

    if job.author != current_user:
        job_logger.warning(
            f"Unauthorized edit attempt on job id={job_id} by {current_user.email}"
        )
        abort(403)

    form = JobForm(obj=job)
    form.category.choices = current_app.config["JOB_CATEGORIES"]

    if form.validate_on_submit():
        job.title = form.title.data.strip()
        job.short_description = form.short_description.data.strip()
        job.full_description = form.full_description.data.strip()
        job.company = form.company.data.strip()
        job.salary = form.salary.data
        job.location = form.location.data.strip()
        job.category = form.category.data
        db.session.commit()

        job_logger.info(f"Job edited: '{job.title}' (id={job.id}) by {current_user.email}")  # log #4
        flash("Job updated successfully!", "success")
        return redirect(url_for("jobs.job_detail", job_id=job.id))

    return render_template("job_form.html", form=form, title="Edit Job")


@jobs_bp.route("/job/<int:job_id>/delete", methods=["POST"])
@login_required
def delete_job(job_id):
    """Requirement #8: only the owner may delete their own post."""
    job = Job.query.get_or_404(job_id)

    if job.author != current_user:
        job_logger.warning(
            f"Unauthorized delete attempt on job id={job_id} by {current_user.email}"
        )
        abort(403)

    title = job.title
    db.session.delete(job)
    db.session.commit()

    job_logger.info(f"Job deleted: '{title}' (id={job_id}) by {current_user.email}")  # log #4
    flash("Job deleted.", "info")
    return redirect(url_for("main.index"))

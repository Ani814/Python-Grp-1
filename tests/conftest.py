import pytest
from config import TestConfig
from app import create_app
from app.extensions import db
from app.models import User, Job


@pytest.fixture
def app():
    app = create_app(TestConfig)
    with app.app_context():
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def user_a(app):
    with app.app_context():
        u = User(name="Alice", email="alice@example.com")
        u.set_password("password123")
        db.session.add(u)
        db.session.commit()
        return u.id


@pytest.fixture
def user_b(app):
    with app.app_context():
        u = User(name="Bob", email="bob@example.com")
        u.set_password("password456")
        db.session.add(u)
        db.session.commit()
        return u.id


@pytest.fixture
def job_by_a(app, user_a):
    with app.app_context():
        job = Job(
            title="Backend Developer",
            short_description="Build APIs",
            full_description="Full details about the backend role.",
            company="Acme Inc",
            salary=3000,
            location="Tbilisi",
            category="IT",
            user_id=user_a,
        )
        db.session.add(job)
        db.session.commit()
        return job.id


def login(client, email, password):
    return client.post(
        "/login", data={"email": email, "password": password}, follow_redirects=True
    )

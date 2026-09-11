import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Secret key used to sign sessions and CSRF tokens.
    # In production, set this via an environment variable on your host.
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///" + os.path.join(BASE_DIR, "instance", "jobboard.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "app", "static", "uploads")
    ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # 2 MB max upload

    LOG_FILE = os.path.join(BASE_DIR, "logs", "app.log")

    JOB_CATEGORIES = ["IT", "Design", "Marketing", "Sales", "Customer Support", "Other"]


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False  # disabled only for automated tests

    # In-memory SQLite normally gives each new connection a fresh, empty
    # database. Forcing a single shared connection (StaticPool) keeps all
    # requests in a test talking to the same in-memory DB.
    from sqlalchemy.pool import StaticPool

    SQLALCHEMY_ENGINE_OPTIONS = {
        "poolclass": StaticPool,
        "connect_args": {"check_same_thread": False},
    }

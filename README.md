# JobBoard

A Flask web app for posting and browsing job listings, built for the
Tbilisi School of Communication Python final project.

## Features implemented (mapped to the assignment spec)

- Registration & login (Flask-Login, hashed passwords via Flask-Bcrypt)
- Public browsing: anyone can view Jobs and About without an account
- Nav bar changes after login (Add Job / Profile / Logout appear; Login /
  Register disappear)
- Add / edit / delete job postings — **only the owner** can edit or delete
  their own post (server-side 403 check in `app/routes/jobs.py`, mirrored
  in the templates)
- Job cards (title, author, date, short description) + "Read More" full
  detail page
- Author name links to a public profile page listing their other jobs
- Categories (IT, Design, Marketing, Sales, Customer Support, Other) with
  filtering, plus sorting by date/salary
- Custom, styled 404 and 500 error pages
- CSRF protection on every form (Flask-WTF)
- Profile page: edit name, email, and upload a profile picture
- External API: live currency conversion (GEL → USD/EUR) via the free
  Frankfurter API, shown on the job detail page
- Logging to `logs/app.log`: successful/failed logins, job created,
  job edited/deleted, and API request errors
- 12 automated pytest tests covering routes, login, and permissions
  (`tests/`)

## Project structure

```
jobboard/
├── app/
│   ├── __init__.py        # app factory, blueprint + error handler registration
│   ├── extensions.py       # db, login_manager, csrf, bcrypt instances
│   ├── models.py           # User, Job
│   ├── forms.py             # Flask-WTF forms (all CSRF-protected)
│   ├── routes/
│   │   ├── main.py          # home (jobs list) + about
│   │   ├── auth.py          # register / login / logout
│   │   ├── jobs.py          # add / edit / delete / detail
│   │   └── profile.py       # own profile + public profile view
│   ├── utils/
│   │   ├── logger.py         # file logging setup
│   │   └── external_api.py    # Frankfurter currency conversion
│   ├── templates/           # Jinja2 + Bootstrap 5
│   └── static/
├── tests/                   # pytest suite (route/login/permissions)
├── config.py                # Config + TestConfig
├── run.py                   # entry point
└── requirements.txt
```

## Running locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Visit `http://127.0.0.1:5000`. The SQLite database and `logs/app.log`
are created automatically on first run.

## Running the tests

```bash
pytest tests/ -v
```

## Environment variables (for production)

Set a real `SECRET_KEY` before deploying — don't rely on the default:

```bash
export SECRET_KEY="a-long-random-string"
```

Optionally set `DATABASE_URL` if you're using something other than the
bundled SQLite file (e.g. Postgres on Render).

## Deploying (GitHub + hosting, per the assignment requirement)

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: JobBoard Flask app"
   git branch -M main
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Host it** (any of these work well for a free Flask deployment):
   - **Render.com** — new Web Service from your GitHub repo,
     build command `pip install -r requirements.txt`,
     start command `gunicorn run:app`, add a `SECRET_KEY` env var.
   - **PythonAnywhere** — good for simple, always-on Flask hosting.
   - **Railway.app** — similar to Render, auto-detects Flask + gunicorn.

   `gunicorn` is already in `requirements.txt` for this reason — the
   Flask dev server (`python run.py`) is fine locally but should not be
   used in production.

## Notes on the external API

The currency conversion calls `https://api.frankfurter.app` at request
time — no API key needed. If the API is briefly unreachable, the page
still renders (salary in GEL only) and the failure is written to
`logs/app.log` as an "API request error," per the logging requirement.

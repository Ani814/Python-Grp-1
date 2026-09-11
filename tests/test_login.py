from tests.conftest import login


def test_login_success(client, user_a):
    """Requirement: Login test — correct credentials log the user in."""
    response = login(client, "alice@example.com", "password123")
    assert response.status_code == 200
    assert b"Welcome back" in response.data


def test_login_wrong_password(client, user_a):
    """Wrong password should be rejected and the user kept on the login page."""
    response = login(client, "alice@example.com", "wrongpassword")
    assert response.status_code == 200
    assert b"Invalid email or password" in response.data


def test_login_unknown_email(client):
    """Logging in with an email that was never registered should also fail cleanly."""
    response = login(client, "nobody@example.com", "whatever123")
    assert response.status_code == 200
    assert b"Invalid email or password" in response.data


def test_logout_requires_login(client):
    """Logout is a protected route — anonymous users get redirected, not a 500."""
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200

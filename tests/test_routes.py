def test_home_page_loads(client):
    """Requirement: Route test — public home page should return 200."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Open Positions" in response.data


def test_about_page_loads(client):
    response = client.get("/about")
    assert response.status_code == 200


def test_add_job_requires_login(client):
    """Anonymous users must be redirected away from the protected add-job route."""
    response = client.get("/job/add", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data  # redirected to the login page


def test_unknown_route_returns_404(client):
    response = client.get("/this-page-does-not-exist")
    assert response.status_code == 404

from tests.conftest import login


def test_owner_can_access_edit_page(client, user_a, job_by_a):
    """Requirement: permissions test — the owner CAN reach the edit form."""
    login(client, "alice@example.com", "password123")
    response = client.get(f"/job/{job_by_a}/edit")
    assert response.status_code == 200
    assert b"Edit Job" in response.data


def test_non_owner_cannot_edit_others_post(client, user_a, user_b, job_by_a):
    """Requirement: permissions test — Bob must NOT be able to edit Alice's job."""
    login(client, "bob@example.com", "password456")
    response = client.get(f"/job/{job_by_a}/edit")
    assert response.status_code == 403


def test_non_owner_cannot_delete_others_post(client, user_a, user_b, job_by_a):
    """Requirement: permissions test — Bob must NOT be able to delete Alice's job."""
    login(client, "bob@example.com", "password456")
    response = client.post(f"/job/{job_by_a}/delete")
    assert response.status_code == 403


def test_anonymous_cannot_edit(client, job_by_a):
    """Anonymous users get redirected to login rather than reaching the form."""
    response = client.get(f"/job/{job_by_a}/edit", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data

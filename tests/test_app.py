from fastapi.testclient import TestClient

from src.app import app


def test_duplicate_signup_is_rejected():
    client = TestClient(app)
    activity_name = "Chess Club"
    email = "duplicate.student@mergington.edu"

    first_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
    assert first_response.status_code == 200

    second_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    assert second_response.status_code == 400
    assert second_response.json()["detail"] == "Student already signed up for this activity"

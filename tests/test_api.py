from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["message"] == (
        "Business Report Automation API is running"
    )


def test_get_all_employees():

    response = client.get("/employees")

    assert response.status_code == 200

    data = response.json()

    assert data["total_employees"] == 8
    assert len(data["employees"]) == 8


def test_filter_employees_by_department():

    response = client.get("/employees?department=IT")

    assert response.status_code == 200

    data = response.json()

    assert data["total_employees"] == 3

    for employee in data["employees"]:
        assert employee["Department"] == "IT"


def test_invalid_department():

    response = client.get(
        "/employees?department=Marketing"
    )

    assert response.status_code == 404

    assert response.json()["detail"] == (
        "Department 'Marketing' not found"
    )


def test_search_employee():

    response = client.get(
        "/employees/search?name=rah"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total_employees"] == 1
    assert data["employees"][0]["Employee_Name"] == "Rahul"
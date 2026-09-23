from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_api_status():

    response = client.get("/api")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == (
        "Business Report Automation API is running"
    )


def test_get_all_employees():

    response = client.get("/employees")

    assert response.status_code == 200

    data = response.json()

    assert data["total_employees"] == 8
    assert len(data["employees"]) == 8


def test_filter_employees_by_department():

    response = client.get(
        "/employees?department=IT"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total_employees"] == 3

    for employee in data["employees"]:

        assert employee["Department"] == "IT"


def test_search_employee():

    response = client.get(
        "/employees?name=rah"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total_employees"] == 1

    assert (
        data["employees"][0]["Employee_Name"]
        == "Rahul"
    )


def test_combined_filter():

    response = client.get(
        "/employees?name=rah&department=IT"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total_employees"] == 1

    assert (
        data["employees"][0]["Employee_Name"]
        == "Rahul"
    )


def test_no_matching_employee():

    response = client.get(
        "/employees?name=rah&department=HR"
    )

    assert response.status_code == 404

    assert (
        response.json()["detail"]
        == "No employee records found."
    )


def test_department_summary():

    response = client.get("/departments")

    assert response.status_code == 200

    data = response.json()

    assert "departments" in data

    assert len(data["departments"]) == 3


def test_generate_report():

    response = client.get("/employees")

    assert response.status_code == 200

    employees = response.json()["employees"]

    report_response = client.post(
        "/generate-report",
        json=employees
    )

    assert report_response.status_code == 200

    assert (
        report_response.headers["content-type"]
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

def test_parse_pdf():

    response = client.get("/parse-pdf")

    assert response.status_code == 200

    data = response.json()

    assert data["file"] == "data/pdfs/business_report.pdf"

    assert "Business Performance Report" in data["text"]
    assert "Amit" in data["text"]
    assert "Neha" in data["text"]
    assert "90%" in data["text"]
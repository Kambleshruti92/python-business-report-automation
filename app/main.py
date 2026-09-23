from fastapi import FastAPI, HTTPException
from app.data_processor import (
    load_employee_data,
    process_employee_data,
    generate_department_summary
)

from app.report_generator import generate_excel_report


app = FastAPI(
    title="Business Report Automation API",
    description="API for employee performance and business reporting",
    version="1.0.0"
)


# Load and process data
df = load_employee_data()
processed_data = process_employee_data(df)
department_summary = generate_department_summary(processed_data)


@app.get("/")
def home():
    return {
        "message": "Business Report Automation API is running"
    }


@app.get("/employees")
def get_employees(department: str = None):

    data = processed_data

    # Filter employees by department if provided
    if department:

        data = data[
            data["Department"].str.lower() == department.lower()
        ]

        # Department does not exist
        if data.empty:
            raise HTTPException(
                status_code=404,
                detail=f"Department '{department}' not found"
            )

    employees = data.to_dict(orient="records")

    return {
        "total_employees": len(employees),
        "employees": employees
    }

@app.get("/employees/search")
def search_employee(name: str):

    data = processed_data[
        processed_data["Employee_Name"]
        .str.contains(name, case=False, na=False)
    ]

    if data.empty:
        raise HTTPException(
            status_code=404,
            detail=f"No employee found with name '{name}'"
        )

    employees = data.to_dict(orient="records")

    return {
        "total_employees": len(employees),
        "employees": employees
    }

@app.get("/departments")
def get_department_summary():

    summary = department_summary.to_dict(orient="records")

    return {
        "departments": summary
    }


@app.post("/generate-report")
def generate_report():

    try:

        report_file = generate_excel_report(
            processed_data,
            department_summary
        )

        return {
            "message": "Report generated successfully",
            "file": report_file
        }

    except PermissionError:

        raise HTTPException(
            status_code=423,
            detail=(
                "The Excel report is currently open. "
                "Please close the file and try again."
            )
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Report generation failed: {str(error)}"
        )
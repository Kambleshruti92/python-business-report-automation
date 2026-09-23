from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

import pandas as pd

from app.data_processor import (
    load_employee_data,
    process_employee_data,
    generate_department_summary
)

from app.report_generator import generate_excel_report


# --------------------------------------------------
# FastAPI Application
# --------------------------------------------------

app = FastAPI(
    title="Business Report Automation API",
    description="API for employee performance and business reporting",
    version="1.0.0"
)


# --------------------------------------------------
# Frontend Static Files
# --------------------------------------------------

app.mount(
    "/frontend",
    StaticFiles(directory="frontend"),
    name="frontend"
)


# --------------------------------------------------
# Load and Process Data
# --------------------------------------------------

df = load_employee_data()

processed_data = process_employee_data(df)

department_summary = generate_department_summary(
    processed_data
)


# --------------------------------------------------
# Home Page
# --------------------------------------------------

@app.get("/")
def home():

    return FileResponse(
        "frontend/index.html"
    )


# --------------------------------------------------
# API Status
# --------------------------------------------------

@app.get("/api")
def api_status():

    return {
        "message": "Business Report Automation API is running"
    }


# --------------------------------------------------
# Get Employees
# --------------------------------------------------

@app.get("/employees")
def get_employees(
    department: str = None,
    name: str = None
):

    data = processed_data.copy()

    # Filter by department
    if department:

        data = data[
            data["Department"].str.lower()
            == department.lower()
        ]

    # Filter by employee name
    if name:

        data = data[
            data["Employee_Name"]
            .str.contains(
                name,
                case=False,
                na=False
            )
        ]

    # No matching records
    if data.empty:

        raise HTTPException(
            status_code=404,
            detail="No employee records found."
        )

    employees = data.to_dict(
        orient="records"
    )

    return {
        "total_employees": len(employees),
        "employees": employees
    }


# --------------------------------------------------
# Department Summary
# --------------------------------------------------

@app.get("/departments")
def get_department_summary():

    summary = department_summary.to_dict(
        orient="records"
    )

    return {
        "departments": summary
    }


# --------------------------------------------------
# Generate Excel Report
# --------------------------------------------------

@app.post("/generate-report")
def generate_report(
    employees: list[dict]
):

    try:

        # Check if there are records
        if not employees:

            raise HTTPException(
                status_code=400,
                detail="No employee records available for report."
            )


        # Convert filtered employee data
        # into a Pandas DataFrame
        filtered_data = pd.DataFrame(
            employees
        )


        # Generate department summary
        # only for the filtered employees
        filtered_summary = (
            generate_department_summary(
                filtered_data
            )
        )


        # Generate Excel report
        report_file = generate_excel_report(
            filtered_data,
            filtered_summary
        )


        # Return Excel file for download
        return FileResponse(
            path=report_file,
            filename="employee_performance_report.xlsx",
            media_type=(
                "application/vnd.openxmlformats-"
                "officedocument.spreadsheetml.sheet"
            )
        )


    except PermissionError:

        raise HTTPException(
            status_code=423,
            detail=(
                "The Excel report is currently open. "
                "Please close the file and try again."
            )
        )


    except HTTPException:

        raise


    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=(
                f"Report generation failed: {str(error)}"
            )
        )
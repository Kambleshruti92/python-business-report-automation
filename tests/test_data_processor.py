import pandas as pd

from app.data_processor import process_employee_data


def test_process_employee_data():

    data = pd.DataFrame({
        "Employee_ID": ["EMP001"],
        "Employee_Name": ["Amit"],
        "Department": ["IT"],
        "Tasks_Assigned": [20],
        "Tasks_Completed": [18],
        "Hours_Worked": [40]
    })

    result = process_employee_data(data)

    assert result["Completion_Percentage"].iloc[0] == 90.00
    assert result["Pending_Tasks"].iloc[0] == 2
import pandas as pd
import numpy as np


def load_employee_data():
    """
    Load employee data from CSV file.
    """

    file_path = "data/employees.csv"

    df = pd.read_csv(file_path)

    return df


def process_employee_data(df):
    """
    Clean employee data and calculate performance metrics.
    """

    # Remove rows containing missing values
    df = df.dropna()

    # Calculate task completion percentage
    df["Completion_Percentage"] = (
        df["Tasks_Completed"] / df["Tasks_Assigned"]
    ) * 100

    # Round percentage to 2 decimal places
    df["Completion_Percentage"] = np.round(
        df["Completion_Percentage"], 2
    )

    # Calculate pending tasks
    df["Pending_Tasks"] = (
        df["Tasks_Assigned"] - df["Tasks_Completed"]
    )

    return df


def generate_department_summary(df):
    """
    Generate department-wise performance summary.
    """

    summary = df.groupby("Department").agg(
        Total_Employees=("Employee_ID", "count"),
        Total_Tasks_Assigned=("Tasks_Assigned", "sum"),
        Total_Tasks_Completed=("Tasks_Completed", "sum"),
        Total_Hours_Worked=("Hours_Worked", "sum")
    ).reset_index()

    # Calculate department completion percentage
    summary["Completion_Percentage"] = (
        summary["Total_Tasks_Completed"]
        / summary["Total_Tasks_Assigned"]
    ) * 100

    summary["Completion_Percentage"] = np.round(
        summary["Completion_Percentage"], 2
    )

    return summary
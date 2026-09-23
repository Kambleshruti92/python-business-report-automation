# Python Business Report Automation System

A Python-based business reporting and automation application that processes employee data, provides REST APIs for searching and filtering employees, and automatically generates formatted Excel reports.

## Project Overview

The system automates a common business reporting workflow:

CSV Employee Data
        ↓
Python Data Processing
        ↓
Pandas + NumPy
        ↓
FastAPI REST APIs
        ↓
openpyxl Excel Report
        ↓
Automated Testing

The project demonstrates Python backend development, data processing, REST API development, Excel automation, error handling, and automated testing.

## Features

- Load employee data from CSV
- Clean and process data using Pandas
- Calculate employee task completion percentage
- Calculate pending tasks
- Generate department-wise performance summaries
- Search employees by name
- Filter employees by department
- REST APIs using FastAPI
- Generate formatted Excel reports automatically
- Excel borders, filters, frozen headers, and column formatting
- API error handling
- Automated testing using pytest

## Technologies Used

### Programming
- Python 3.11

### Data Processing
- Pandas
- NumPy

### Backend
- FastAPI
- Uvicorn
- REST APIs
- JSON

### Reporting
- openpyxl
- Excel automation

### Testing
- pytest
- FastAPI TestClient

### Development Tools
- Git
- GitHub
- VS Code

## Project Structure

```text
python-business-report-automation/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── data_processor.py
│   └── report_generator.py
│
├── data/
│   └── employees.csv
│
├── reports/
│   └── employee_performance_report.xlsx
│
├── tests/
│   ├── test_api.py
│   └── test_data_processor.py
│
├── .gitignore
├── requirements.txt
└── README.md
# Python Business Report Automation System

A Python-based business reporting and automation application that processes employee data, exposes REST APIs, automates Excel report generation, parses PDF reports, and provides a web-based dashboard with automated UI testing.

## Project Overview

The application demonstrates a complete business reporting workflow:

```text
Employee CSV Data
       ↓
Python Data Processing
       ↓
Pandas + NumPy
       ↓
FastAPI REST APIs
       ↓
Web Dashboard
       ↓
openpyxl Excel Automation
       ↓
PDF Parsing
       ↓
Automated API + UI Testing
```

The project was built to demonstrate practical Python development skills including data processing, backend API development, business report automation, document processing, testing, and Git-based version control.

## Features

* Load employee data from CSV
* Clean and process data using Pandas
* Calculate employee task completion percentage using NumPy
* Calculate pending tasks
* Generate department-wise performance summaries
* Search employees by name
* Filter employees by department
* Combine employee search and department filtering
* REST APIs using FastAPI
* Interactive web dashboard
* Generate and download formatted Excel reports
* Excel formatting using openpyxl
* PDF text extraction using pypdf
* API error handling
* Automated API and unit testing using pytest
* Browser-based UI automation using Selenium
* Git/GitHub version control

## Technologies Used

### Programming

* Python 3.11

### Data Processing

* Pandas
* NumPy

### Backend

* FastAPI
* Uvicorn
* REST APIs
* JSON

### Reporting & Document Processing

* openpyxl
* pypdf
* ReportLab

### Frontend

* HTML5
* CSS3
* JavaScript

### Testing

* pytest
* FastAPI TestClient
* Selenium WebDriver

### Development Tools

* Git
* GitHub
* VS Code

## Project Structure

```text
python-business-report-automation/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── data_processor.py
│   ├── report_generator.py
│   └── pdf_parser.py
│
├── data/
│   ├── employees.csv
│   ├── create_sample_pdf.py
│   └── pdfs/
│       └── business_report.pdf
│
├── reports/
│   └── employee_performance_report.xlsx
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── tests/
│   ├── test_api.py
│   ├── test_data_processor.py
│   ├── test_pdf_parser.py
│   └── selenium/
│       └── test_dashboard.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── venv/
```

> `venv/` and generated Excel reports are excluded from Git using `.gitignore`.

## Application Workflow

### 1. Employee Data Processing

The application reads employee information from a CSV file using Pandas.

The dataset contains:

* Employee ID
* Employee Name
* Department
* Tasks Assigned
* Tasks Completed
* Hours Worked

The application calculates:

```text
Completion Percentage =
(Tasks Completed / Tasks Assigned) × 100

Pending Tasks =
Tasks Assigned - Tasks Completed
```

### 2. Department Analysis

Employee records are grouped by department to calculate:

* Total employees
* Total tasks assigned
* Total tasks completed
* Total hours worked
* Department completion percentage

### 3. REST API

FastAPI provides endpoints for accessing employee information, filtering data, generating reports, and parsing PDF documents.

### 4. Web Dashboard

The frontend provides:

* Employee performance table
* Employee search
* Department filter
* Combined filtering
* Total employee count
* Department count
* Average completion percentage
* Excel report download
* API/report status messages

### 5. Excel Automation

The application generates a formatted Excel workbook containing:

**Employee Performance**

* Employee details
* Task information
* Completion percentage
* Pending tasks

**Department Summary**

* Department-level performance metrics

The workbook includes:

* Formatted headers
* Borders
* Column width adjustment
* Auto filters
* Frozen header rows
* Percentage formatting

### 6. PDF Processing

The application uses `pypdf` to extract text from PDF business reports.

The extracted content can be accessed through the FastAPI PDF parsing endpoint.

### 7. Automated Testing

The project contains API, data-processing, PDF parsing, and browser automation tests.

Current test coverage includes:

* API status
* Employee retrieval
* Department filtering
* Employee search
* Combined filters
* Invalid search handling
* Department summaries
* Excel report generation
* PDF parsing
* Data processing
* Selenium dashboard search
* Selenium department filtering
* Selenium Excel report generation

Current test result:

```text
15 passed
```

## API Endpoints

### API Status

```http
GET /api
```

Returns the API status.

### Get Employees

```http
GET /employees
```

Returns all employee records.

### Search Employees

```http
GET /employees?name=rah
```

Searches employees by name.

### Filter by Department

```http
GET /employees?department=IT
```

Returns employees belonging to the selected department.

### Combined Search and Filter

```http
GET /employees?name=rah&department=IT
```

Combines employee-name search with department filtering.

### Department Summary

```http
GET /departments
```

Returns department-level performance metrics.

### Generate Excel Report

```http
POST /generate-report
```

Generates a formatted Excel report from the selected employee records.

### Parse PDF

```http
GET /parse-pdf
```

Extracts text from the sample business PDF report.

## Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Kambleshruti92/python-business-report-automation.git
cd python-business-report-automation
```

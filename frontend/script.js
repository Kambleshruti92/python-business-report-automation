const API_BASE_URL = "";


// --------------------------------------------------
// Current Visible Employees
// --------------------------------------------------

// This variable always contains the records
// currently visible in the table.

let currentEmployees = [];


// --------------------------------------------------
// DOM Elements
// --------------------------------------------------

const employeeTableBody =
    document.getElementById("employeeTableBody");

const totalEmployeesElement =
    document.getElementById("totalEmployees");

const totalDepartmentsElement =
    document.getElementById("totalDepartments");

const averageCompletionElement =
    document.getElementById("averageCompletion");

const employeeCountElement =
    document.getElementById("employeeCount");

const searchInput =
    document.getElementById("searchInput");

const departmentFilter =
    document.getElementById("departmentFilter");

const searchButton =
    document.getElementById("searchButton");

const resetButton =
    document.getElementById("resetButton");

const generateReportButton =
    document.getElementById("generateReportButton");

const messageElement =
    document.getElementById("message");


// --------------------------------------------------
// Initial Load
// --------------------------------------------------

document.addEventListener(
    "DOMContentLoaded",
    function () {

        loadEmployees();

    }
);


// --------------------------------------------------
// Load All Employees
// --------------------------------------------------

async function loadEmployees() {

    showLoading();

    hideMessage();


    try {

        const response =
            await fetch(
                `${API_BASE_URL}/employees`
            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Unable to load employee data."
            );
        }


        // Store currently visible records
        currentEmployees =
            data.employees;


        displayEmployees(
            currentEmployees
        );


        updateDashboard(
            currentEmployees
        );


    } catch (error) {

        console.error(error);


        showError(
            error.message
        );


        currentEmployees = [];


        showEmptyState();

        updateDashboard([]);

        employeeCountElement.textContent =
            "0 employees";
    }
}


// --------------------------------------------------
// Search + Department Filter
// --------------------------------------------------

async function searchAndFilterEmployees() {

    const name =
        searchInput.value.trim();

    const department =
        departmentFilter.value;


    showLoading();

    hideMessage();


    try {

        const params =
            new URLSearchParams();


        // Add employee name
        if (name !== "") {

            params.append(
                "name",
                name
            );
        }


        // Add department
        if (department !== "") {

            params.append(
                "department",
                department
            );
        }


        const queryString =
            params.toString();


        let url =
            `${API_BASE_URL}/employees`;


        if (queryString !== "") {

            url += `?${queryString}`;
        }


        const response =
            await fetch(url);


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "No employee records found."
            );
        }


        // Store ONLY filtered records
        currentEmployees =
            data.employees;


        // Display ONLY filtered records
        displayEmployees(
            currentEmployees
        );


        updateDashboard(
            currentEmployees
        );


    } catch (error) {

        console.error(error);


        currentEmployees = [];


        showError(
            error.message
        );


        showEmptyState();

        updateDashboard([]);

        employeeCountElement.textContent =
            "0 employees";
    }
}


// --------------------------------------------------
// Display Employees
// --------------------------------------------------

function displayEmployees(employees) {

    employeeTableBody.innerHTML = "";


    if (!employees ||
        employees.length === 0) {

        showEmptyState();

        employeeCountElement.textContent =
            "0 employees";

        return;
    }


    employees.forEach(
        function (employee) {

            const row =
                document.createElement("tr");


            // Employee ID
            const employeeIdCell =
                document.createElement("td");

            employeeIdCell.textContent =
                employee.Employee_ID;


            // Employee Name
            const employeeNameCell =
                document.createElement("td");

            employeeNameCell.textContent =
                employee.Employee_Name;


            // Department
            const departmentCell =
                document.createElement("td");

            departmentCell.textContent =
                employee.Department;


            // Tasks Assigned
            const tasksAssignedCell =
                document.createElement("td");

            tasksAssignedCell.textContent =
                employee.Tasks_Assigned;


            // Tasks Completed
            const tasksCompletedCell =
                document.createElement("td");

            tasksCompletedCell.textContent =
                employee.Tasks_Completed;


            // Hours Worked
            const hoursWorkedCell =
                document.createElement("td");

            hoursWorkedCell.textContent =
                employee.Hours_Worked;


            // Completion Percentage
            const completionCell =
                document.createElement("td");

            const completion =
                Number(
                    employee.Completion_Percentage
                );


            completionCell.textContent =
                `${completion.toFixed(2)}%`;


            if (completion >= 90) {

                completionCell.classList.add(
                    "completion-high"
                );

            } else if (completion >= 75) {

                completionCell.classList.add(
                    "completion-medium"
                );

            } else {

                completionCell.classList.add(
                    "completion-low"
                );
            }


            // Pending Tasks
            const pendingTasksCell =
                document.createElement("td");

            pendingTasksCell.textContent =
                employee.Pending_Tasks;


            // Add cells to row
            row.appendChild(
                employeeIdCell
            );

            row.appendChild(
                employeeNameCell
            );

            row.appendChild(
                departmentCell
            );

            row.appendChild(
                tasksAssignedCell
            );

            row.appendChild(
                tasksCompletedCell
            );

            row.appendChild(
                hoursWorkedCell
            );

            row.appendChild(
                completionCell
            );

            row.appendChild(
                pendingTasksCell
            );


            // Add row to table
            employeeTableBody.appendChild(
                row
            );
        }
    );


    employeeCountElement.textContent =
        `${employees.length} employee` +
        `${employees.length === 1 ? "" : "s"}`;
}


// --------------------------------------------------
// Dashboard
// --------------------------------------------------

function updateDashboard(employees) {

    if (!employees ||
        employees.length === 0) {

        totalEmployeesElement.textContent =
            "0";

        totalDepartmentsElement.textContent =
            "0";

        averageCompletionElement.textContent =
            "0%";

        return;
    }


    // Total employees
    totalEmployeesElement.textContent =
        employees.length;


    // Unique departments
    const departments =
        new Set(
            employees.map(
                function (employee) {

                    return employee.Department;

                }
            )
        );


    totalDepartmentsElement.textContent =
        departments.size;


    // Average completion
    const totalCompletion =
        employees.reduce(
            function (total, employee) {

                return total +
                    Number(
                        employee.Completion_Percentage
                    );

            },
            0
        );


    const averageCompletion =
        totalCompletion /
        employees.length;


    averageCompletionElement.textContent =
        `${averageCompletion.toFixed(2)}%`;
}


// --------------------------------------------------
// Reset Filters
// --------------------------------------------------

function resetFilters() {

    searchInput.value = "";

    departmentFilter.value = "";

    hideMessage();

    loadEmployees();
}


// --------------------------------------------------
// Generate Filtered Excel Report
// --------------------------------------------------

async function generateReport() {

    // Prevent generating an empty report
    if (
        !currentEmployees ||
        currentEmployees.length === 0
    ) {

        showError(
            "There are no employee records to export."
        );

        return;
    }


    generateReportButton.disabled =
        true;

    generateReportButton.textContent =
        "Generating...";

    hideMessage();


    try {

        const response =
            await fetch(
                `${API_BASE_URL}/generate-report`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify(
                        currentEmployees
                    )
                }
            );


        if (!response.ok) {

            const errorData =
                await response.json();


            throw new Error(
                errorData.detail ||
                "Report generation failed."
            );
        }


        // Convert response to Excel Blob
        const blob =
            await response.blob();


        // Create temporary download URL
        const downloadUrl =
            window.URL.createObjectURL(
                blob
            );


        // Create download link
        const link =
            document.createElement("a");


        link.href =
            downloadUrl;


        link.download =
            "employee_performance_report.xlsx";


        document.body.appendChild(
            link
        );


        link.click();


        link.remove();


        window.URL.revokeObjectURL(
            downloadUrl
        );


        showSuccess(
            `Excel report downloaded with ` +
            `${currentEmployees.length} employee` +
            `${currentEmployees.length === 1 ? "" : "s"}.`
        );


    } catch (error) {

        console.error(error);


        showError(
            error.message
        );


    } finally {

        generateReportButton.disabled =
            false;

        generateReportButton.textContent =
            "Generate Excel Report";
    }
}


// --------------------------------------------------
// Loading State
// --------------------------------------------------

function showLoading() {

    employeeTableBody.innerHTML = `
        <tr>
            <td colspan="8" class="loading">
                Loading employee data...
            </td>
        </tr>
    `;
}


// --------------------------------------------------
// Empty State
// --------------------------------------------------

function showEmptyState() {

    employeeTableBody.innerHTML = `
        <tr>
            <td colspan="8" class="empty-state">
                No employee records found.
            </td>
        </tr>
    `;
}


// --------------------------------------------------
// Success Message
// --------------------------------------------------

function showSuccess(message) {

    messageElement.textContent =
        message;

    messageElement.className =
        "message success";
}


// --------------------------------------------------
// Error Message
// --------------------------------------------------

function showError(message) {

    messageElement.textContent =
        message;

    messageElement.className =
        "message error";
}


// --------------------------------------------------
// Hide Message
// --------------------------------------------------

function hideMessage() {

    messageElement.textContent =
        "";

    messageElement.className =
        "message";
}


// --------------------------------------------------
// Event Listeners
// --------------------------------------------------

searchButton.addEventListener(
    "click",
    searchAndFilterEmployees
);


resetButton.addEventListener(
    "click",
    resetFilters
);


// Department change
departmentFilter.addEventListener(
    "change",
    searchAndFilterEmployees
);


// Generate Excel
generateReportButton.addEventListener(
    "click",
    generateReport
);


// Search using Enter key
searchInput.addEventListener(
    "keydown",
    function (event) {

        if (event.key === "Enter") {

            searchAndFilterEmployees();

        }

    }
);
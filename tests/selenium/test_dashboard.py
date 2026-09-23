from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_driver():

    options = Options()

    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    return webdriver.Chrome(options=options)


def test_employee_search():

    driver = create_driver()

    try:

        driver.get("http://127.0.0.1:8000/")

        wait = WebDriverWait(driver, 10)

        search_input = wait.until(
            EC.presence_of_element_located(
                (By.ID, "searchInput")
            )
        )

        search_input.send_keys("Rahul")

        driver.find_element(
            By.ID,
            "searchButton"
        ).click()

        employee_name = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//tbody[@id='employeeTableBody']//td[2]"
                )
            )
        )

        assert employee_name.text == "Rahul"

    finally:

        driver.quit()


def test_department_filter():

    driver = create_driver()

    try:

        driver.get("http://127.0.0.1:8000/")

        wait = WebDriverWait(driver, 10)

        department_filter = wait.until(
            EC.presence_of_element_located(
                (By.ID, "departmentFilter")
            )
        )

        department_filter.click()

        department_filter.find_element(
            By.CSS_SELECTOR,
            "option[value='IT']"
        ).click()

        rows = wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.CSS_SELECTOR,
                    "#employeeTableBody tr"
                )
            )
        )

        assert len(rows) == 3

    finally:

        driver.quit()

def test_generate_excel_report():

    driver = create_driver()

    try:

        driver.get("http://127.0.0.1:8000/")

        wait = WebDriverWait(driver, 10)

        report_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "generateReportButton")
            )
        )

        report_button.click()

        success_message = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "message")
            )
        )

        assert "Excel report downloaded" in (
            success_message.text
        )

    finally:

        driver.quit()
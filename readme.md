# 🧪 Playwright Python Framework

This is a **modular, scalable end-to-end test automation framework** built using **Playwright with Python and Pytest**. 
It follows the **Page Object Model (POM)** design pattern and integrates with **CI tools like GitHub Actions and Jenkins** for continuous testing.

---

## 📁 Folder Structure
playwrightframework/
│
├── .github/workflows/         # GitHub Actions CI/CD workflows
├── .idea/                     # PyCharm IDE configuration files (can be ignored in Git)
├── database/                  # SQL scripts or DB-related files
├── pageObject/                # Page classes using Playwright locators and methods
├── tests/                     # Pytest test scripts organized by feature
├── utilities/                 # Helper functions, configs, and utilities
│
├── .gitignore                 # Git ignored files/folders
├── jenkins.groovy             # Jenkins pipeline Groovy script
├── pytest.ini                 # Pytest configuration (markers, logs, etc.)
├── readme.md                  # Project documentation
├── requirements.txt           # List of Python dependencies
├── test_results.csv           # Used for test data (optional)

---

## 📘 Folder Details

### 🔹 `.github/workflows/`
Contains GitHub Actions workflows (e.g., trigger tests on push/pull request).

### 🔹 `pageObject/`
Implements the **Page Object Model** where each page has its own class with element locators and related actions.

### 🔹 `tests/`
Holds all the **pytest test cases**, organized by functionality or module.

### 🔹 `utilities/`
Includes reusable helper methods such as:
- Config parser
- Logger setup
- Data generators
- Custom utilities

### 🔹 `database/`
Used for SQL files, mock data, and setup scripts if DB interaction is part of the tests.

---

## ⚙️ Key Files

| File             | Purpose                                                                 |
|------------------|-------------------------------------------------------------------------|
| `pytest.ini`      | Central config for test markers, logs, and Pytest behavior             |
| `requirements.txt`| Contains all required Python libraries and versions                    |
| `jenkins.groovy`  | Jenkins scripted pipeline for CI integration                           |
| `test_results.csv`| Optional – Used for test data                   |

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-user/playwrightframework.git
cd playwrightframework

2. Install dependencies
pip install -r requirements.txt
playwright install

3. Run all tests
pytest

4. Run a specific test
pytest -k "test_name"

5. Generate HTML report
pytest --html=report.html

#commands used for generating allure reports #

🔧 Step 1: Install Required Dependencies
pip install allure-pytest
🔧 Step 2: Run Pytest with Allure Result Directory
pytest --alluredir=allure-results
🔧 Step 3: Generate the HTML Report from Results
allure generate allure-results -o allure-report --clean
🔧 Step 4: Open the Report
allure open allure-report


## Tracing ##
>> To open and view the trace:
npx playwright show-trace trace.zip


📌 Tech Stack
	•	Language: Python 3.10+
	•	Automation Tool: Playwright (Python)
	•	Test Runner: Pytest
	•	Design Pattern: Page Object Model (POM)
	•	CI Tools: GitHub Actions, Jenkins
	•	Reporting: Pytest HTML (optional)



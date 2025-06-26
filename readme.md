### 🔧 Setup Instructions

```bash
pip install -r requirements.txt
playwright install


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



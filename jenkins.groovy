pipeline {
    agent any

    environment {
        PYTHON_BIN = '/Users/inderpreetsingh/Library/Python/3.9/bin'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git(
                    url: 'https://github.com/Inderqa/playwrightframework',
                    branch: 'main',
                    credentialsId: '03f71c7b-be5c-4892-bbda-9aa0c553ba68'
                )
            }
        }

        stage('Prepare Workspace') {
            steps {
                sh '''
                    echo "Current workspace path: $WORKSPACE"
                    ls -l
                '''
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    export PATH="$PYTHON_BIN:$PATH"
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    playwright install
                '''
            }
        }

        stage('Run Tests and Generate Allure Report') {
            steps {
                sh '''
                    source venv/bin/activate
                    pytest --alluredir=allure-results
                    allure generate allure-results -o allure-report --clean
                '''
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
        success {
            subject: "Jenkins Job SUCCESS: ${env.JOB_NAME} [#${env.BUILD_NUMBER}]"
            body: "Good news! The build succeeded.\n\nCheck report: ${env.BUILD_URL}"
        }

        failure {
            subject: "Jenkins Job FAILED: ${env.JOB_NAME} [#${env.BUILD_NUMBER}]"
            body: "Something went wrong in the build.\n\nCheck details: ${env.BUILD_URL}"
        }
    }
}
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Получение исходного кода проекта'
                checkout scm
            }
        }

        stage('Prepare environment') {
            steps {
                echo 'Проверка версии Python'
                bat 'python --version'
                bat 'python -m pip install --upgrade pip'
                bat 'pip install pytest'
            }
        }

        stage('Run tests') {
            steps {
                echo 'Запуск автоматизированных тестов'
                bat 'pytest -v'
            }
        }
    }

    post {
        success {
            echo 'CI pipeline успешно выполнен'
        }

        failure {
            echo 'CI pipeline завершился с ошибкой'
        }
    }
}
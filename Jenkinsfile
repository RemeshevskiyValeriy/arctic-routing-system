pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Получение исходного кода'
                checkout scm
            }
        }

        stage('Prepare environment') {
            steps {
                echo 'Создание виртуального окружения'
                sh 'python3 -m venv venv'
                sh './venv/bin/python -m pip install --upgrade pip'
                sh './venv/bin/pip install pytest'
            }
        }

        stage('Run tests') {
            steps {
                echo 'Запуск pytest'
                sh './venv/bin/pytest -v'
            }
        }
    }

    post {
        success {
            echo 'Pipeline успешно выполнен'
        }

        failure {
            echo 'Pipeline завершился с ошибкой'
        }
    }
}

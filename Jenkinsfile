
pipeline {
    agent any

    environment {
        DOCKER = 'C:\\Users\\iflin\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
        IMAGE_NAME = 'iflinajzahya/simple-app'
        REGISTRY_CREDENTIALS = 'dockerhub-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Kode berhasil diambil dari GitHub.'
            }
        }

        stage('Build') {
            steps {
                bat 'echo "Build di Windows"'
            }
        }
	stage('Database Integration Test') {
    steps {
        bat 'C:\\Users\\iflin\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe compose up --build -d'
        bat 'C:\\Users\\iflin\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe compose exec -T app python -c "import mysql.connector; c=mysql.connector.connect(host=\'db\', user=\'root\', password=\'\', database=\'simpleapp\'); print(\'DATABASE CONNECTED:\', c.database); c.close()"'
    }
}
        stage('Build Docker Image') {
            steps {
                bat '"%DOCKER%" build -t %IMAGE_NAME%:%BUILD_NUMBER% .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: REGISTRY_CREDENTIALS,
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    bat '''
                        @echo off
                        setlocal DisableDelayedExpansion
                        <nul set /p "=%DOCKER_PASS%" | "%DOCKER%" login -u "%DOCKER_USER%" --password-stdin
                        if errorlevel 1 exit /b 1
                    '''
                    bat '"%DOCKER%" push %IMAGE_NAME%:%BUILD_NUMBER%'
                    bat '"%DOCKER%" tag %IMAGE_NAME%:%BUILD_NUMBER% %IMAGE_NAME%:latest'
                    bat '"%DOCKER%" push %IMAGE_NAME%:latest'
                }
            }
        }
    }

    post {
        always {
            echo 'Selesai build.'
        }
    }
}

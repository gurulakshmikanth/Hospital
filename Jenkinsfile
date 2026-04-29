pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/Hospital.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python manage.py test'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t hospital-app .'
            }
        }

        stage('Deploy to OpenShift') {
            steps {
                sh 'oc rollout restart deployment/hospital -n kanth-project'
            }
        }
    }
}

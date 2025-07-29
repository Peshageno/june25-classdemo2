pipeline {
    agent any
    environment {
        VENV = 'venv'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Peshageno/june25-classdemo2.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                python3 -m venv $VENV
                . $VENV/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . $VENV/bin/activate
                pytest
                '''
            }
        }
    }
}

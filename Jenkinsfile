pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Test') {
   	   steps {
        	sh '''
        	bash -c "
        	python3 -m venv venv
        	source venv/bin/activate
        	pip install -r requirements.txt
        	pip install pytest
        	pytest tests/
        	"
        	'''
    	   }
	}

        stage('Deploy') {
            steps {
                sh 'docker compose up -d'
            }
        }
    }
}

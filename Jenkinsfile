
pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    triggers {
        // Backup polling; GitHub webhook provides faster triggering.
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh '''
                    python3 --version
                    python3 -m compileall -q calc.py
                    mkdir -p dist
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'python3 -m unittest discover -s . -p "test_*.py" -v'
            }
        }

        stage('Create Artifact') {
            steps {
                sh '''
                    tar -czf dist/calculator-${BUILD_NUMBER}.tar.gz \
                        calc.py test_calc.py
                '''
                archiveArtifacts artifacts: 'dist/*.tar.gz',
                                 fingerprint: true
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo 'Tests passed. Deploying tested artifact.'
                sh '''
                    echo "Artifact ready: dist/calculator-${BUILD_NUMBER}.tar.gz"
                    # Add your real deployment command here.
                '''
            }
        }
    }

    post {
        success {
            echo 'CI pipeline successful'
        }
        failure {
            echo 'Pipeline failed; deployment was not completed'
        }
    }
}

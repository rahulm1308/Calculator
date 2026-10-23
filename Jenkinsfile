
pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        APP_NAME = 'calculator'
        DEPLOY_DIR = '/opt/calculator'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git log -1 --oneline'
            }
        }

        stage('Build') {
            steps {
                sh '''
                    set -eu
                    python3 --version
                    python3 -m py_compile calc.py test_calc.py
                    mkdir -p dist
                    tar --exclude=.git --exclude=dist \
                        --exclude=__pycache__ \
                        -czf dist/calculator.tar.gz \
                        calc.py test_calc.py
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                sh '''
                    set -eu
                    python3 -m unittest -v test_calc
                '''
            }
        }

        stage('Archive Artifact') {
            steps {
                archiveArtifacts(
                    artifacts: 'dist/calculator.tar.gz',
                    fingerprint: true
                )
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
                expression {
                    return params.DEPLOY_TO_SERVER
                }
            }
            steps {
                sshagent(credentials: ['calculator-deploy-key']) {
                    sh '''
                        set -eu

                        scp -o StrictHostKeyChecking=yes \
                            dist/calculator.tar.gz \
                            "$DEPLOY_USER@$DEPLOY_HOST:/tmp/calculator.tar.gz"

                        ssh -o StrictHostKeyChecking=yes \
                            "$DEPLOY_USER@$DEPLOY_HOST" \
                            "sudo mkdir -p '$DEPLOY_DIR' &&
                             sudo tar -xzf /tmp/calculator.tar.gz \
                               -C '$DEPLOY_DIR' &&
                             sudo chmod 755 '$DEPLOY_DIR/calc.py' &&
                             rm -f /tmp/calculator.tar.gz"
                    '''
                }
            }
        }
    }

    parameters {
        booleanParam(
            name: 'DEPLOY_TO_SERVER',
            defaultValue: false,
            description: 'Deploy to the configured Linux server'
        )
    }

    post {
        always {
            echo "Pipeline finished: ${currentBuild.currentResult}"
        }
        success {
            echo 'Build, tests and enabled deployment completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}

pipeline {
    agent any

    environment {
        // Windows path for deployment (using backslashes)
        DEPLOY_DIR = "C:\\tmp\\flask_app_deployment"
    }

    stages {
        // --- STAGE 1: CLONE ---
        stage('Checkout Code') {
            steps {
                echo 'Step 1: Cloning Repository...'
                checkout scm
            }
        }

        // --- STAGE 2: INSTALL DEPENDENCIES ---
        stage('Install Dependencies') {
            steps {
                echo 'Step 2: Installing Python Dependencies...'
                // "bat" is for Windows. We also use "call" to activate the venv correctly.
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest
                '''
            }
        }

        // --- STAGE 3: RUN UNIT TESTS ---
        stage('Run Unit Tests') {
            steps {
                echo 'Step 3: Running Pytest...'
                bat '''
                    call venv\\Scripts\\activate
                    pytest --verbose --junitxml=test-results.xml
                '''
            }
        }

        // --- STAGE 4: BUILD (Package) ---
        stage('Build Artifact') {
            steps {
                echo 'Step 4: Packaging the App...'
                // Windows supports tar in newer versions, or we can just echo for simplicity
                bat 'tar -czf flask_app_v1.tar.gz --exclude=venv --exclude=.git .'
                
                archiveArtifacts artifacts: 'flask_app_v1.tar.gz', allowEmptyArchive: true
            }
        }

        // --- STAGE 5: DEPLOY ---
        stage('Deploy App') {
            steps {
                echo "Step 5: Deploying to ${DEPLOY_DIR}..."
                bat '''
                    if not exist "%DEPLOY_DIR%" mkdir "%DEPLOY_DIR%"
                    tar -xzf flask_app_v1.tar.gz -C "%DEPLOY_DIR%"
                    echo DEPLOYMENT SUCCESS
                '''
            }
        }
    }
}

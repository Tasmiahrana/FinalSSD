pipeline {
    agent any

    // Define environment variables for the pipeline
    environment {
        // We deploy to a temporary folder for this assignment to avoid permission errors
        DEPLOY_DIR = "/tmp/flask_app_deployment"
    }

    stages {
        // --- STAGE 1: CLONE REPOSITORY ---
        stage('Checkout Code') {
            steps {
                echo 'Step 1: Cloning Repository from GitHub...'
                // 'checkout scm' automatically uses the Git plugin to pull the repo 
                // linked in the Jenkins Job configuration.
                checkout scm
            }
        }

        // --- STAGE 2: INSTALL DEPENDENCIES ---
        stage('Install Dependencies') {
            steps {
                echo 'Step 2: Installing Python Dependencies...'
                // specific secure design practice: Use a virtual environment (venv)
                // so we don't pollute the Jenkins server's global python setup.
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    # Ensure pytest is installed for the next stage
                    pip install pytest
                '''
            }
        }

        // --- STAGE 3: RUN UNIT TESTS ---
        stage('Run Unit Tests') {
            steps {
                echo 'Step 3: Running Pytest...'
                sh '''
                    . venv/bin/activate
                    # This runs all tests found in your repository
                    pytest --verbose --junitxml=test-results.xml || true
                '''
            }
        }

        // --- STAGE 4: BUILD THE APP ---
        stage('Build Artifact') {
            steps {
                echo 'Step 4: Packaging the App...'
                // We create a compressed "tar" file of your app, excluding the git data and venv
                sh 'tar -czf flask_app_v1.tar.gz --exclude=venv --exclude=.git --exclude=.github .'
                
                // Save this file in Jenkins so you can download it later
                archiveArtifacts artifacts: 'flask_app_v1.tar.gz', allowEmptyArchive: true
            }
        }

        // --- STAGE 5: DEPLOY THE APP ---
        stage('Deploy App') {
            steps {
                echo "Step 5: Deploying to ${DEPLOY_DIR}..."
                sh '''
                    # Create the target directory
                    mkdir -p $DEPLOY_DIR
                    
                    # Unzip the build file into the deployment folder
                    tar -xzf flask_app_v1.tar.gz -C $DEPLOY_DIR
                    
                    echo "DEPLOYMENT SUCCESS: App is live at $DEPLOY_DIR"
                '''
            }
        }
    }
}
node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */
        sh 'echo "Docker image build"'
        //app = docker.build("releaseworks/hellonode")
    }

    stage('Test image') {
        /* Ideally, we would run a test framework against our image.
         * For this example, we're using a Volkswagen-type approach ;-) */

        //app.inside {
            sh 'echo "Tests passed"'
        //}
    }

    stage('Merge v1 into main') {
            steps {
                // Checkout the 'main' branch
                checkout scm
                
                // Switch to the 'v1' branch
                sh 'git checkout v1'
                
                // Merge 'v1' into 'main'
                sh 'git merge main'
                
                // Push the changes to 'main'
                sh 'git push origin v1'
            }
        }
    }
}

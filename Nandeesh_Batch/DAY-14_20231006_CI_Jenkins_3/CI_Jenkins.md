##### Session Video:
    https://drive.google.com/file/d/1zff9NZ3Xr3ntu-yZFJWn7SU6_HMkrmpd/view?usp=sharing  

#### Jenkins Setup

https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html

https://www.jenkins.io/

https://www.jenkins.io/doc/

https://www.jenkins.io/doc/book/installing/

https://www.jenkins.io/doc/book/installing/windows/



```

node {
   def mvnHome

  stage('Prepare') {
      git url: 'https://github.com/kesavkummari/cb9amjava.git', branch: 'b109am'
      mvnHome = tool 'maven'
   }
  stage ('Clean') {
      sh "'${mvnHome}/bin/mvn'  clean"
  }
  stage ('Validate') {
      sh "'${mvnHome}/bin/mvn'  validate"
  }
  stage ('Compile') {
      sh "'${mvnHome}/bin/mvn'  compile"
  }
  stage ('Test') {
      sh "'${mvnHome}/bin/mvn'  test"
  }
  stage ('Package') {
      sh "'${mvnHome}/bin/mvn'  package"
  }
  stage ('Verify') {
      sh "'${mvnHome}/bin/mvn'  verify"
  }
  stage ('Install') {
      sh "'${mvnHome}/bin/mvn'  install"
  }
}

```

```
pipeline {
    agent any

    tools {
        // Configure the JDK and Maven tools
        jdk 'JDK'
        maven 'Maven'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from a version control system
                // For example, from a Git repository:
                git 'https://github.com/username/repo.git'
            }
        }

        stage('Build') {
            steps {
                // Build the application using Maven
                sh 'mvn clean package'
            }
        }

        stage('Test') {
            steps {
                // Run unit and integration tests
                sh 'mvn test'
            }
        }

        stage('Deploy') {
            steps {
                // Deploy the application to a test environment
                sh 'mvn deploy'
            }
        }
    }
}

```
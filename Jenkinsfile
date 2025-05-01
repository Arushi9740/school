pipeline{
    agent any
    stages{
        stage("git clone"){
            steps{
                echo "cloning to git"
                git url : 'https://github.com/Arushi9740/school.git', branch : 'main'
            }
        }
        stage("setup dependency"){
            echo "Installing dependencies"
            bat '''
            python -m venv venv
            pip install --upgrade pip
            call venv\\Scripts\\activate
            pip install pytest
            '''
        }
        stage("function"){
            echo "function testing"
            bat '''
            call venv\\Scripts\\activate
            python students.py
            '''
        }
        stage("testing"){
            echo "testing stage"
            bat'''
            call venv\\Scripts\\activate
            pytest test_file.py
            '''
        }
    }
}
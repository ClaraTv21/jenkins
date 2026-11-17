pipeline {
    agent any
    triggers {
    githubPush()              // roda quando o GitHub avisar
    pollSCM('H/5 * * * *')    // reserva: confere a cada 5 min, caso o aviso falhe
        }triggers { pollSCM('* * * * *') }   // verifica o repo a cada minuto
    stages {
        stage('Testes') {
            steps { sh 'python3 -m unittest -v' }
        }
        stage('Build') {
            steps {
                sh 'mkdir -p dist && tar czf dist/app.tar.gz *.py'
                archiveArtifacts artifacts: 'dist/*.tar.gz'
            }
        }
        stage('Deploy') {
            steps { echo 'Deploy simulado para produção 🚀' }
        }
    }
}
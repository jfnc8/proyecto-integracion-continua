pipeline {
    agent any

    options {
        disableConcurrentBuilds()
    }

    stages {
        stage('Construir e iniciar servicios') {
            steps {
                bat 'git rev-parse --short HEAD'
                bat 'docker compose -p jenkins-dashboard up -d --build'
            }
        }

        stage('Verificar Flask y MySQL') {
            steps {
                powershell '''
                    for ($intento = 1; $intento -le 30; $intento++) {
                        try {
                            $salud = Invoke-RestMethod `
                                -Uri 'http://localhost:5000/api/salud' `
                                -TimeoutSec 5 -ErrorAction Stop

                            if ($salud.mysql -eq 'conectado') {
                                Write-Output 'Flask y MySQL conectados'
                                exit 0
                            }
                        } catch {
                            Write-Output "Esperando a Flask ($intento/30)"
                        }

                        Start-Sleep -Seconds 2
                    }

                    docker compose -p jenkins-dashboard logs
                    throw 'La API no confirmo la conexion con MySQL'
                '''
            }
        }

        stage('Verificar dashboard y usuarios') {
            steps {
                powershell '''
                    $dashboard = Invoke-WebRequest -UseBasicParsing `
                        -Uri 'http://localhost:5000/salud' `
                        -TimeoutSec 10 -ErrorAction Stop

                    if ($dashboard.Content -notmatch 'Monitor de servicios') {
                        throw 'No se encontro el texto esperado en el dashboard'
                    }

                    Write-Output 'Dashboard funcionando'
                '''
                bat 'py -3 tests/test_usuarios.py'
            }
        }
    }

    post {
        always {
            bat 'docker compose -p jenkins-dashboard down'
        }
    }
}
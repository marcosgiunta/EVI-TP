#config.py
class DevelopmentConfig():
    DEBUG=True #debug=true es para hacer pruebas en modo desarrollador sin tener que reiniciar el servidor
    MYSQL_HOST='db'
    MYSQL_USER='root'
    MYSQL_PASSWORD='root'
    MYSQL_DB='tp_evi_api'

config = {

 'development' : DevelopmentConfig

}    
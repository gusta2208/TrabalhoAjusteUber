import mysql.connector
from mysql.connector import errorcode

def conectar():
    try:
        db_connection = mysql.connector.connect(host= 'localhost', user = 'root', password = '', database='bancoUber' )
        print("Conectado com Sucesso!!")
        return db_connection
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_BD_ERROR: #salvado o erro na variavel error
            print("Banco De Dados não existe!") #caso banco de dados não exista
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR: #caso haja um erro de usuário
            print("Nome ou Usuário ou Senha inválidos!")
        else:
            print(error)
    else:
        db_connection.close()
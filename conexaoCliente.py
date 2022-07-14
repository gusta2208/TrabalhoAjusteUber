import mysql.connector
import this


import conexao
this.contador = 0
db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()


def loginValidado(cpf):
    try:
        sql = "select senha from cliente where cpf = '{}';".format(cpf)
        con.execute(sql)
        db_connection.commit()
        for (senha) in con:
            print(senha[0])
            if this.senha == senha[0]:
                print
    except Exception as erro:
        print(erro)
    print("CPF ou senha inválidos ou não cadastrados, tente novamente!!")



def loginCliente(cpf, senha):
    try:
        sql = "select senha from cliente where cpf = '{}';".format(cpf, senha)
        con.execute(sql)

        for (senha) in con:
            if this.senha == senha[this.contador]:
                permissao = True
            else:
                permissao = False
            this.contador += 1
        return permissao
    except Exception as erro:
        print




def inserir(cpf, nome, telefone, endereco, dataNascimento, senha):
    try:
        if (cpf != "") and (nome != "") and (telefone != "") and (endereco != "") and (dataNascimento != "") and (senha != ""):
            sql = "insert into cliente(cpf, nome, telefone, endereco, dataNascimento, senha) values('{}','{}','{}','{}','{}','{}')".format(
                cpf, nome, telefone, endereco, dataNascimento, senha)
            con.execute(sql)  # Prepara o comando para ser executado
            db_connection.commit()  # Executa o comando no banco de dados
            return "Cadastrado!"
        else:
            return "Preencha todos os campos!"
    except Exception as erro:
        print(erro)


# Consultar os dados do BD
def selecionar():
    try:
        sql = "select * from cliente"
        con.execute(sql)

        for (codigo, cpf, nome, telefone, endereco, dataNascimento) in con:
            print(codigo, nome, telefone, endereco, dataNascimento)
        print('\n')
    except Exception as erro:
        print(erro)


def atualizar(cpf, campo, novoDado):
    try:
        sql = "update cliente set {} = '{}' where cpf = '{}'".format(campo, novoDado, cpf)
        con.execute(sql)
        db_connection.commit()
        return "{} Atualizado!".format(con.rowcount)
    except Exception as erro:
        return erro

def consultar(cpf):
    try:
        if (cpf != ""):
            sql = "select * from cliente where cpf = '{}'".format(cpf)
            con.execute(sql)

            this.msg = ""
            this.msg = "Nenhum dado Encontrado!"
            for(cpf, nome, telefone, endereco, dataDeNascimento, senha) in con:
                if int(cpf) == int(cpf):
                    this.msg = "Cpf: {}, Nome: {}, Telefone: {}, Endereço: {}, Data de Nascimento: {}, Senha: {},"  .format(cpf, nome, telefone, endereco, dataDeNascimento, senha)
                    return this.msg
            return this.msg
    except Exception as erro:
        this.msg = ""
        return erro


def deletar(cpf):
    try:
        sql = "delete from cliente where cpf = '{}'".format(cpf)
        con.execute(sql)
        db_connection.commit()
        return "{} deletado!".format(con.rowcount)
    except Exception as erro:
        return erro


def transformarData(texto):
    separado = texto.split('/')
    dia = separado[0]
    mes = separado[1]
    ano = separado[2]
    return '{}-{}-{}'.format(ano, mes, dia)
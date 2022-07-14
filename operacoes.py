import mysql.connector
import this

import conexao
this.contador = 0
this.msg = ""
db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def loginValidado(cpf, senha):
    print("Informe seu CPF: ")
    this.cpf = input()
    print("Informe sua Senha: ")
    this.senha = input()
    try:
        sql = "select senha from cliente where cpf = '{}';".format(this.cpf)
        con.execute(sql) # prepara o comando para ser executado

        for (senha) in con:
            print(senha[0])
            if this.senha == senha[0]:
                print(cliente.bemVindo())
    except Exception as erro:
        print(erro)
    print("CPF ou senha inválidos ou não cadastrados, tente novamente!!")
    loginValidado(cpf, senha)
def loginValidadoMotorista(cpf, senha):
    print("Informe seu CPF: ")
    this.cpf = input()
    print("Informe sua Senha: ")
    this.senha = input()
    try:
        sql = "select senha from motorista where cpf = '{}';".format(this.cpf)
        con.execute(sql) # prepara o comando para ser executado

        for (senha) in con:
            print(senha[0])
            if this.senha == senha[0]:
                print(login())
    except Exception as erro:
        print(erro)
    print("CPF ou senha inválidos ou não cadastrados, tente novamente!!")
    loginValidado(cpf, senha)

def cadastrarMotorista(cpf, nome, telefone, endereco, modelo, placa, dataNascimento, senha):
    try:
        sql = "insert into motorista (cpf, nome, telefone, endereco, modelo, placa, dataNascimento, senha) values ('{}','{}','{}','{}','{}','{}','{}','{}')".format(cpf, nome, telefone, endereco, modelo, placa, dataNascimento, senha)
        con.execute(sql) # prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
        print(con.rowcount, "Inserido!!")
    except Exception as erro:
        print(erro)

def atualizar(cpf, campo, novoDado):
    try:
        sql = "update motorista set {} = '{}' where cpf = '{}'".format(campo, novoDado, cpf)
        con.execute(sql)
        db_connection.commit()
        return "{} Atualizado!".format(con.rowcount)
    except Exception as erro:
        return erro

def consultar(cpf):
    try:
        sql = "select * from motorista where cpf = '{}'".format(cpf)
        con.execute(sql)

        this.msg = ""
        this.msg = "Nenhum dado Encontrado!"
        for(cpf, nome, telefone, endereco, modelo, placa, dataDeNascimento, senha) in con:
            if int(cpf) == int(cpf):
                this.msg = "Cpf: {} / Nome: {} / Telefone: {} / Endereço: {} / Modelo: {} / Placa: {} / Data de Nascimento: {} / Senha: {}"  .format(cpf, nome, telefone, endereco, modelo, placa, dataDeNascimento, senha)
                return this.msg
        return this.msg
    except Exception as erro:
        return erro

def deletar(cpf):
    try:
        sql = "delete from motorista where cpf = '{}'".format(cpf)
        con.execute(sql)
        db_connection.commit()
        return "{} deletado!".format(con.rowcount)
    except Exception as erro:
        return erro


def atualizarMotorista():
    print("   O Que Deseja Atualizar?   \n")

    print("1. Nome\n" +
          "2. Telefone\n"+
          "3. Endereço\n" +
          "4. Modelo do veiculo\n" +
          "5. Placa do veiculo\n" +
          "6. Data De Nascimento\n")
    this.opcao = int(input())
    try:
        while this.opcao != 8:
            if this.opcao == 1:
                print("Informe seu CPF: ")
                CPF = input()
                print("Informe o novo Nome: ")
                nome = input()
                atualizarNomeMotorista(CPF, nome)
            elif this.opcao == 2:
                print("Informe seu CPF: ")
                CPF = input()
                print("Informe o novo Telefone: ")
                telefone = input()
                atualizarTelefoneMotorista(CPF, telefone)
            elif this.opcao == 3:
                print("Informe seu CPF: ")
                CPF = input()
                print("Informe o novo Endereço: ")
                endereco = input()
                atualizarEnderecoMotorista(CPF, endereco)
            elif this.opcao == 4:
                print("Informe seu CPF: ")
                CPF = input()
                print("Informe o novo Modelo do veiculo: ")
                modelo = input()
                atualizarModeloMotorista(CPF, modelo)
            elif this.opcao == 5:
                print("Informe seu CPF: ")
                CPF = input()
                print("Informe a nova Placa: ")
                placa = input()
                atualizarPlacaMotorista(CPF, placa)
            elif this.opcao == 6:
                print("Informe seu CPF: ")
                CPF = input()
                print("Informe a nova Data De Nascimento ")
                dataDeNascimento = input()
                atualizarDataMotorista(CPF, dataDeNascimento)
            else:
                print('\nSelecione uma opção válida!!!\n')
                atualizarMotorista()
    except:
        print('\nSelecione uma opção válida!!!\n')
        atualizarMotorista()
def login():
    print("1. Consultar Cadastro \n" +
          "2. Alterar Dados\n" +
          "3. Deletar Conta\n" +
          "4. Disponível \n" +
          "5. Indisponível\n" +
          "0. Sair \n")
    this.opcaoLogin = int(input())
    try:
        while this.opcaoLogin != 7:
            if this.opcaoLogin == 1:
                print("Informe o CPF que deseja Consultar:")
                CPF = int(input())
                consultarMotorista(CPF)
            elif this.opcaoLogin == 2:
                atualizarMotorista()
            elif this.opcaoLogin == 3:
                print("Informe seu CPF: ")
                CPF = input()
                excluirMotorista(CPF)
            elif this.opcaoLogin == 4:
                print("Agora você está disponível para receber novas corridas!")

                login()

            elif this.opcaoLogin == 5:
                print("Você está Indisponivel para receber corridas!")
                login()

            else:
                print("\nSelecione uma opção válida!!!\n")
                login()
    except:
        print('\nSelecione uma opção válida!!!\n')
        login()
from classe import *
from funcoes import *
from os import system
from login import login
from login import *

#Douglas
login.login()

initial()


while True:
    retorno = options() 

    if retorno == "3":
        # Jeff
        while True:
            print("Deseja verifica a matricula do aluno")
            matricula = input("Matricula:")
            while matricula.isnumeric() == False:
                    print("Matricula deve conter somente números\nTente Novamente")
                    matricula = input("Matricula: ")

            aluno = Alunos(None,None,matricula,None,None,None)
            aluno.relatorio()

            reiniciar = input("Deseja verificar mais algum cadastro?\n(S/N): ")
            if reiniciar.lower() !="s":
                break
        
    elif retorno == "1":
        # Jeff
        while True:
            print("Cadastre um aluno aqui")
            matricula = input("Matricula: ")

            while matricula.isnumeric() == False:
                print("Matricula deve conter somente números\nTente Novamente")
                matricula = input("Matricula: ")

            nome = input("Nome: ")
            data_nascimento= data()
            turma = escolher_turma()
            sexo = escolher_sexo()
            modalidade = escolher_modalidade()

            aluno = Alunos(nome, data_nascimento.strftime("%d/%m/%Y"), matricula, turma, sexo, modalidade)
            aluno.cad()

            reiniciar = input("Deseja fazer mais algum cadastro?\n(S/N): ")
            if reiniciar.lower() !="s":
                break

    elif retorno == "4": 
        # Jeff
        while True:
            system('cls')
            print("Ok, vamos alterar um cadastro")
            matricula = input("Insira o número de matricula do aluno que deseja alterar\nR: ")
            while matricula.isnumeric() == False:
                print("Matricula deve conter somente números\nTente Novamente")
                matricula = input("Insira o número de matricula do aluno que deseja alterar\nR: ")
            aluno = Alunos(None, None, matricula, None, None, None)
            aluno.alterar_dados()

            reiniciar = input("Deseja alterar mais algum cadastro?\n(S/N): ")
            if reiniciar.lower() !="s":
                break

    elif retorno == "5":
        relatorio_geral()
from classe import *
from funcoes import *
from os import system
from login import login
from login import *
from datetime import datetime


i = 0
a = 0

login.login()


retorno = initial()


if retorno == "3":
    print("Deseja verifica a matricula do aluno")
    matricula = input("Matricula:")
    aluno = Alunos(None,None,matricula,None,None,None)
    aluno.relatorio()
   
        

elif retorno == "1":
    def data():
        while True:
            data_str = input("Digite sua data de nascimento (DD/MM/AAAA): ")
            try:
                data = datetime.strptime(data_str, "%d/%m/%Y")
                return data
            except ValueError:
                print("Formato inválido. Digite a data no formato DD/MM/AAAA.")

    
    while True:
        print("Cadastre o aluno aqui")
        matricula = input("Matricula: ")
        nome = input("Nome: ")
        data_nascimento= data()
        turma = escolher_turma()
        sexo = input("Sexo: ")
        modalidade = input("Modalidade: ")

        aluno = Alunos(nome, data_nascimento.strftime("%d/%m/%Y"), matricula, turma, sexo, modalidade)
        aluno.cad()
        reiniciar = input("Deseja fazer mais algum relatorio?\n (S/N): ")
        if reiniciar.lower() !="s":
            break


elif retorno == "4":
    system('cls')
    print("Ok, vamos alterar um cadastro")
    matricula = input("Insira o número de matricula do aluno que deseja alterar\nR: ")
    aluno = Alunos(None, None, matricula, None, None, None)
    aluno.alterar_dado_aluno()
from classe import *
from funcoes import *
from os import system
from login import login
from login import *


def relatorio():   
    global alunos_Cadastrados
    relatorio = input("deseja gerar um relatório:\n[1]Sim\n[2]Não\n")
    system('cls')
    while True:
        if relatorio == '1':
            text("Relatório_dos_alunos_cadastrados\n")
            for i in range(len(alunos_Cadastrados)):
                alunos_Cadastrados[i].exibir2()

        elif relatorio == '2':
            text("Finalizando....")
            break

        while relatorio != '1' and relatorio != '2':
            relatorio = input("deseja gerar um relatório:\n[1]Sim\n[2]Não\n")
            system('cls')

            if relatorio == '1':
                text("Relatório_dos_alunos_cadastrados\n")
                for i in range(len(alunos_Cadastrados)):
                    alunos_Cadastrados[i].exibir2()
                break

            elif relatorio == '2':
                text("Finalizando....")
                break
        break

# DOIDEIRA DO ROBSON
i = 0
a = 0
alunos_Cadastrados = []
login.login()


retorno = initial()


if retorno == "3":
    print("Deseja verifica a matricula do aluno")
    matricula = input("Matricula:")
    aluno = Alunos(None,None,matricula,None,None,None)
    aluno.relatorio()

elif retorno == "1":
    print("Cadastre o aluno aqui")
    matricula = input("Matricula: ")
    nome = input("Nome: ")
    data = input("Data: ")
    turma = input("Turma: ")
    sexo = input("Sexo: ")
    modalidade = input("Modalidade: ")

    aluno = Alunos(nome, data, matricula, turma, sexo, modalidade)
    aluno.cad()
    
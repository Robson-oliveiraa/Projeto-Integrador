from classe import *
from funcoes import *
from os import system
from login import login
from login import *

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
    print("Cadastre o aluno aqui")
    matricula = input("Matricula: ")
    nome = input("Nome: ")
    data = input("Data: ")
    turma = escolher_turma()
    sexo = input("Sexo: ")
    modalidade = input("Modalidade: ")

    aluno = Alunos(nome, data, matricula, turma, sexo, modalidade)
    aluno.cad()

elif retorno == "4":
    system('cls')
    print("Ok, vamos alterar um cadastro")
    matricula = input("Insira o número de matricula do aluno que deseja alterar\nR: ")
    aluno = Alunos(None, None, matricula, None, None, None)
    aluno.alterar_dado_aluno()
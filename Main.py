from Classe import *
from Funções import *
from os import system

i = 0
valor = 0
Alunos_Cadastrados = []
while True:
    nome = input('Nome do Aluno:\n')
    data_N = input('Data de Nascimento do Aluno:\n')
    n_Matricula = input('Nº da Matricula do Aluno:\n')
    turma = input('Turma e Turno do Aluno:\n')
    sexo = input('Sexo do Aluno:\n')
    system('cls')

    valor = Cadastro(nome,data_N,n_Matricula,turma,sexo)
    Alunos_Cadastrados.insert(i, valor)
    valor =+ 1
    i =+ 1

    escolhar = input('Deseja adicionar outro aluno?\n[1] Sim\n[2] Não\n')
    system('cls')
    if escolhar == '2':
        break

for i in range(len(Alunos_Cadastrados)):
    Alunos_Cadastrados[i].exibir()

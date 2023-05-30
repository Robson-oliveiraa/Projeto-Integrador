from Classe import *
from Funções import *

i = 0
valor = 0
Alunos_Cadastrados = []
while True:
    nome = input('Nome do Aluno:\n')
    data_N = input('Data de Nascimento do Aluno:\n')
    n_Matricula = input('Nº da Matricula do Aluno:\n')
    turma = input('Turma e Turno do Aluno:\n')
    sexo = input('Sexo do Aluno:\n')

    valor = Cadastro(nome,data_N,n_Matricula,turma,sexo)
    valor =+ 1
    Alunos_Cadastrados.insert(i, valor)
    i =+ 1

    escolhar = input('Deseja adicionar outro aluno?\n[1] Sim\n[2] Não\n')
    if escolhar == '2':
        break

for Atleta in list(Alunos_Cadastrados):
    print(Atleta)
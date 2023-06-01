from Classe import *
from Funções import *
from os import system

i = 0
valor = 0
cancelar = 0
Alunos_Cadastrados = []
while True:
    if cancelar == 1:
        break
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
    if escolhar == '1':
        continue
    elif escolhar == '2':
        break
    while escolhar != '1' and escolhar != '2':
        escolhar = input('Deseja adicionar outro aluno?\n[1] Sim\n[2] Não\n')
        system('cls')
        if escolhar == '1':
            continue
        elif escolhar == '2':
            cancelar += 1
            break

for i in range(len(Alunos_Cadastrados)):
    Alunos_Cadastrados[i].exibir()
    while True:
        info = input('Deseja alterar alguma informação do aluno?\n[1] Sim\n[2] Não\n')
        while info != '1' and info != '2':
            info = input('Deseja alterar alguma informação do aluno?\n[1] Sim\n[2] Não\n')
            if info == '2':
                break
        if info == '1':
            modaca = input('Qual informação deseja alterar\n[1] Nome\n[2] Data Nasc.\n[3] Nº Matri.\n[4] Turma\Turno\n[5] Sexo\n')
            indice = ['1','2','3','4','5']
            while modaca not in indice:
                modaca = input('Qual informação deseja alterar\n[1] Nome\n[2] Data Nasc.\n[3] Nº Matri.\n[4] Turma\Turno\n[5] Sexo\n')
            if modaca == indice[0]:
                nome = input('Nome do Aluno:\n')
                Alunos_Cadastrados[i].setNome(nome)
                Alunos_Cadastrados[i].exibir()

            elif modaca == indice[1]:
                data_N = input('Data de Nascimento do Aluno:\n')
                Alunos_Cadastrados[i].setData_N(data_N)
                Alunos_Cadastrados[i].exibir()

            elif modaca == indice[2]:
                n_Matricula = input('Nº da Matricula do Aluno:\n')
                Alunos_Cadastrados[i].setN_Matricula(n_Matricula)
                Alunos_Cadastrados[i].exibir()

            elif modaca == indice[3]:
                turma = input('Turma e Turno do Aluno:\n')
                Alunos_Cadastrados[i].setTurma(turma)
                Alunos_Cadastrados[i].exibir()

            elif modaca == indice[4]:
                sexo = input('Sexo do Aluno:\n')
                Alunos_Cadastrados[i].setSexo(sexo)
                Alunos_Cadastrados[i].exibir()
        elif info == '2':
            break

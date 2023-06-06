from classe import *
from funcoes import *
from os import system

# DOIDEIRA DO ROBSON
i = 0
cancelar = 0
alunos_Cadastrados = []

while True:
    if cancelar == 1:
        break
    nome = input('Nome do Aluno:\n')
    data_N = input('Data de Nascimento do Aluno:\n')
    n_Matricula = input('Nº da Matricula do Aluno:\n')
    turma = input('Turma e Turno do Aluno:\n')
    sexo = input('Sexo do Aluno:\n')
    system('cls')

    Atleta = cadastro(nome,data_N,n_Matricula,turma,sexo)
    alunos_Cadastrados.insert(i, Atleta)
    i =+ 1

    escolha = input('Deseja adicionar outro aluno?\n[1] Sim\n[2] Não\n')
    system('cls')
    if escolha == '1':
        continue
    elif escolha == '2':
        break
    while escolha != '1' and escolha != '2':
        escolha = input('Deseja adicionar outro aluno?\n[1] Sim\n[2] Não\n')
        system('cls')
        if escolha == '1':
            break
        elif escolha == '2':
            cancelar = 1
            break

for i in range(len(alunos_Cadastrados)):
    alunos_Cadastrados[i].exibir()
    while True:
        info = input('Deseja alterar alguma informação?\n[1] Sim\n[2] Não\n')
        while info != '1' and info != '2':
            info = input('Deseja alterar alguma informação?\n[1] Sim\n[2] Não\n')
            if info == '2':
                break
        if info == '1':
            modaca = input('Qual informação deseja alterar\n[1] Nome\n[2] Data Nasc.\n[3] Nº Matri.\n[4] Turma\Turno\n[5] Sexo\n')
            indice = ['1','2','3','4','5']
            while modaca not in indice:
                modaca = input('Qual informação deseja alterar\n[1] Nome\n[2] Data Nasc.\n[3] Nº Matri.\n[4] Turma\Turno\n[5] Sexo\n')
            if modaca == indice[0]:
                nome = input('Nome do Aluno:\n')
                alunos_Cadastrados[i].setNome(nome)
                alunos_Cadastrados[i].exibir()

            elif modaca == indice[1]:
                data_N = input('Data de Nascimento do Aluno:\n')
                alunos_Cadastrados[i].setData_N(data_N)
                alunos_Cadastrados[i].exibir()

            elif modaca == indice[2]:
                n_Matricula = input('Nº da Matricula do Aluno:\n')
                alunos_Cadastrados[i].setN_Matricula(n_Matricula)
                alunos_Cadastrados[i].exibir()

            elif modaca == indice[3]:
                turma = input('Turma e Turno do Aluno:\n')
                alunos_Cadastrados[i].setTurma(turma)
                alunos_Cadastrados[i].exibir()

            elif modaca == indice[4]:
                sexo = input('Sexo do Aluno:\n')
                alunos_Cadastrados[i].setSexo(sexo)
                alunos_Cadastrados[i].exibir()
        elif info == '2':
            break
i = 0
with open('main.txt','w') as cadastros:
    for cadastrodos in alunos_Cadastrados:
        i += 1
        cadastros.write(cadastrodos.info(str(i)))
from sys import stdout
from time import sleep
from os import system
from datetime import datetime
import DataBaserAlunos

def text(txt):
    for letra in list(txt):
        print(letra, end = '')
        stdout.flush()
        sleep(0.05)
    sleep(0.05)
    print(end = '\n')

def escolher_sexo():
    
    print("[1]Masculino\n[2]Feminino")
    escolha = input("R: ")
    while escolha.isnumeric() == False or int(escolha) > 2 or int(escolha) < 1:
        print("Número invalido\nTente novamente")
        escolha = input("R: ")

    if escolha == "1":
        escolha = "M"
    else:
        escolha = "F"

    return escolha

def escolher_turma():
    turmas = [
    "1º Informática A",
    "1º Informática B",
    "1º Química A",
    "1º Química B",
    "1º Edificações A",
    "1º Edificações B",
    "1º Eletrotécnica A",
    "1º Eletrotécnica B",
    "2º Informática Matutino",
    "2º Informática Vespertino",
    "2º Química Matutino",
    "2º Química Vespertino",
    "2º Edificações Matutino",
    "2º Edificações Vespertino",
    "2º Eletrotécnica Matutino",
    "2º Eletrotécnica Vespertino",
    "3º Informática Matutino",
    "3º Informática Vespertino",
    "3º Química Matutino",
    "3º Química Vespertino",
    "3º Edificações Matutino",
    "3º Edificações Vespertino",
    "3º Eletrotécnica Matutino",
    "3º Eletrotécnica Vespertino"
    ]



    print("Escolha tua turma")

    print("""
        [1] 1º Informática A
        [2] 1º Informática B
        [3] 1º Química A
        [4] 1º Química B
        [5] 1º Edificações A
        [6] 1º Edificações B
        [7] 1º Eletrotécnica A
        [8] 1º Eletrotécnica B
        [9] 2º Informática Matutino
        [10] 2º Informática Vespertino
        [11] 2º Química Matutino
        [12] 2º Química Vespertino
        [13] 2º Edificações Matutino
        [14] 2º Edificações Vespertino
        [15] 2º Eletrotécnica Matutino
        [16] 2º Eletrotécnica Vespertino
        [17] 3º Informática Matutino
        [18] 3º Informática Vespertino
        [19] 3º Química Matutino
        [20] 3º Química Vespertino
        [21] 3º Edificações Matutino
        [22] 3º Edificações Vespertino
        [23] 3º Eletrotécnica Matutino
        [24] 3º Eletrotécnica Vespertino
    """)

    escolha_da_turma = input("R: ")

    while escolha_da_turma.isnumeric() == False or int(escolha_da_turma) > 24 or int(escolha_da_turma) < 1:
        print("Número invalido\nTente novamnte")
        escolha_da_turma = input("R: ")
    escolha = int(escolha_da_turma) - 1

    return turmas[escolha]

def escolher_modalidade():
    modalidade = [
    "ARREMESSO DE PESO",
    "LANÇAMENTO DE DARDO",
    "SALTO EM DISTÂNCIA",
    "LANÇAMENTO DE DISCO",
    "SALTO EM ALTURA",
    "SALTO TRIPLO",
    "100 METROS",
    "200 METROS",
    "400 METROS",
    "800 METROS",
    "1500 METROS",
    "3000 METROS (só moças)",
    "5000 METROS (só rapazes)",
    "4 X 100 METROS",
    "4 X 400 METROS",
    ]

    print("Escolha a modalidade ")

    print(""" 
    [1] ARREMESSO DE PESO
    [2] LANÇAMENTO DE DARDO
    [3] SALTO EM DISTÂNCIA
    [4] LANÇAMENTO DE DISCO
    [5] SALTO EM ALTURA
    [6] SALTO TRIPLO
    [7] 100 METROS
    [8] 200 METROS
    [9] 400 METROS
    [10] 800 METROS
    [11] 1500 METROS
    [12] 3000 METROS (femenino)
    [13] 5000 METROS (masculino)
    [14] 4 X 100 METROS 
    [15] 4 X 400 METROS 
    """)

    escolha_da_modalidade = input("R: ")

    while escolha_da_modalidade.isnumeric() == False or int(escolha_da_modalidade) > 15 or int(escolha_da_modalidade) < 1:
        print("Número invalido\nTente novamnte")
        escolha_da_modalidade = input("R: ")
    escolha = int(escolha_da_modalidade) - 1

    return modalidade [escolha]

def toLoad(text, str, times):
    for i in range(3):
        for i in range(times):
            points = str*i
            print(text, points)
            sleep(0.4)
            system('cls')

def initial():
    print("━━━━━━━━━━━━━━━━❪❂❫━━━━━━━━━━━━━━━━")
    print("             BEM VINDO             ")
    print("━━━━━━━━━━━━━━━━❪❂❫━━━━━━━━━━━━━━━━")
    sleep(3)

    toLoad('carregando', '.', 4)

    print("┎━─━─━─━─━─━━─━─━──━─━━─━━─━━─━━─━─━┒")
    text("           System for JIC'S           ")
    print("┖━─━─━─━─━─━─━─━──━─━─━─━─━─━─━─━─━━┚")

def options():
    print("Oque deseja fazer?")
    print("""
    [1] Iniciar
    [2] Sair
    [3] Ver Cadastros feitos
    [4] Editar Cadastros
    [5] Relatório
    """)
    escolha = input("R: ")

    while escolha.isnumeric() == False or int(escolha) > 5:
        print("Digite um número válido\nTente novamente")
        print("""
        [1] Iniciar
        [2] Sair
        [3] Ver cadastros feitos
        [4] Editar cadastro
        [5] Relatório
        """)
        escolha = input("R: ")
    
    if escolha == "1":
        return escolha
    elif escolha == "2":
        toLoad('saindo', '.', 4)
        quit()
    elif escolha == "3":
        return escolha
    elif escolha == "4":
        return escolha
    elif escolha == "5":
        return escolha

def data():
        while True:
            data_str = input("Digite sua data de nascimento (DD/MM/AAAA): ")
            try:
                data = datetime.strptime(data_str, "%d/%m/%Y")
                return data
            except ValueError:
                print("Formato inválido. Digite a data no formato DD/MM/AAAA.")

def relatorio_geral():
        cursor = DataBaserAlunos.conn.execute("""
            SELECT * FROM Alunos
            ORDER BY turma
        """)

        alunos = cursor.fetchall()

        if len(alunos) > 0:
            turma_atual = ""
            print("Alunos Cadastrados")
            for aluno in alunos:
                if aluno[4] != turma_atual:
                    turma_atual = aluno[4]
                    print(f"\nTurma: {turma_atual}")
                print(f"""
                Dados atuais do aluno:
                Matrícula: {aluno[1]}
                Nome: {aluno[2]}
                Data de Nascimento: {aluno[3]}
                Turma: {aluno[4]}
                Modalidade: {aluno[5]}
                Sexo: {aluno[6]}
                """)

        else:
            print("Nenhum aluno cadastrado")
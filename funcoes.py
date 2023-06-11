from sys import stdout
from time import sleep
from os import system

def text(txt):
    for letra in list(txt):
        print(letra, end = '')
        stdout.flush()
        sleep(0.05)
    sleep(0.05)
    print(end = '\n')

    system('cls')


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

    print("""
    [1] Iniciar
    [2] Sair
    [3] Ver Cadastros feitos
    [4] Editar Cadastros
    """)
    escolha = input("R: ")

    while escolha.isnumeric() == False or int(escolha) > 4:
        print("Digite um número válido\nTente novamente")
        print("""
        [1] Iniciar
        [2] Sair
        [3] Ver cadastros feitos
        [4] Editar cadastro
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


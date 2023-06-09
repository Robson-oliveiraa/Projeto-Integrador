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
    """)
    escolha = input("R: ")

    while escolha.isnumeric() == False or int(escolha) > 3:
        print("Digite um número válido\nTente novamente")
        print("""
        [1] Iniciar
        [2] Sair
        [3] Ver Cadastros feitos
        """)
        escolha = input("R: ")
    
    if escolha == "1":
        return escolha
    elif escolha == "2":
        toLoad('saindo', '.', 4)
        quit()
    elif escolha == "3":
        return escolha
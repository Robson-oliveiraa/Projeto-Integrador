from funcoes import *
import time


def initial():
    print("━━━━━━━━━━━━━━━━❪❂❫━━━━━━━━━━━━━━━━")
    print("             BEM VINDO             ")
    print("━━━━━━━━━━━━━━━━❪❂❫━━━━━━━━━━━━━━━━")
    time.sleep(3)

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


    
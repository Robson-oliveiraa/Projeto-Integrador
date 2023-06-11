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
        [12] 3000 METROS (só moças)
        [13] 5000 METROS (só rapazes)
        [14] 4 X 100 METROS 
        [15] 4 X 400 METROS 
        """)

        escolha_da_modalidade = input("R: ")

        while escolha_da_modalidade.isnumeric() == False or int(escolha_da_modalidade) > 15 or int(escolha_da_modalidade) < 1:
            print("Número invalido\nTente novamnte")
            escolha_da_modalidade = input("R: ")
        escolha = int(escolha_da_modalidade) - 1

        return modalidade [escolha]

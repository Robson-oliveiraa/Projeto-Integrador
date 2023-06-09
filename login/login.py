import os
from time import sleep

def login():
    def cad():
        matricula = input("Digite o número de matricula\nR: ")
        senha = input("Digite sua senha\nR: ")
        teste = 0
        if matricula.isdigit() == True:
            with open ("usuarios.txt","r", encoding="utf-8") as arquivo:
                usuarios = arquivo.readlines()
            for linha in usuarios:
                while matricula and senha in linha:
                    print("ERRO DE CADASTRO\nESTE USUARIO JÁ EXISTE\nTENTE OUTRO NOME E SENHA")
                    matricula = input("Digite o número de matricula\nR: ")
                    senha = input("Digite sua senha\nR: ")
                    teste +=1
            while matricula == senha:
                print("ERRO DE CADASTRO\nO nome de usuario não pode ser igual a senha")
                teste +=1
                matricula = input("Digite o número de matricula\nR: ")
                senha = input("Digite sua senha\nR: ")
            if teste == 0:
                print(f"CADASTRO APROVADO!\nBEM VINDO, {matricula}!")
                with open ("usuarios.txt","a", encoding="utf-8") as arquivo:
                    arquivo.write(str(matricula) + (senha)+ ("\n"))
        while matricula.isdigit() == False:
            print("ERRO DE CADASTRO\nMatricula deve conter somente números")
            matricula = input("Digite o número de matricula\nR: ")
            senha = input("Digite sua senha\nR: ")




    def log():
        cancelar = 0
        while cancelar == 0:
            matricula = input("Digite o número de matricula\nR: ")
            senha = input("Digite sua senha\nR: ")
            if matricula.isdigit() == True:
                with open ("usuarios.txt","r", encoding="utf-8") as arquivo:
                    usuarios = arquivo.readlines()
                for linha in usuarios:
                    if matricula and senha in linha:
                        print(f"LOGIN APROVADO!\nBOM TE VER AQUI, {matricula}!")
                        cancelar+=1

                    else:
                        print("LOGIN NEGADO!\nUSUARIO OU SENHA INVALIDO!")
                        matricula = input("Digite o número de matricula\nR: ")
                        senha = input("Digite sua senha\nR: ")

            while matricula.isdigit() == False:
                print("ERRO DE CADASTRO\nMatricula deve conter somente números")
                matricula = input("Digite o número de matricula\nR: ")
                senha = input("Digite sua senha\nR: ")

    print("━━━━━━━━━━━━━━━━❪❂❫━━━━━━━━━━━━━━━━")
    print("             BEM VINDO             ")
    print("━━━━━━━━━━━━━━━━❪❂❫━━━━━━━━━━━━━━━━")
    sleep(1)
    print("Deseja fazer login?\nOu cadastro?")
    escolha = input("[1]Login\n[2]Cadastro\nR:")
    while escolha.isnumeric() == False or int(escolha) > 2:
        print("Digite um número válido\nTente novamente")
        escolha = input("[1]Login\n[2]Cadastro\nR:")
    if escolha == "1":
        log()
    else:
        cad()



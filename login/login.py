import re
from classe import User


def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(padrao, email):
        return True
    else:
        return False

def login():
    print("Deseja fazer login ou cadastro?\n[1]login\n[2]cadastro")
    escolha = input("R: ")

    while escolha.isnumeric() == False or int(escolha) > 2:
        print("Número inválido")
        print("Deseja fazer login ou cadastro?\n[1]login\n[2]cadastro")
        escolha = input("R: ")

    if escolha == "2": 
        matricula = input("Matricula: ")
        while matricula.isdigit() == False:
            print("O número de matricula deve conter somentes números")
            matricula = input("Matricula: ")

        senha = input("Senha: ")
        while len(senha) < 6:
            print("A senha deve conter pelo menos 6 digitos")
            senha = input("Senha: ")

        email = input("Email: ")
        if validar_email(email) == False:
            print("Digite um email válido") 
            email = input("Email: ")

        user = User(matricula, senha, email)
        user.registerToDataBase()
    else:
        matricula = input("Matricula: ")
        senha = input("Senha: ")
        email = None
        user = User(matricula, senha, email)
        user.log()
        
       
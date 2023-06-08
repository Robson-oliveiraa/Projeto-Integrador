from tkinter import *
from tkinter import messagebox
import os
def login():
    master = Tk()
    master.title("Cadastro/Login")
    master.geometry("1000x500")
    master.resizable(width=1, height= 1)

    #funções
    def cad():
        matricula=cad_token.get()
        senha=cad_senha.get()
        teste = 0
        if matricula.isdigit() == True:
            with open ("usuarios.txt","r", encoding="utf-8") as arquivo:
                usuarios = arquivo.readlines()
            for linha in usuarios:
                if matricula and senha in linha:
                    messagebox.showerror("ERRO DE CADASTRO", message="ESTE USUARIO JÁ EXISTE\nTENTE OUTRO NOME E SENHA")
                    teste +=1
            if matricula == senha:
                messagebox.showerror(title="ERRO DE CADASTRO", message="O nome de usuario não pode ser igual a senha")
                teste +=1
            elif teste == 0:
                messagebox.showinfo(title="CADASTRO APROVADO!", message="BEM VINDO, {}!".format(matricula))
                with open ("usuarios.txt","a", encoding="utf-8") as arquivo:
                    arquivo.write(str(matricula) + (senha)+ ("\n"))
        else:
            messagebox.showerror(title="ERRO DE CADASTRO", message="Matricula deve conter somente números")




    def log():
        matricula = en_token.get()
        senha = en_senha.get()
        if matricula.isdigit() == True:
            with open ("usuarios.txt","r", encoding="utf-8") as arquivo:
                usuarios = arquivo.readlines()
            for linha in usuarios:
                if matricula and senha in linha:
                    messagebox.showinfo(title="LOGIN APROVADO!", message="BOM DE VER AQUI, {}!".format(matricula))

                else:
                    messagebox.showerror(title="LOGIN NEGADO!", message="USUARIO OU SENHA INVALIDO!")
        else:
            messagebox.showerror(title="ERRO DE CADASTRO", message="Matricula deve conter somente números")


    #variaveis globais
    pastapp = os.path.dirname(__file__)
    esconda_senha = StringVar

    #import img
    img_fundo = PhotoImage(file=pastapp+"\\tela_final.png")
    botao = PhotoImage(file=pastapp+"\\botão.png")
    sign = PhotoImage(file=pastapp+"\\sign_up.png")


    #Lables
    lab_fundo = Label(master, image=img_fundo)
    lab_fundo.place (x=0, y=0)


    #caixas de entrada
    en_token = Entry(master, bd=2, font=("Calibri", 15), justify=CENTER)
    en_token.place(width=439, height=44, x=32, y=134)

    cad_token = Entry(master, bd=2, font=("Calibri", 15), justify=CENTER)
    cad_token.place(width=437, height=43, x=532, y=135)

    en_senha = Entry(master, textvariable=esconda_senha, show="*", bd=2, font=("Calibri",15), justify=CENTER)
    en_senha.place(width=436, height=41, x=34, y=231)

    cad_senha = Entry(master, textvariable=esconda_senha, show="*", bd=2, font=("Calibri",15), justify=CENTER)
    cad_senha.place(width=436, height=44, x=534, y=230)

    #botões

    bt_entrar = Button(master, bd=0, image=botao, command=log)
    bt_entrar.place(width=140, height=29, x=181, y=397)

    bt_entrar1 = Button(master, bd=0, image=botao, command=cad)
    bt_entrar1.place(width=141, height=32, x=682, y=396)

    #função2


    master.mainloop()




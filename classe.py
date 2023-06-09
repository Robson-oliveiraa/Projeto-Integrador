from funcoes import *
from login import DataBaser


class cadastro():
    def __init__(self, nome, data_N, n_Matricula, turma, sexo):
        self.nome = nome
        self.data_N = data_N
        self.n_Matricula = n_Matricula
        self.turma = turma
        self.sexo = sexo


    def exibir(self):
        text(f'Nome: {self.nome}\nData de Nascimento: {self.data_N}\nNº Matricula: {self.n_Matricula}\nTurma: {self.turma}\nSexo: {self.sexo}')

    def info(self, indice):
        return '\n\n' + indice + '\nNome: ' + self.nome + '\nData de Nascimento: ' + self.data_N + '\nNº Matricula: ' + self.n_Matricula + '\nTurma: '+ self.turma + '\nSexo: ' + self.sexo

    def setNome(self, nome):
        self.nome = nome

    def setData_N(self, data_N):
        self.data_N = data_N

    def setN_Matricula(self, n_Matricula):
        self.n_Matricula = n_Matricula

    def setTurma(self, turma):
        self.turma = turma

    def setSexo(self, sexo):
        self.sexo = sexo

    def exibir2(self):
        print(f'Nome: {self.nome}\nData de Nascimento: {self.data_N}\nNº Matricula: {self.n_Matricula}\nTurma: {self.turma}\nSexo: {self.sexo}\n')
    
class User():
    def __init__(self, matricula, senha, email):
        self.matricula = matricula
        self.senha = senha
        self.email = email

    def registerToDataBase(self):

        DataBaser.cursor.execute("""
        INSERT INTO Users(matricula, password, email) VALUES(?, ?, ?)
        """, (self.matricula, self.senha, self.email))
        DataBaser.conn.commit()
        print("Registrado com sucesso")
    
    def log(self):
        DataBaser.cursor.execute("""
        SELECT * FROM Users
        WHERE (matricula = ? AND password = ?)
        """, (self.matricula, self.senha))
        verify = DataBaser.cursor.fetchone()
        try:
            if (self.matricula in verify and self.senha in verify):
                print("Login realizado, Bem vindo")

        except:
            print("Login negado, matricula ou senha estão errados")

        


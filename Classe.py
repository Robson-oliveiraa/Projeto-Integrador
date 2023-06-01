from Funções import *

class Cadastro():
    def __init__(self, nome, data_N, n_Matricula, turma, sexo):
        self.nome = nome
        self.data_N = data_N
        self.n_Matricula = n_Matricula
        self.turma = turma
        self.sexo = sexo

    def exibir(self):
        Text(f'''
Nome: {self.nome}
Data de Nascimento: {self.data_N}
Nº Matricula: {self.n_Matricula}
Turma: {self.turma}
Sexo: {self.sexo}''')

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
from funcoes import *

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
        return '\n' + indice + '\nNome: ' + self.nome + '\nData de Nascimento: ' + self.data_N + '\nNº Matricula: ' + self.n_Matricula + '\nTurma: '+ self.turma + '\nSexo: ' + self.sexo

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
from funcoes import *
from login import DataBaser
import DataBaserAlunos


class Alunos():
    def __init__(self, nome, data_N, n_Matricula, turma, sexo, modalidade):
        self.nome = nome
        self.data_N = data_N
        self.n_Matricula = n_Matricula
        self.turma = turma
        self.sexo = sexo
        self.modalidade = modalidade

    def cad(self):
        DataBaserAlunos.conn.execute("""
            INSERT INTO Alunos(matricula, nome, data_nascimento, turma, modalidade, sexo) VALUES(?,?,?,?,?,?)
        """,(self.n_Matricula, self.nome, self.data_N, self.turma, self.modalidade, self.sexo))
        DataBaserAlunos.conn.commit()
        print("Cadastrado com sucesso.")
    
    def relatorio(self):
        cursor = DataBaserAlunos.conn.execute("""
        SELECT * FROM Alunos
        WHERE matricula = ?
        """,(self.n_Matricula,))
        alunos = cursor.fetchall()
        if len(alunos) > 0:
            print("Informações do aluno:")
            for aluno in alunos:
                print(f"""
                matricula: {aluno[1]}
                nome: {aluno[2]}
                data_nascimento: {aluno[3]}
                turma: {aluno[4]}
                modalidade: {aluno[5]}
                sexo: {aluno[6]}
                """)
        else:
            print("Nenhum aluno encontrado com a matrícula fornecida.")


    
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
                return True

        except:
            print("Login negado, matricula ou senha estão errados")
            quit()
            
            

        


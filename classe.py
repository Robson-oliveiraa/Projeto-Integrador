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


    def alterar_dado_aluno(self):
        cursor = DataBaserAlunos.conn.execute("""
            SELECT * FROM Alunos
            WHERE matricula = ?
        """, (self.n_Matricula,))
        aluno = cursor.fetchone()

        if aluno is None:
            print("Aluno não encontrado.")
            return

        print("Dados atuais do aluno:")
        print("Matrícula:", aluno[1])
        print("Nome:", aluno[2])
        print("Data de Nascimento:", aluno[3])
        print("Turma:", aluno[4])
        print("Modalidade:", aluno[5])
        print("---------------------")

        print("Qual dado deseja alterar?")
        escolha = input("[1] Matrícula\n[2] Nome\n[3] Data de Nascimento\n[4] Turma\n[5] Modalidade: ")

        novo_valor = input("Novo valor: ")

        if escolha == "1":
            DataBaserAlunos.conn.execute("""
                UPDATE Alunos
                SET matricula = ?
                WHERE matricula = ?
            """, (novo_valor, self.n_Matricula))
        elif escolha == "2":
            DataBaserAlunos.conn.execute("""
                UPDATE Alunos
                SET nome = ?
                WHERE matricula = ?
            """, (novo_valor, self.n_Matricula))
        elif escolha == "3":
            DataBaserAlunos.conn.execute("""
                UPDATE Alunos
                SET data_nascimento = ?
                WHERE matricula = ?
            """, (novo_valor, self.n_Matricula))
        elif escolha == "4":
            DataBaserAlunos.conn.execute("""
                UPDATE Alunos
                SET turma = ?
                WHERE matricula = ?
            """, (novo_valor, self.n_Matricula))
        elif escolha == "5":
            DataBaserAlunos.conn.execute("""
                UPDATE Alunos
                SET modalidade = ?
                WHERE matricula = ?
            """, (novo_valor, self.n_Matricula))
        else:
            print("Opção inválida.")

        DataBaserAlunos.conn.commit()
        print("Dado alterado com sucesso.")
    
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
            
            

        


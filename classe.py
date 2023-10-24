from funcoes import *
from login import DataBaser
import DataBaserAlunos

class usuario():
    def __init__(self, nMatricula,senha):
        self.nMatricula = nMatricula
        self.__senha = senha

    def verificarLogin(self):
        DataBaser.cursor.execute("""
        SELECT * FROM Users
        WHERE (matricula = ? AND password = ?)
        """, (self.nMatricula, self.senha))
        verify = DataBaser.cursor.fetchone()
        try:
            if (self.nMatricula in verify and self.senha in verify):
                print("Login realizado, Bem vindo")
                return True

        except:
            print("Login negado, matricula ou senha estão errados")
            quit()

class aluno(usuario):
    def __init__(self, nome, senha, turma, sexo, dataNascimento, modalidadeInscrita):
        super.__init__(nome, senha)
        self.turma = turma
        self.sexo = sexo
        self.dataNascimento = dataNascimento
        self.modalidade = modalidadeInscrita

    def cadastraInfo(self):
        DataBaserAlunos.conn.execute("""
            INSERT INTO Alunos(matricula, nome, data_nascimento, turma, modalidade, sexo) VALUES(?,?,?,?,?,?)
        """,(self.n_Matricula, self.nome, self.data_N, self.turma, self.modalidade, self.sexo))
        DataBaserAlunos.conn.commit()
        print("Cadastrado com sucesso.")

    def inscreverModalidade():
        escolher_modalidade()

    def __AlteraSenhar(self ):
        matricula = input('Qual é sua madricula:\n')

        DataBaserAlunos.conn.execute("""
            SELECT I* FROM Users
            WHERE ( matricula = ?)
        """, (self.nMatricula))
        verify = DataBaserAlunos.cusor.fetchone()
        try:
            if ( self.nMatricula in verify):
                print('Matricula Correta')

        except:
            print("Matricula Incorreto")
            quit()


        cursor = DataBaserAlunos.conn.execute("""
            SELECT INTO Users(matricula, password) VALUES(?, ?)
            WHERE matricula = ?
        """, (self.n_Matricula, self.__senha))
        aluno = cursor.fetchone()

        if aluno is None:
            print("Não foi possivel encontrar este aluno\nVerifique os dados informados")
            return

        print(f"""
        Dados atuais do aluno:
        Matrícula: {aluno[1]}
        Nome: {aluno[2]}
        Data de Nascimento: {aluno[3]}
        Turma: {aluno[4]}
        Modalidade: {aluno[5]}
        Sexo: {aluno[6]}
        """)

        print("Qual dado deseja alterar?")
        escolha = input("[1] Matrícula\n[2] Nome\n[3] Data de Nascimento\n[4] Turma\n[5] Modalidade\n[6] Sexo\n: ")

        while escolha.isnumeric() == False or int(escolha) > 6 or int(escolha) < 1:
            print("Número inválido\nTente novamente")
            escolha = input("[1] Matrícula\n[2] Nome\n[3] Data de Nascimento\n[4] Turma\n[5] Modalidade\n[6] Sexo\n: ")


'''
class Alunos():
    #Igor
    def __init__(self, nome, data_N, n_Matricula, turma, modalidade, sexo):
        self.nome = nome
        self.data_N = data_N
        self.n_Matricula = n_Matricula
        self.turma = turma
        self.modalidade = modalidade
        self.sexo = sexo

    #Robson
    def cad(self):
        DataBaserAlunos.conn.execute("""
            INSERT INTO Alunos(matricula, nome, data_nascimento, turma, modalidade, sexo) VALUES(?,?,?,?,?,?)
        """,(self.n_Matricula, self.nome, self.data_N, self.turma, self.modalidade, self.sexo))
        DataBaserAlunos.conn.commit()
        print("Cadastrado com sucesso.")
    
    #Robson
    def alterar_dados(self):
        cursor = DataBaserAlunos.conn.execute("""
            SELECT * FROM Alunos
            WHERE matricula = ?
        """, (self.n_Matricula,))
        aluno = cursor.fetchone()

        if aluno is None:
            print("Não foi possivel encontrar este aluno\nVerifique os dados informados")
            return

        print(f"""
        Dados atuais do aluno:
        Matrícula: {aluno[1]}
        Nome: {aluno[2]}
        Data de Nascimento: {aluno[3]}
        Turma: {aluno[4]}
        Modalidade: {aluno[5]}
        Sexo: {aluno[6]}
        """)

        print("Qual dado deseja alterar?")
        escolha = input("[1] Matrícula\n[2] Nome\n[3] Data de Nascimento\n[4] Turma\n[5] Modalidade\n[6] Sexo\n: ")

        while escolha.isnumeric() == False or int(escolha) > 6 or int(escolha) < 1:
            print("Número inválido\nTente novamente")
            escolha = input("[1] Matrícula\n[2] Nome\n[3] Data de Nascimento\n[4] Turma\n[5] Modalidade\n[6] Sexo\n: ")

        

        if escolha == "1":
            matricula = input("Matricula:")
            while matricula.isnumeric() == False:
                    print("Matricula deve conter somente números\nTente Novamente")
                    matricula = input("Matricula: ")

            DataBaserAlunos.conn.execute("""
                UPDATE Alunos
                SET matricula = ?
                WHERE matricula = ?
            """, (matricula, self.n_Matricula))

        elif escolha == "2":
            nome = input("Nome: ")
            DataBaserAlunos.conn.execute("""
                UPDATE Alunos
                SET nome = ?
                WHERE matricula = ?
            """, (nome, self.n_Matricula))

        elif escolha == "3":
            data_nascimento = data()
            DataBaserAlunos.conn.execute("""
                UPDATE Alunos
                SET data_nascimento = ?
                WHERE matricula = ?
            """, (data_nascimento, self.n_Matricula))

        elif escolha == "4":
            turma = escolher_turma()
            DataBaserAlunos.conn.execute("""
                UPDATE Alunos
                SET turma = ?
                WHERE matricula = ?
            """, (turma, self.n_Matricula))

        elif escolha == "5":
            modalidade = escolher_modalidade()
            DataBaserAlunos.conn.execute("""
                UPDATE Alunos
                SET modalidade = ?
                WHERE matricula = ?
            """, (modalidade, self.n_Matricula))

        elif escolha == "6":
            sexo = escolher_sexo()
            DataBaserAlunos.conn.execute("""
                UPDATE Alunos
                SET sexo = ?
                WHERE matricula = ?
            """, (sexo, self.n_Matricula))

        DataBaserAlunos.conn.commit()
        print("Dado alterado com sucesso")
    
    #VVande11
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
            print("Não foi possivel encontrar algum aluno com a matrícula fornecida.\nVerifique os dados")

#Douglas
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
'''
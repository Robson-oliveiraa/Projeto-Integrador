#Douglas

import sqlite3

conn = sqlite3.connect("cadastros.db")

cusor = conn.cursor()

cusor.execute("""
CREATE TABLE IF NOT EXISTS Alunos(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    matricula TEXT NOT NULL,
    nome TEXT NOT NULL,
    data_nascimento DATE NOT NULL,
    turma TEXT NOT NULL,
    modalidade TEXT NOT NULL,
    sexo TEXT NOT NULL

);
""")

print("connect")
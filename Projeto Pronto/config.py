import sqlite3
#VARIAVEIS GLOBAIS

# Lista global de cadastros
lista_cadastros = []

# Lista global de matérias
lista_materias = []

# Lista global de resumos
lista_resumos = []

global usuario_logado

# Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Criar tabela de usuários, se ainda não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha_hash TEXT NOT NULL,
    data_criacao TEXT NOT NULL
)
''')
conn.commit()

# Criar tabela de matérias, se ainda não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS materias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    corpo TEXT NOT NULL,
    data_criacao TEXT NOT NULL,
    usuario_id INTEGER,
    FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
)
''')
conn.commit()

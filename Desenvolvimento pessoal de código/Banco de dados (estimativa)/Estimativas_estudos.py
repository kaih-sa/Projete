import sqlite3

#Códigos para poder usar o banco de dados e funções pra alterá-lo

#x = 1
# tem que incrementar + 1 no x, a cada criação de perfil
# e não pode ser criado aqui tbm né, pq ai ficaria resetando sempre que rodasse esse arquivo inteiro

def Banco_db(id_usuario):

    # Conectando ao banco de dados
    conexao = sqlite3.connect('comparativo.db')
    cursor = conexao.cursor()

    tabela_nome = f'horas_estudo{id_usuario}'

    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {tabela_nome} (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            data TEXT, 
            tempo_geral INTEGER,
            id_user INTEGER NOT NULL
    );
    """)
    # Fechando a conexão

    return conexao,cursor,tabela_nome

def Codigos_ler_db(x):
    # Conectando ao banco de dados
    conexao = sqlite3.connect('comparativo.db')
    cursor = conexao.cursor()
    tabela_nome = f'horas_estudo{x}'#referente ao id do usuario

    # Consulta para ler todos os dados do usuario x
    '''cursor.execute(f"SELECT data, tempo_geral FROM {tabela_nome} WHERE id_user = ? ", (x,))
    for linha in  cursor.fetchall():
        print(linha)
    '''
    # Ler de um id especifico
    '''cursor.execute(f"SELECT data, tempo_geral FROM {tabela_nome} WHERE id = ?", (variavel_do_id,))'''

    #Ler de uma data especifica
    '''cursor.execute(f"SELECT data, tempo_geral FROM {tabela_nome} WHERE data = ? ", (variavel_da_data,))'''

    '''tabela_nome = f'horas_estudo{x}'
    tabela_data = f'2024-09-{data_escolhida}'
    
    # Ler de uma data especifica
    cursor.execute(f"SELECT data, tempo_geral FROM {tabela_nome} WHERE data = ? ", (tabela_data,))
    '''
# Fiz duas pq cada temporizador tem sua maneira de lidar com um count, então são jeitos diferentes de lidar
#Salva o tempo no db, esse tempo é refrente a data
def Salvar_tempo_no_db(tempo,id_usuario):

    conexao, cursor, tabela_nome = Banco_db(id_usuario)

 # Verifica se já tem a linha da data
    cursor.execute(f"SELECT tempo_geral FROM {tabela_nome} WHERE data = DATE('now')")
    resultado = cursor.fetchone()

    if resultado is not None:
        # Soma se ja tiver
        tempo_atual = resultado[0]
        novo_tempo = (tempo - 1) + tempo_atual #tempo corrigido pro delay
        print(f"Tempo Atual: {tempo_atual}, Novo Tempo: {novo_tempo}")  # Exibe o tempo atualizado
        cursor.execute(f"UPDATE {tabela_nome} SET tempo_geral = ? WHERE data = DATE('now')", (novo_tempo,))
    else:
        # Se não, ele adiciona
        print(f"Inserindo novo tempo: {tempo}")  # Exibe o tempo sendo inserido
        cursor.execute(f"INSERT INTO {tabela_nome} (tempo_geral,id_user,data) VALUES (?,?,DATE('now'))", (tempo,id_usuario))

    conexao.commit()
    conexao.close()

def Ler_db(id_usuario):

    conexao, cursor, tabela_nome = Banco_db(id_usuario)
    cursor.execute(f"SELECT * FROM {tabela_nome}")
    todos_registros = cursor.fetchall()

    for dt in reversed(todos_registros[-7:]):  # X ultimos registros
        print(dt)

    conexao.close()


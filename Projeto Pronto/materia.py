import tkinter as tk
from tkinter import messagebox, filedialog, Canvas, Scrollbar
import datetime as dt
import sqlite3

from materiaEditar import criar_janela_editar_materia
import inicio
import config

# Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

def deletar_materia(materia_id):
    if messagebox.askyesno("Confirmar", "Você tem certeza de que deseja deletar esta matéria?"):
        cursor.execute('DELETE FROM materias WHERE id = ?', (materia_id,))
        conn.commit()
        messagebox.showinfo("Sucesso", "Matéria deletada com sucesso!")
        janela_acessar_materia.destroy()  # Fecha a janela atual de matérias
        acessar_materia()  # Reabre a janela atualizada

def acessar_materia():
    global janela_acessar_materia
    janela_acessar_materia = tk.Toplevel()
    janela_acessar_materia.title('Acessar Matéria')
    janela_acessar_materia.geometry('400x600')
    janela_acessar_materia.configure(bg='#a2d8f1')

    cursor.execute('''SELECT id, titulo FROM materias WHERE usuario_id = ?''', (config.usuario_logado[0],))
    materias = cursor.fetchall()

    # Canvas para a rolagem
    canvas = tk.Canvas(janela_acessar_materia, bg='#a2d8f1')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Barra de rolagem vertical
    scrollbar = tk.Scrollbar(janela_acessar_materia, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame que irá conter todos os widgets
    frame_conteudo = tk.Frame(canvas, bg='#a2d8f1')
    canvas.create_window((0, 0), window=frame_conteudo, anchor="nw")

    # Ajustar a rolagem conforme o conteúdo
    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_conteudo.bind("<Configure>", ajustar_scroll)

    # Adicionando suporte ao scroll do mouse
    def _on_mouse_wheel(event):
        canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

    # Vincula a rolagem do mouse no Windows e MacOS
    janela_acessar_materia.bind_all("<MouseWheel>", _on_mouse_wheel)

    # Em sistemas baseados em Unix/Linux, o evento da roda do mouse é diferente
    janela_acessar_materia.bind_all("<Button-4>", lambda event: canvas.yview_scroll(-1, "units"))
    janela_acessar_materia.bind_all("<Button-5>", lambda event: canvas.yview_scroll(1, "units"))

    # Título centralizado
    titulo_centralizado = tk.Label(frame_conteudo, text="MATÉRIAS", font=("Helvetica", 16, "bold"), bg='#a2d8f1', fg='#f9e653')
    titulo_centralizado.grid(row=0, column=0, columnspan=2, pady=(20, 0), sticky="n")

    # Linha abaixo do título
    canvas_line = tk.Canvas(frame_conteudo, width=400, height=2, bg='#a2d8f1', highlightthickness=0)
    canvas_line.grid(row=1, column=0, columnspan=2, pady=(0, 10), sticky="n")
    canvas_line.create_line(0, 1, 400, 1, fill="#539aff", width=2)

    if not materias:
        messagebox.showinfo("Informação", "Nenhuma matéria disponível")
    else:
        for i, materia in enumerate(materias, start=1):
            coluna = (i - 1) % 2  # Alterna entre 0 e 1 para criar duas colunas
            linha = (i - 1) // 2 * 2 + 2  # Incrementa a linha a cada 2 matérias, começando na linha 2

            # Exibir o título da matéria em duas colunas
            tk.Label(frame_conteudo, text=f"{materia[1]}", font=("Helvetica", 14, "bold"), bg='#a2d8f1',
                     fg="white").grid(row=linha, column=coluna, padx=10, pady=5, sticky="w")

            # Criar um frame para os botões
            frame_botoes = tk.Frame(frame_conteudo, bg='#a2d8f1')
            frame_botoes.grid(row=linha + 1, column=coluna, padx=10, pady=5, sticky="w")

            botao_editar = tk.Label(frame_botoes, text="editar", font=("Helvetica", 10, "bold"), fg="#0099fa",
                                    bg="#a2d8f1", cursor="hand2")
            botao_editar.bind("<Button-1>", lambda e, id=materia[0]: [janela_acessar_materia.withdraw(),
                                                                      criar_janela_editar_materia(id)])
            botao_editar.grid(row=0, column=0, padx=5)

            botao_deletar = tk.Label(frame_botoes, text="deletar", font=("Helvetica", 10, "bold"), fg="#0099fa",
                                     bg="#a2d8f1", cursor="hand2")
            botao_deletar.bind("<Button-1>", lambda e, id=materia[0]: deletar_materia(id))
            botao_deletar.grid(row=0, column=1, padx=5)


def criar_materia():
    titulo = entry_materia.get()
    corpo = text_corpo.get("1.0", tk.END).strip()

    if not titulo or not corpo:
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    # Salvar matéria na tabela de matérias no banco de dados
    data_criacao = dt.datetime.now().strftime("%d/%m/%y %H:%M")

    try:
        cursor.execute('''
            INSERT INTO materias (titulo, corpo, data_criacao, usuario_id)
            VALUES (?, ?, ?, ?)
            ''', (titulo, corpo, data_criacao, config.usuario_logado[0]))
        conn.commit()

        messagebox.showinfo("Sucesso", "Matéria criada com sucesso!")
        janela_materia.destroy()

    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def criar_janela_materia():
    global entry_materia, text_corpo, janela_materia

    janela_materia = tk.Toplevel()
    janela_materia.title('Criar Matéria')
    janela_materia.geometry('400x600')
    janela_materia.configure(bg='#a2d8f1')

    # Configurando o grid para centralizar
    janela_materia.grid_columnconfigure(0, weight=1)
    janela_materia.grid_rowconfigure(0, weight=1)
    janela_materia.grid_rowconfigure(6, weight=1)

    label_materia = tk.Label(janela_materia, text="Título",  font=("Helvetica", 20, "bold"), bg='#a2d8f1', fg='#f9e653')
    label_materia.grid(row=1, column=0, padx=10, pady=10, sticky='n')

    frame_entry = tk.Frame(janela_materia, bd=0.001, relief=tk.SUNKEN, background='#90c7e8')
    frame_entry.grid(row=2, column=0, padx=10, pady=10, sticky='n')

    entry_materia = tk.Entry(frame_entry, width=30, bg='white')
    entry_materia.pack(padx=10, pady=10)

    label_texto = tk.Label(janela_materia, text="Conteúdo", font=("Helvetica", 14, "bold"), bg='#a2d8f1', fg='#f9e653')
    label_texto.grid(row=3, column=0, padx=10, pady=10, sticky='n')

    frame_texto = tk.Frame(janela_materia, bd=0.001, relief=tk.SUNKEN, background='#90c7e8')
    frame_texto.grid(row=4, column=0, padx=10, pady=10, sticky='n')

    text_corpo = tk.Text(frame_texto, height=15, width=40, wrap=tk.WORD, bg='white')
    text_corpo.pack(padx=10, pady=10)

    frame_botoes = tk.Frame(janela_materia, bg='#a2d8f1')
    frame_botoes.grid(row=5, column=0, padx=10, pady=10, sticky='n')

    botao_materia = tk.Button(frame_botoes, text="criar", font=("Helvetica", 12, "bold"), bg="#5fa3f1", fg="#f9f58a", width=10, height=1, command=criar_materia)
    botao_materia.grid(row=0, column=0, padx=5)

    # Espaço ao redor para centralizar tudo
    janela_materia.grid_rowconfigure(0, weight=1)
    janela_materia.grid_rowconfigure(6, weight=1)

    janela_materia.transient(inicio.janela_inicial)
    janela_materia.grab_set()
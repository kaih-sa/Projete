import tkinter as tk #Importa o módulo tkinter, que é a biblioteca padrão para criar interfaces gráficas em Python
from tkinter import messagebox, filedialog
import inicio
import shutil  # Para copiar o arquivo
import os  # Para criar diretórios e lidar com caminhos
import sqlite3

import materia
import config

# Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

def criar_janela_editar_materia(materia_id):
    global entry_editar_materia, entry_editar_texto, janela_editar_materia

    janela_editar_materia = tk.Toplevel()
    janela_editar_materia.title('Editar Matéria')
    janela_editar_materia.geometry('400x600')  # tamanho da janela
    janela_editar_materia.configure(bg='#a2d8f1')

    # Buscar a matéria pelo ID
    cursor.execute('''
    SELECT titulo, corpo FROM materias WHERE id = ?
    ''', (materia_id,))
    materia = cursor.fetchone()

    if materia:
        titulo, corpo = materia
        # Configurando o grid para centralizar
        janela_editar_materia.grid_columnconfigure(0, weight=1)  # Coluna central
        janela_editar_materia.grid_rowconfigure(0, weight=1)  # Espaço antes dos elementos
        janela_editar_materia.grid_rowconfigure(6, weight=1)  # Espaço após os elementos

        label_editar_materia = tk.Label(janela_editar_materia, text="Título", font = ("Helvetica", 14, "bold"), bg = '#a2d8f1', fg = '#f9e653')
        label_editar_materia.grid(row=1, column=0, padx=10, pady=10, sticky='n')

        frame_entry = tk.Frame(janela_editar_materia, bd=0.001, relief=tk.SUNKEN, background='#90c7e8')
        frame_entry.grid(row=2, column=0, padx=10, pady=10, sticky='n')

        entry_editar_materia = tk.Entry(frame_entry,width=30)
        entry_editar_materia.insert(0, titulo)
        entry_editar_materia.grid(row=2, column=0, padx=10, pady=10, sticky='n')

        label_editar_texto = tk.Label(janela_editar_materia, text="Conteúdo", font = ("Helvetica", 14, "bold"), bg = '#a2d8f1', fg = '#f9e653')
        label_editar_texto.grid(row=3, column=0, padx=10, pady=10, sticky='n')

        # Crie um frame com uma borda
        frame_texto_editar = tk.Frame( janela_editar_materia, bd=0.001, relief=tk.SUNKEN, background='#90c7e8')  # 'bd' é a largura da borda
        frame_texto_editar.grid(row=4, column=0, padx=10, pady=10, sticky='n')

        entry_editar_texto = tk.Text(frame_texto_editar, height=15, width=40,wrap=tk.WORD)  # 'wrap=tk.WORD' quebra o texto automaticamente
        entry_editar_texto.insert("1.0", corpo)
        entry_editar_texto.grid(row=4, column=0, padx=10, pady=10, sticky='n')

        frame_botons = tk.Frame(janela_editar_materia, bg='#a2d8f1')
        frame_botons.grid(row=5, column=0, padx=10, pady=10, sticky='n')  # grid utilizado ao invés de pack

        botao_editar = tk.Button(frame_botons, text="salvar", font=("Helvetica", 12,"bold"), bg="#5fa3f1", fg="#f9f58a", width=10, height=1, command=lambda: editar_materia(materia_id ))
        #botao_editar.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
        botao_editar.grid(row=0, column=0, padx=5)

        # Espaço ao redor para centralizar tudo
        janela_editar_materia.grid_rowconfigure(0, weight=1)
        janela_editar_materia.grid_rowconfigure(6, weight=1)

    janela_editar_materia.transient(inicio.janela_inicial)
    janela_editar_materia.grab_set()
    inicio.janela_inicial.wait_window(janela_editar_materia)

def editar_materia(materia_id):
    novo_titulo = entry_editar_materia.get()
    novo_corpo = entry_editar_texto.get("1.0", tk.END).strip()

    if not novo_titulo or not novo_corpo:
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    cursor.execute('''
    UPDATE materias SET titulo = ?, corpo = ? WHERE id = ?
    ''', (novo_titulo, novo_corpo, materia_id))
    conn.commit()

    messagebox.showinfo("Sucesso", "Matéria editada com sucesso!")
    janela_editar_materia.destroy()
    materia.acessar_materia()
import tkinter as tk
from tkinter import ttk
import datetime as dt
import tkinter.messagebox as tkmb
import hashlib

lista_cadastros = []

def criar_cadastro(): 
    def cadastrar():
        nome = entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()
        confirmar_senha = entry_confirmar_senha.get()

        # Checa se todos os campos têm algo escrito
        if not nome or not email or not senha or not confirmar_senha:
            tkmb.showerror("ERRO", "Preencha todos os campos")
            return

        # Checa se as senhas são iguais
        if senha != confirmar_senha:
            tkmb.showerror("ERRO", "As senhas são diferentes")
            return

        # Colocando data e hora no cadastro
        data_criacao = dt.datetime.now().strftime("%d/%m/%y %H:%M")

        # Mostrando a lista de cadastros
        cadastros = len(lista_cadastros) + 1
        cadastros_str = f"cadastro-{cadastros}"
        lista_cadastros.append((cadastros_str, nome, email, senha, confirmar_senha, data_criacao))
        print(lista_cadastros)
        tkmb.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        janela_cadastro.destroy()

    # Definir o tamanho da janela aqui tem o tamanho da tela do celular lá do Figma (n tem mais, mudei)
    janela_cadastro = tk.Tk()
    janela_cadastro.geometry("250x450")
    janela_cadastro.title('Cadastro')

    # Nome de usuário
    tk.Label(janela_cadastro, text="Nome de usuário").grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_nome = tk.Entry(janela_cadastro)
    entry_nome.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    # Email
    tk.Label(janela_cadastro, text="Email").grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_email = tk.Entry(janela_cadastro)
    entry_email.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    # Senha
    tk.Label(janela_cadastro, text="Senha").grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_senha = tk.Entry(janela_cadastro, show='*')
    entry_senha.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    # Confirmar senha
    tk.Label(janela_cadastro, text="Confirmar senha").grid(row=7, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_confirmar_senha = tk.Entry(janela_cadastro, show='*')
    entry_confirmar_senha.grid(row=8, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    # Botão para cadastrar
    tk.Button(janela_cadastro, text="Cadastrar", command=cadastrar).grid(row=9, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

    janela_cadastro.mainloop()

def login():
    def Checar_login():
         nome = entry_nome
         senha = entry_senha
         if nome == entry_nome:
              tkmb.showinfo("Sucesso", "Login realizado com sucesso!")
              janela_login.destroy()
            
                
    # Definir o tamanho da janela aqui tem o tamanho da tela do celular lá do Figma
    janela_login = tk.Tk()
    janela_login.geometry("250x450")
    janela_login.title('Login')

    # Nome de usuário
    tk.Label(janela_login, text="Nome de usuário").grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_nome = tk.Entry(janela_login)
    entry_nome.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    # Senha
    tk.Label(janela_login, text="Senha").grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_senha = tk.Entry(janela_login, show='*')
    entry_senha.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    # Botão para logar
    tk.Button(janela_login, text="Login").grid(row=9, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

    janela_login.mainloop()

criar_cadastro()
login()

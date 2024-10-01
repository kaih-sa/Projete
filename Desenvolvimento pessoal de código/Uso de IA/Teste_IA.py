import tkinter as Tkinter

def Gemini():
    #Import the Python SDK
    import google.generativeai as genai
    # Used to securely store your API key

    GOOGLE_API_KEY = 'AIzaSyC5ubXAp6pbZkOfeSwT2Qx7N4lSyi_Dw6Y'

    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-pro')


    # tentar usar verdadeiro ou falso
    entra = entrada.get()
    response = model.generate_content("Me de uma questão de verdadeiro ou falso sobre "+entra+" e me de a reposta em baixo")
    #return response.text
    print(response.text)#[:-25]


global root
# a tal raiz para surgir a janela
root = Tkinter.Tk()
root.title("Escolher")
root.geometry("400x300")#faz a janela
root.configure(bg="lightblue")


#escrever na tela
label = Tkinter.Label(root, text="Manda, chefe!", fg="green",bg="lightblue", font="Verdana 30 bold")
label.place(relx=0.5, rely=0.5, anchor='center')#centralizei
label.pack()

entrada = Tkinter.Entry(root, width=10)
entrada.pack()


#botoes e suas configs
f = Tkinter.Frame(root)
enviar = Tkinter.Button(f, text='Enviar', width=9,bg="lightgreen", command= Gemini)
#enviar = Tkinter.Button(f, text='Enviar', width=9,bg="lightgreen")
f.pack(padx=5, pady=5,anchor="center",)
enviar.pack()

root.mainloop()


#print(resposta[:-25])

'''
escolha = "Gepmetria plana"
r = Gemini("Me de uma questão de verdadeiro ou falso sobre "+escolha+" e me de a reposta em baixo")
resposta = r[-10:]  # últimos caracteres
pra_pessoa = r[:-25] # exclui os últimos
print("IA diz: "+r)
print("resposta certa: "+resposta)
print("pra pessoa: " + pra_pessoa )
'''


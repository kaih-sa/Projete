#bibliotecas
import tkinter as Tkinter
from datetime import datetime, timezone
import teste_uso_txt_ as txt

import datetime as dt

from google.api_core.operations_v1.operations_client_config import config

# Colocando data e hora no cadastro
mes = dt.datetime.now().strftime("%m")
dia = dt.datetime.now().strftime("%d")


def Cronometro():
    root.destroy()
    global counter,running
    counter = 0
    running = False

    def counter_label(labelcr):
        def count():
            if running:
                global counter

                # delay pra começar
                if counter == 0:
                    display = "Starting..."

                else:
                    ttcr = datetime.fromtimestamp(counter, timezone.utc)  # conversão do UTC, coisa de horarios
                    string = ttcr.strftime("%H:%M:%S")
                    display = string

                labelcr['text'] = display

                '''
                 função label.after(faz o delay, chama a função que tá aqui)
                 delay em milissegundos e dps chama a função no segundo parametro
                 pra valer tipo um contar, chamaria de segundno de segundo
                 '''
                labelcr.after(1000, count)
                counter += 1

        # chama
        count()

    # começar
    def Start(labelcr):
        global running
        running = True
        counter_label(labelcr)
        startcr['state'] = 'disabled'
        stopcr['state'] = 'normal'
        resetcr['state'] = 'normal'
        backcr['state'] = 'normal'

    # parar
    def Stop():
        global running
        txt.Adicionar_horas(counter)
        startcr['state'] = 'normal'
        stopcr['state'] = 'disabled'
        resetcr['state'] = 'normal'
        backcr['state'] = 'normal'
        running = False
        tempo= txt.Adicionar_horas(counter)
        txt.Add_calendario(mes,dia,tempo)




    # reset normal
    def Reset(labelcr):
        global counter
        counter = 0

        # reset se n tiver contando
        if not running:
            resetcr['state'] = 'disabled'
            backcr['state'] = 'normal'
            labelcr['text'] = 'Welcome!'

        # reset se o cronometro parado
        else:
            labelcr['text'] = 'Starting...'


    rootcr = Tkinter.Tk()
    rootcr.title("Escolher")
    rootcr.geometry("400x300")  # faz a janela
    rootcr.configure(bg="lightblue")


    labelcr = Tkinter.Label(rootcr, text="Contar!", bg="lightblue",fg="green", font="Verdana 30 bold")
    labelcr.pack()
    fcr = Tkinter.Frame(rootcr)
    startcr = Tkinter.Button(fcr, text='Start', width=6,bg="lightgreen", command=lambda: Start(labelcr))
    stopcr = Tkinter.Button(fcr, text='Stop', width=6,bg="lightgreen", state='disabled', command=Stop)
    resetcr = Tkinter.Button(fcr, text='Reset', width=6,bg="lightgreen", state='disabled', command=lambda: Reset(labelcr))
    backcr = Tkinter.Button(fcr, text='Back', width=6, state='disabled', )


    fcr.pack(anchor='center', pady=5)
    startcr.pack(side="left")
    stopcr.pack(side="left")
    resetcr.pack(side="left")
    backcr.pack(side='left')

    rootcr.mainloop()


def Timer():
    root.destroy()
    global running,counter
    counter = 0
    running = False

    def counter_label(labelmr):
        def count():
            if running:
                global counter

                if counter <= 0:
                    display = "Fim..."


                else:
                    ttmr = datetime.fromtimestamp(counter, timezone.utc)# conversão do UTC
                    string = ttmr.strftime("%H:%M:%S")
                    display = string

                #labelmr = Tkinter.Label(rootmr,bg= "lightgreen", text=display, fg="black", font="Verdana 30 bold")
                labelmr['text'] = display
                labelmr['bg'] = 'lightblue'
                labelmr['fg'] = 'green'
                labelmr.after(1000, count)
                counter -= 1

        count()
        return

    def Start(labelmr):
        startmr.config(text = 'Start')
        global running, counter
        running = True

        time_str = entrymr.get()
        if time_str.isdigit():
            counter = int(time_str)
        else:
            labelmr['text'] = "Digite um número válido!"
            return

        counter_label(labelmr)
        startmr['state'] = 'disabled'
        stopmr['state'] = 'normal'
        resetmr['state'] = 'normal'
        backmr['state'] = 'normal'

    def Stop():
        global running
        startmr.config(text="Run", command = lambda : Run(labelmr))
        startmr['state'] = 'normal'
        stopmr['state'] = 'disable'
        resetmr['state'] = 'normal'
        backmr['state'] = 'normal'
        running = False
        txt.Adicionar_horas(counter)

    # Recomeçar
    def Run(labelmr):
        global running
        running = True
        counter_label(labelmr)
        startmr['state'] = 'normal'
        stopmr['state'] = 'normal'
        resetmr['state'] = 'normal'
        backmr['state'] = 'normal'
        startmr.config(text="Start", command = lambda : Start(labelmr))

    def Reset(labelmr):
        global counter

        # Pega o tempo em segundos da entrada do usuário
        time_str = entrymr.get()

        if time_str.isdigit():
            counter = int(time_str)
        else:
            labelmr['text'] = "Digite um número válido!"

        if not running:
            resetmr['state'] = 'disable'
            labelmr['text'] = 'Welcome!'
        else:
            labelmr['text'] = 'Starting...'


    rootmr = Tkinter.Tk()
    rootmr.title("Timer")
    rootmr.geometry("400x300")
    rootmr.configure(bg="lightblue")

    labelmr = Tkinter.Label(rootmr, text="Welcome!",bg = 'lightblue', fg="green", font="Verdana 30 bold")
    labelmr.pack()

    entrymr = Tkinter.Entry(rootmr, width=10)
    entrymr.pack()


    fmr = Tkinter.Frame(rootmr)
    startmr = Tkinter.Button(fmr, text='Start', width=6, command=lambda: Start(labelmr))
    stopmr = Tkinter.Button(fmr, text='Stop', width=6, state='disabled', command=Stop)
    resetmr = Tkinter.Button(fmr, text='Reset', width=6, state='disabled', command=lambda: Reset(labelmr))
    backmr = Tkinter.Button(fmr, text='Back', width=6, state='disabled')


    fmr.pack(anchor='center', pady=5)
    startmr.pack(side="left")
    stopmr.pack(side="left")
    resetmr.pack(side="left")
    backmr.pack(side="left")


    rootmr.mainloop()

# O LOOP FUNCIONA MAS A JANELA NUNCA FECHA DE VDD
global root
# a tal raiz para surgir a janela
root = Tkinter.Tk()
root.title("Escolher")
root.geometry("400x300")#faz a janela
root.configure(bg="lightblue")

#escrever na tela
label = Tkinter.Label(root, text="Faça sua escolha!", fg="green",bg="lightblue", font="Verdana 30 bold")
label.place(relx=0.5, rely=0.5, anchor='center')#centralizei
label.pack()

#botoes e suas configs
f = Tkinter.Frame(root)
cronometro = Tkinter.Button(f, text='Cronômetro', width=9,bg="lightgreen", command=lambda: Cronometro())
timer = Tkinter.Button(f, text='Timer', width=9,bg="lightgreen", command=lambda: Timer())
f.pack(padx=5, pady=5,anchor="center",)
cronometro.pack(side="left")
timer.pack()

#loop da janela da tela
root.mainloop()


'''
LOOPING OU IR DE VOLTA A 1 PAGINA

FAZER O BOTÃO DE SETAR TEMPO?

ARRUMAR A CAIXA DE TXTO DO TIMER PRA HOR/MIN/SEG

FAZER COMPARATIVO DE HORAS
    GUARDAR O TEMPO PASSADO, PASSAR PRA TXT (ta acontecendo)
    E DEPOIS FAZER UMA ESTIMATIVA (o gráfico vai ser: escolhe o dia e setar no gráfico{front} )     
'''
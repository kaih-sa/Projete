#bibliotecas
import tkinter as Tkinter
from datetime import datetime, timezone
from Estimativas_estudos import Salvar_tempo_no_db

id_usuario = 1

def Cronometro():
    root.destroy()
    global counter,running,contador_pro_db
    counter = 0
    contador_pro_db = 0
    running = False

    def counter_label(labelcr):
        def count():
            if running:
                global counter,contador_pro_db

                # delay pra começar
                if counter == 0:
                    display = "Starting..."

                else:
                    string = "{:02d}:{:02d}:{:02d}".format(counter // 3600, (counter % 3600) // 60, counter % 60)
                    display = string

                labelcr['text'] = display

                '''
                 função label.after(faz o delay, chama a função que tá aqui)
                 delay em milissegundos e dps chama a função no segundo parametro
                 pra valer tipo um contar, chamaria de segundno de segundo
                 '''
                labelcr.after(1000, count)
                counter += 1
                contador_pro_db += 1

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
        global running, contador_pro_db
        print("Tempo antes do stop:", contador_pro_db)
        Salvar_tempo_no_db(contador_pro_db,id_usuario)
        startcr['state'] = 'normal'
        stopcr['state'] = 'disabled'
        resetcr['state'] = 'normal'
        backcr['state'] = 'normal'
        running = False
        contador_pro_db = 0

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
    global running,counter,contador_pro_db
    contador_pro_db = 0
    counter = 0
    running = False

    def counter_label(labelmr):
        def count():
            if running:
                global counter,contador_pro_db

                if counter <= 0:
                    display = "Fim..."

                else:
                    ttmr = datetime.fromtimestamp(counter, timezone.utc)# conversão do UTC
                    string = ttmr.strftime("%H:%M:%S")
                    display = string

                labelmr['text'] = display
                labelmr['bg'] = 'lightblue'
                labelmr['fg'] = 'green'
                labelmr.after(1000, count)
                counter -= 1
                contador_pro_db += 1

        count()
        return

    def Start(labelmr):
        startmr.config(text = 'Start')
        global running, counter
        running = True
        '''
        Código para 3 entradas de valor para o front:
        
        horas_entrada = entry_horas.get()
        minutos_entrada = entry_min.get()
        segundos_entrada = entry_segundos.get()

        if horas_entrada.isdigit() and minutos_entrada.isdigit() and segundos_entrada.isdigit():
            hours = int(horas_entrada)
            minutes = int(minutos_entrada)
            seconds = int(segundos_entrada)

            counter = (hours * 3600) + (minutes * 60) + seconds #convertendo tudo pra segundos

        else:
            labelmr['text'] = "Digite um número válido!"
            return
        '''
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
        global running,contador_pro_db
        startmr.config(text="Run", command = lambda : Run(labelmr))
        startmr['state'] = 'normal'
        stopmr['state'] = 'disabled'
        resetmr['state'] = 'normal'
        backmr['state'] = 'normal'
        running = False
        print("Tempo antes do stopmr:", contador_pro_db)
        Salvar_tempo_no_db(contador_pro_db,id_usuario)
        contador_pro_db = 0

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
        '''
        Código para 3 entradas de valor para o front:
        horas_entrada = entry_horas.get()
        minutos_entrada = entry_min.get()
        segundos_entrada = entry_segundos.get()
        
        if horas_entrada.isdigit() and minutos_entrada.isdigit() and segundos_entrada.isdigit():
            hours = int(horas_entrada)
            minutes = int(minutos_entrada)
            seconds = int(segundos_entrada)

            counter = (hours * 3600) + (minutes * 60) + seconds #convertendo tudo pra segundos
        else:
            labelmr['text'] = "Digite um número válido!"

        if not running:
            resetmr['state'] = 'disable'
            labelmr['text'] = 'Welcome!'
        else:
            labelmr['text'] = 'Starting...'
        '''
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

    labelmr = Tkinter.Label(rootmr, text="Welcome!", bg='lightblue', fg="green", font="Verdana 30 bold")
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

global root
# a raiz para surgir a janela
root = Tkinter.Tk()
root.title("Escolher")
root.geometry("400x300")#faz a hforma da janela
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


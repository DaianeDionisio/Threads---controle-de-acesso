from tkinter import *
from Porta import porta

porta = porta()

class janela():
    def __init__(self):
        self.janelaInterfone = Tk()
        self.janelaInterfone.title("Porta 01 de acesso do Edificio")
        self.button1 = Button(self.janelaInterfone, text = "Falar com o apto 101",command= lambda: self.abrirChat("101"))
        self.button1.grid(column=0, row=0, padx=10, pady=10)
        self.button2 = Button(self.janelaInterfone, text="Falar com o apto 102",command= lambda: self.abrirChat("102"))
        self.button2.grid(column=1, row=0, padx=10, pady=10)
        self.button3 = Button(self.janelaInterfone, text="Falar com o apto 103",command= lambda: self.abrirChat("103"))
        self.button3.grid(column=2, row=0, padx=10, pady=10)
        self.button4 = Button(self.janelaInterfone, text="Falar com o apto 104",command= lambda: self.abrirChat("104"))
        self.button4.grid(column=0, row=1, padx=10, pady=10)
        self.button5 = Button(self.janelaInterfone, text="Falar com o apto 105",command= lambda: self.abrirChat("105"))
        self.button5.grid(column=1, row=1, padx=10, pady=10)
        self.button6 = Button(self.janelaInterfone, text="Falar com o apto 106",command= lambda: self.abrirChat("106"))
        self.button6.grid(column=2, row=1, padx=10, pady=10)
        self.button7 = Button(self.janelaInterfone, text="Falar com o apto 107",command= lambda: self.abrirChat("107"))
        self.button7.grid(column=0, row=2, padx=10, pady=10)
        self.button8 = Button(self.janelaInterfone, text="Falar com o apto 108",command= lambda: self.abrirChat("108"))
        self.button8.grid(column=1, row=2, padx=10, pady=10)
        self.button9 = Button(self.janelaInterfone, text="Falar com o apto 109",command= lambda: self.abrirChat("109"))
        self.button9.grid(column=2, row=2, padx=10, pady=10)
        self.janelaInterfone.mainloop()

    def acionaFechadura(self, apto: str):
        self.janelaMorador.destroy()
        self.janelaVisitante.destroy()
        if (porta.estadoGet() == False):
            porta.estadoSet(True)
            print("Porta aberta pelo apartamento ", apto)

    def abrirChat(self,apto:str):
        def enviaMensagem(mensagem: str):
            def enviaMensagemMorador():
                if (self.chatMorador0['text'] == ""):
                    self.chatMorador0['text'] = mensagem
                elif (self.chatMorador1['text'] == ""):
                    self.chatMorador1['text'] = mensagem
                elif (self.chatMorador2['text'] == ""):
                    self.chatMorador2['text'] = mensagem
                elif (self.chatMorador3['text'] == ""):
                    self.chatMorador3['text'] = mensagem
                else:
                    self.chatMorador0['text'] = mensagem
                    self.chatMorador1['text'] = ''
                    self.chatMorador2['text'] = ''
                    self.chatMorador3['text'] = ''
            def enviaMensagemVisitante():
                if (self.chatVisitante0['text'] == ""):
                    self.chatVisitante0['text'] = mensagem
                elif (self.chatVisitante1['text'] == ""):
                    self.chatVisitante1['text'] = mensagem
                elif (self.chatVisitante2['text'] == ""):
                    self.chatVisitante2['text'] = mensagem
                elif (self.chatVisitante3['text'] == ""):
                    self.chatVisitante3['text'] = mensagem
                else:
                    self.chatVisitante0['text'] = mensagem
                    self.chatVisitante1['text'] = ''
                    self.chatVisitante2['text'] = ''
                    self.chatVisitante3['text'] = ''

            enviaMensagemMorador()
            enviaMensagemVisitante()

        self.janelaMorador = Tk()
        self.janelaMorador.title("Interfone da porta do edifício")
        self.janelaMorador.geometry("600x250")
        self.janelaVisitante = Tk()
        self.janelaVisitante.title("Apartamento" + apto)
        self.janelaVisitante.geometry("600x250")

        self.chatMorador = Label(self.janelaMorador, text='Apartamento '+apto+": ")
        self.chatMorador.grid(column=0, row=0, padx=10, pady=10)
        self.entradaMorador = Entry(self.janelaMorador, width=30)
        self.entradaMorador.grid(column=1, row=0, padx=10, pady=10)
        self.buttonChatMorador = Button(self.janelaMorador, text="Enviar",command= lambda: enviaMensagem("Apartamento "+apto+": "+self.entradaMorador.get()))
        self.buttonChatMorador.grid(column=2, row=0, padx=10, pady=10)

        self.chatMorador0 = Label(self.janelaMorador, text= "")
        self.chatMorador0.grid(column=0, row=1, padx=10, pady=10)
        self.chatMorador1 = Label(self.janelaMorador, text="")
        self.chatMorador1.grid(column=0, row=2, padx=10, pady=10)
        self.chatMorador2 = Label(self.janelaMorador, text="")
        self.chatMorador2.grid(column=0, row=3, padx=10, pady=10)
        self.chatMorador3 = Label(self.janelaMorador, text="")
        self.chatMorador3.grid(column=0, row=4, padx=10, pady=10)

        self.chatVisitante = Label(self.janelaVisitante, text='Interfone: ')
        self.chatVisitante.grid(column=0, row=0, padx=10, pady=10)
        self.entradaVisitante = Entry(self.janelaVisitante, width=30)
        self.entradaVisitante .grid(column=1, row=0, padx=10, pady=10)
        self.buttonChatVisitante = Button(self.janelaVisitante, text="Enviar",command= lambda: enviaMensagem("Interfone: "+self.entradaVisitante.get()))
        self.buttonChatVisitante.grid(column=2, row=0, padx=10, pady=10)

        self.chatVisitante0 = Label(self.janelaVisitante, text= "")
        self.chatVisitante0.grid(column=0, row=1, padx=10, pady=10)
        self.chatVisitante1 = Label(self.janelaVisitante, text="")
        self.chatVisitante1.grid(column=0, row=2, padx=10, pady=10)
        self.chatVisitante2 = Label(self.janelaVisitante, text="")
        self.chatVisitante2.grid(column=0, row=3, padx=10, pady=10)
        self.chatVisitante3 = Label(self.janelaVisitante, text="")
        self.chatVisitante3.grid(column=0, row=4, padx=10, pady=10)

        self.button = Button(self.janelaMorador, text="Abrir porta do edifício", command= lambda : self.acionaFechadura(apto))
        self.button.grid(column=4, row=8, padx=10, pady=10)

        self.janelaMorador.mainloop()
        self.janelaVisitante.mainloop()







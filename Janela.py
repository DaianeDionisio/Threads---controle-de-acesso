from tkinter import *

class janela():

    def __init__(self):
        self.janelaInterfone = Tk()
        self.janelaInterfone.title("Porta 01 de acesso do Edificio")
        self.button1 = Button(self.janelaInterfone, text = "Falar com o apto 101")
        self.button1.grid(column=0, row=0, padx=10, pady=10)
        self.button2 = Button(self.janelaInterfone, text="Falar com o apto 102")
        self.button2.grid(column=1, row=0, padx=10, pady=10)
        self.button3 = Button(self.janelaInterfone, text="Falar com o apto 103")
        self.button3.grid(column=2, row=0, padx=10, pady=10)
        self.button4 = Button(self.janelaInterfone, text="Falar com o apto 104")
        self.button4.grid(column=0, row=1, padx=10, pady=10)
        self.button5 = Button(self.janelaInterfone, text="Falar com o apto 105")
        self.button5.grid(column=1, row=1, padx=10, pady=10)
        self.button6 = Button(self.janelaInterfone, text="Falar com o apto 106")
        self.button6.grid(column=2, row=1, padx=10, pady=10)
        self.button7 = Button(self.janelaInterfone, text="Falar com o apto 107")
        self.button7.grid(column=0, row=2, padx=10, pady=10)
        self.button8 = Button(self.janelaInterfone, text="Falar com o apto 108")
        self.button8.grid(column=1, row=2, padx=10, pady=10)
        self.button9 = Button(self.janelaInterfone, text="Falar com o apto 109")
        self.button9.grid(column=2, row=2, padx=10, pady=10)
        self.texto1 = Label(self.janelaInterfone, text="Ações da porta:")
        self.texto1.grid(column=0, row=4, padx=10, pady=10)
        self.janelaInterfone.mainloop()

    def acao(self,textTela: str):
        self.texto2 = Label(self.janelaInterfone, text=textTela)
        self.texto2.grid(column=1, row=4, padx=10, pady=10)
import threading
import time
from Porta import porta
from random import randint
from Janela import janela

def leitorAcesso():
    while(1):
        if (porta.estadoGet() == False):
            cartaoAcesso = randint(1000,1040)
            if(cartaoAcesso in acessosPermitidos):
                porta.estadoSet(True)
                string1 = ("Porta aberta com o cartão de acesso ", cartaoAcesso)
                print(string1)
                janela.acao(string1)
        time.sleep(7)

def acionaFechadura():
    while(1):
        apto = randint(101, 110)
        if (porta.estadoGet() == False):
            porta.estadoSet(True)
            print("Porta aberta pelo apartamento ", apto)
        time.sleep(30)

def timerFechaPorta():
    while(1):
        while(porta.estadoGet() == True):
            time.sleep(10)
            porta.estadoSet(False)
            print("Porta fechada por excesso de tempo!")

def enviaMensagem():

    time.sleep(2)

def recebeMensagem():
    time.sleep(2)

janela = janela()
acessosPermitidos = [1006,1008,1009,1012,1018,1023,1024,1030,1036,1039]
porta = porta()

thread1 = threading.Thread(target=leitorAcesso)
thread2 = threading.Thread(target=acionaFechadura)
thread3 = threading.Thread(target=timerFechaPorta)
thread4 = threading.Thread(target=enviaMensagem)
thread5 = threading.Thread(target=recebeMensagem)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()




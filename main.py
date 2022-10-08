import threading
import time
import Janela
from random import randint

def leitorAcesso():
    while(1):
        if (porta.estadoGet() == False):
            cartaoAcesso = randint(1000,1040)
            if(cartaoAcesso in acessosPermitidos):
                porta.estadoSet(True)
                print("Porta aberta com o cartão de acesso ", cartaoAcesso)
        time.sleep(7)

def timerFechaPorta():
    while(1):
        while(porta.estadoGet() == True):
            time.sleep(10)
            porta.estadoSet(False)
            print("Porta fechada por excesso de tempo!")

def interfone():
    janela = Janela.janela()

acessosPermitidos = [1006,1008,1009,1012,1018,1023,1024,1030,1036,1039]

porta = Janela.porta

thread1 = threading.Thread(target=leitorAcesso)
thread2 = threading.Thread(target=interfone)
thread3 = threading.Thread(target=timerFechaPorta)

thread1.start()
thread2.start()
thread3.start()





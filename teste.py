#var tkinter#
from time import strftime
from tkinter import *
import tkinter
from datetime import datetime

import pyglet 
pyglet.font.add_file("digital-7.ttf")
    
    #body tkinter#
#colors 
cor1= "#44dbbf" #meio azul
cor2= "#000000" #preto
cor3= "#f7f7f7" #branco

background= cor1
cor= cor3

janela=Tk()
janela.title()
janela.geometry("440x180")
janela.resizable(width=False, height=False)
janela.configure(bg=cor2)

def relogio():
    tempo= datetime.now()
    hora=tempo.strftime("%H:%M:%S")
    dia_semana=tempo.strftime("%A")
    dia=tempo.day
    mes=tempo.strftime("%b")
    ano=tempo.strftime("%Y")
    
    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config (text=dia_semana+ "   " + str(dia) + "/" + str(mes) + "/" + str(ano))



l1= Label(janela, text="", font=("digital-7 100"), bg=cor2, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5) 

l2= Label(janela, text="", font=("digital-7 17"), bg=cor2, fg=cor1)
l2.grid(row=1, column=0, sticky=NW, padx=5) 

relogio()
janela.mainloop()

    
    
    
    
    
    
    

     
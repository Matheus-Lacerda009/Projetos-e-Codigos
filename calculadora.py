from tkinter import *
  
#Classificando a calculadora como algo manipulável

class Calculadoraapp():
    def __init__(self):
        
        #Criação da janela

        self.root = Tk()
        self.root['bg'] = '#363636'
        self.root.geometry("250x200")
        self.root.title("Calculadora")
        
        #Criação de um espaçamento para centralizar

        self.em = Label(text="                   ")
        self.em.grid(row=7, column=2)
        self.em['bg'] = '#363636'

        #Criação das entradas de dados para o cálculo

        self.e = Entry()
        self.e.grid(row=1, column=4)
        self.e1 = Entry()
        self.e1.grid(row=2, column=4)

        #Criação do botão de soma

        self.bt = Button(text="+", command=self.sm)
        self.bt.grid(row=5, column=4)
        self.bt['bg'] = '#6495ED'
        
        #Criação do botão de subtração
        
        self.bt1 = Button(text="-", command=self.sb)
        self.bt1.grid(row=6, column=4)
        self.bt1['bg'] = '#6495ED'

        #Criação do botao de divisão

        self.bt2 = Button(text="/", command=self.dv)
        self.bt2.grid(row=7, column=4)
        self.bt2['bg'] = '#6495ED'

        #Criação do botão de multiplicação

        self.bt3 = Button(text="X", command=self.mt)
        self.bt3.grid(row=8, column=4)
        self.bt3['bg'] = '#6495ED'

        #Criação da Label onde o resultado vai aparecer

        self.lars = Label(text="")
        self.lars.grid(row=9, column=4)

        #Criacao da janela

        self.root.mainloop()

    #Definindo a função de soma

    def sm(self):
        try:
            self.a = float(self.e.get())
            self.b = float(self.e1.get())
            self.c = self.a+self.b

            self.lars["text"] = self.c
        except ValueError:  
            self.lars["text"] = "ERRO"

    #Definindo a função de subtração

    def sb(self):
        try:
            self.d = float(self.e.get())
            self.z = float(self.e1.get())
            self.f = self.d-self.z

            self.lars["text"] = self.f
        except ValueError:
            self.lars["text"] = "ERRO"

    #Definindo a função de divisão

    def dv(self):
        try:
            self.g = float(self.e.get())
            self.h = float(self.e1.get())
            self.i = self.g/self.h

            self.lars["text"] = self.i
        except ValueError:
            self.lars["text"] = "ERRO"

    #Definindo a função de multiplicação

    def mt(self):
        try:
            self.j = float(self.e.get())
            self.k = float(self.e1.get())
            self.l = self.j*self.k

            self.lars["text"] = self.l
        except ValueError:
            self.lars["text"] = "ERRO"

#Finalizando o código da calduladora e fazendo ela rodar

Calculadoraapp()
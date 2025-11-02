#Importando biblioteca para criar interfaces
from tkinter import *

#Criando classe para a calculadora
class Calculadoraapp():
    
    #Definindo função de início
    def __init__(self):
        
        #Criando variável para sabermos se alguma operação já foi selecionada
        self.operacaoSelecionada = False

        #Variável para mostrar a operação completa
        self.entrada = ""

        #Criando a janela e customizando
        self.janela = Tk()
        self.janela['bg'] = '#000000'
        self.janela.geometry("250x200")
        self.janela.title("Calculadora")
        
        #Criando os botões dos números
        self.bt1 = Button(text="1", command=self.um)
        self.bt1.grid(row=7, column=7)
        self.bt1['bg'] = '#6495ED'

        self.bt2 = Button(text="2", command=self.dois)
        self.bt2.grid(row=7, column=8)
        self.bt2['bg'] = '#6495ED'

        self.bt3 = Button(text="3", command=self.tres)
        self.bt3.grid(row=7, column=9)
        self.bt3['bg'] = '#6495ED'

        self.bt4 = Button(text="4", command=self.quatro)
        self.bt4.grid(row=6, column=7)
        self.bt4['bg'] = '#6495ED'

        self.bt5 = Button(text="5", command=self.cinco)
        self.bt5.grid(row=6, column=8)
        self.bt5['bg'] = '#6495ED'

        self.bt6 = Button(text="6", command=self.seis)
        self.bt6.grid(row=6, column=9)
        self.bt6['bg'] = '#6495ED'

        self.bt7 = Button(text="7", command=self.sete)
        self.bt7.grid(row=5, column=7)
        self.bt7['bg'] = '#6495ED'

        self.bt8 = Button(text="8", command=self.oito)
        self.bt8.grid(row=5, column=8)
        self.bt8['bg'] = '#6495ED'

        self.bt9 = Button(text="9", command=self.nove)
        self.bt9.grid(row=5, column=9)
        self.bt9['bg'] = '#6495ED'

        self.bt10 = Button(text="0", command=self.zero)
        self.bt10.grid(row=8, column=8)
        self.bt10['bg'] = '#6495ED'

        #Criando os botões das operações
        self.bt11 = Button(text="+", command=self.sm)
        self.bt11.grid(row=8, column=4)
        self.bt11['bg'] = '#6495ED'
        
        self.bt12 = Button(text="-", command=self.sb)
        self.bt12.grid(row=5, column=4)
        self.bt12['bg'] = '#6495ED'

        self.bt13 = Button(text="/", command=self.dv)
        self.bt13.grid(row=6, column=4)
        self.bt13['bg'] = '#6495ED'

        self.bt14 = Button(text="X", command=self.mt)
        self.bt14.grid(row=7, column=4)
        self.bt14['bg'] = '#6495ED'
        
        #Criando o botão para exibir o resultado da conta
        self.bt15 = Button(text="=", command=self.re)
        self.bt15.grid(row=7, column=10)
        self.bt15['bg'] = '#6495ED'

        #Criando o botão para limpar a entrada
        self.bt16 = Button(text="C", command=self.clear)
        self.bt16.grid(row=5, column=10)
        self.bt16['bg'] = '#6495ED'

        #Criando uma Label para nos mostrar a operação
        self.visor = Label(text="")
        self.visor.grid(row=4, column=4)

        #Inicializando a janela e criando um loop
        self.janela.mainloop()

    #Criando as funções para os botões dos números
    def um(self):
        if len(self.entrada) > 10:
            return
        self.entrada += "1"
        self.visor["text"] = self.entrada

    def dois(self):
        if len(self.entrada) > 10:
            return
        self.entrada += "2"
        self.visor["text"] = self.entrada

    def tres(self):
        if len(self.entrada) > 10:
            return
        self.entrada += "3"
        self.visor["text"] = self.entrada

    def quatro(self):
        if len(self.entrada) > 10:
            return
        self.entrada += "4"
        self.visor["text"] = self.entrada 

    def cinco(self):
        if len(self.entrada) > 10:
            return
        self.entrada += "5"
        self.visor["text"] = self.entrada            

    def seis(self):
        if len(self.entrada) > 10:
            return
        self.entrada += "6"
        self.visor["text"] = self.entrada

    def sete(self):
        if len(self.entrada) > 10:
            return
        self.entrada += "7"
        self.visor["text"] = self.entrada

    def oito(self):
        if len(self.entrada) > 10:
            return
        self.entrada += "8"
        self.visor["text"] = self.entrada

    def nove(self):
        if len(self.entrada) > 10:
            return
        self.entrada += "9"
        self.visor["text"] = self.entrada
    
    def zero(self):
        if len(self.entrada) > 10:
            return
        self.entrada += "0"
        self.visor["text"] = self.entrada
    
    #Criando as funções para os botões das operações
    def sm(self):
        if self.operacaoSelecionada == False:
            self.entrada += "+"
            self.visor["text"] = self.entrada
            self.operacaoSelecionada = True
    
    def sb(self):
        if self.operacaoSelecionada == False:
            self.entrada += "-"
            self.visor["text"] = self.entrada
            self.operacaoSelecionada = True
    
    def mt(self):
        if self.operacaoSelecionada == False:
            self.entrada += "X"
            self.visor["text"] = self.entrada
            self.operacaoSelecionada = True
    
    def dv(self):
        if self.operacaoSelecionada == False:
            self.entrada += "/"
            self.visor["text"] = self.entrada
            self.operacaoSelecionada = True
    
    #Criando uma função para o botão que limpa a entrada
    def clear(self):
        self.entrada = ""
        self.visor["text"] = ""
        self.operacaoSelecionada = False

    #Criando uma função para exibir o resultado da conta
    def re(self):
        #Condição para exibir a soma
        if "+" in self.entrada:
            n1 = self.entrada[0:self.entrada.find("+")]
            n2 = self.entrada[self.entrada.find("+") + 1 : len(self.entrada)]
            operacao = int(n1) + int(n2)
            self.visor["text"] = operacao
        
        #Condição para exibir a subtração
        elif "-" in self.entrada:
            n1 = self.entrada[0:self.entrada.find("-")]
            n2 = self.entrada[self.entrada.find("-") + 1 : len(self.entrada)]
            operacao = int(n1) - int(n2)
            self.visor["text"] = operacao
        
        #Condição para exibir a divisão
        elif "/" in self.entrada:
            n1 = self.entrada[0:self.entrada.find("/")]
            n2 = self.entrada[self.entrada.find("/") + 1: len(self.entrada)]
            operacao = float(n1) / float(n2)
            self.visor["text"] = operacao

        #Condição para exibir a multiplicação
        elif "X" in self.entrada:
            n1 = self.entrada[0:self.entrada.find("X")]
            n2 = self.entrada[self.entrada.find("X") + 1: len(self.entrada)]
            operacao = int(n1) * int(n2)
            self.visor["text"] = operacao
            
#Executando a classe
Calculadoraapp()
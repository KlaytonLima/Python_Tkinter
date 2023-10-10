from tkinter import * #chamando a biblioteca

root = Tk() #criando uma variavel para receber Tkinter

class Aplicacao(): #criando uma classe
    def __init__(self): #criando funções automáticas
        self.root = root 
        self.tela()
        root.mainloop() 
    def tela(self): #criando funções de configuração de tela
        self.root.title("Cadastro de Clientes")
        self.root.configure(background= 'Lightblue') 
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width= 900, height=700)    
        self.root.minsize(width=400, height=300) 
        


Aplicacao() #chamando a classe com suas funções


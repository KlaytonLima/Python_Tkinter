from tkinter import * #Chamando a biblioteca

root = Tk() #Criando uma variavel para receber Tkinter

class Aplicacao(): #Criando uma classe
    def __init__(self): #Criando funções automáticas
        self.root = root 
        self.tela()
        self.frames_de_tela()
        root.mainloop() #Loop para manter a tela visível 
    def tela(self): #Criando funções de configuração de tela
        self.root.title("Cadastro de Clientes") #Título
        self.root.configure(background= 'Lightblue') #Cor de fundo
        self.root.geometry('700x500') #Tamanho de inicialização de tela
        self.root.resizable(True, True) # Responsividade
        self.root.maxsize(width= 900, height=700) #Maximo tamanho da tela    
        self.root.minsize(width=400, height=300) #Minimo tamanho da tela
    def frames_de_tela(self): #Criando frames
        self.frame_1 = Frame(self.root, bd= 4, bg= 'whitesmoke', highlightbackground= 'lightgray', 
                             highlightthickness= 3) #Configuração frame_1
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)

        self.frame_2 = Frame(self.root, bd= 4, bg= 'whitesmoke', highlightbackground= 'lightgray', 
                             highlightthickness= 3) #Configuração frame_2
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)

Aplicacao() #Chamando a classe com suas funções


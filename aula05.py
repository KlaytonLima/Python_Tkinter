from tkinter import * #Chamando a biblioteca

root = Tk() #Criando uma variavel para receber Tkinter

class Aplicacao(): #Criando uma classe
    def __init__(self): #Criando funções automáticas
        self.root = root 
        self.tela()
        self.frames_de_tela()
        self.widgets_frame_1()
        root.mainloop() #Loop para manter a tela visível 
    def tela(self): #Criando funções de configuração de tela
        self.root.title("Cadastro de Clientes") #Título
        self.root.configure(background= '#008080') #Cor de fundo
        self.root.geometry('700x500') #Tamanho de inicialização de tela
        self.root.resizable(True, True) # Responsividade
        self.root.maxsize(width= 900, height=700) #Maximo tamanho da tela    
        self.root.minsize(width=400, height=300) #Minimo tamanho da tela
    def frames_de_tela(self): #Criando frames
        self.frame_1 = Frame(self.root, bd= 1, bg= '#F8F8FF', highlightbackground= '#008B8B', 
                             highlightthickness= 3) #Configuração frame_1
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)

        self.frame_2 = Frame(self.root, bd= 1, bg= '#F8F8FF', highlightbackground= '#008B8B', 
                             highlightthickness= 3) #Configuração frame_2
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)
    def widgets_frame_1(self): #Criando botões dentro do fram_1
        #Botão Limpar
        self.bt_limpar = Button(self.frame_1, text= "Limpar", bg= '#008080', font = ('verdana', 8, 'bold'), bd= 2)
        self.bt_limpar.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        #Botão Buscar
        self.bt_buscar = Button(self.frame_1, text= "Buscar", bg= '#008080', font = ('verdana', 8, 'bold'), bd= 2)
        self.bt_buscar.place(relx= 0.3, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        #Botão Novo
        self.bt_novo = Button(self.frame_1, text= "Limpar", bg= '#008080', font = ('verdana', 8, 'bold'), bd= 2)
        self.bt_novo.place(relx= 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        #Botão Alterar
        self.bt_alterar = Button(self.frame_1, text= "Alterar", bg= '#008080', font = ('verdana', 8, 'bold'), bd= 2)
        self.bt_alterar.place(relx= 0.7, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        #Botão Apagar
        self.bt_apagar = Button(self.frame_1, text= "Apagar", bg= '#008080', font = ('verdana', 8, 'bold'), bd= 2)
        self.bt_apagar.place(relx= 0.8, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        #Criação da label "Código"
        self.lb_codigo = Label(self.frame_1, text= "Código", bg= '#F8F8FF', font = ('verdana', 8, 'bold'))
        self.lb_codigo.place(relx= 0.05, rely= 0.05)
        #Criação do input do label "Código"
        self.codigo_entry = Entry(self.frame_1, bg= '#008080', font=('verdana', 8, 'bold', 'italic'))
        self.codigo_entry.place(relx= 0.05, rely= 0.15, relwidth= 0.07)

        #Criação da label "Nome"
        self.lb_nome = Label(self.frame_1, text= "Nome", bg= '#F8F8FF', font = ('verdana', 8, 'bold'))
        self.lb_nome.place(relx= 0.05, rely= 0.35)
        #Criação do input do label "Nome"
        self.nome_entry = Entry(self.frame_1, bg= '#008080', font=('verdana', 8, 'bold', 'italic'))
        self.nome_entry.place(relx= 0.05, rely= 0.45, relwidth= 0.7)

        #Criação da label "Telefone"
        self.lb_telefone = Label(self.frame_1, text= "Telefone", bg= '#F8F8FF', font = ('verdana', 8, 'bold'))
        self.lb_telefone.place(relx= 0.05, rely= 0.6)
        #Criação do input do label "Telefone"
        self.telefone_entry = Entry(self.frame_1, bg= '#008080', font=('verdana', 8, 'bold', 'italic'))
        self.telefone_entry.place(relx= 0.05, rely= 0.7, relwidth= 0.4)

        #Criação da label "Cidade"
        self.lb_cidade = Label(self.frame_1, text= "Cidade", bg= '#F8F8FF', font = ('verdana', 8, 'bold'))
        self.lb_cidade.place(relx= 0.5, rely= 0.6)
        #Criação do input do label "Cidade"
        self.cidade_entry = Entry(self.frame_1, bg= '#008080', font=('verdana', 8, 'bold', 'italic'))
        self.cidade_entry.place(relx= 0.5, rely= 0.7, relwidth= 0.4)
    


Aplicacao() #Chamando a classe com suas funções


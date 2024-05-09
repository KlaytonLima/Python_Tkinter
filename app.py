from tkinter import * 
from tkinter import ttk 
import sqlite3

root = Tk() 

# Classe Funcao
class Funcao():     
    def limpa_tela(self):
       self.codigo_entry.delete(0, END)
       self.nome_entry.delete(0, END)
       self.telefone_entry.delete(0, END)
       self.cidade_entry.delete(0, END)
    def conecta_bd(self): 
        self.conn = sqlite3.connect("clientes.bd") 
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados") 
    def desconecta_bd(self): 
        self.conn.close(); print("Desconectando o banco de dados") 
    def montaTabelas(self): 
        self.conecta_bd() 
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone_cliente INTERGER(20) NOT NULL,
                cidade_cliente CHAR(40) NOT NULL                                                                          
            );
        """ )  
        self.conn.commit(); print("Banco de dados criado") 
        self.desconecta_bd() 
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()    
    def add_cliente(self):
            self.variaveis()
            self.codigo = self.codigo_entry.get()
            self.nome = self.nome_entry.get()
            self.telefone = self.telefone_entry.get()
            self.cidade = self.cidade_entry.get()
            self.conecta_bd()    
            self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone_cliente, cidade_cliente)
                VALUES(?, ?, ?)""", (self.nome, self.telefone, self.cidade))
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista()
            self.limpa_tela()
           
    def select_lista(self):
        self.lista_clientes.delete(*self.lista_clientes.get_children())
        self.conecta_bd()
        lista= self.cursor.execute(""" SELECT cod, nome_cliente, telefone_cliente, cidade_cliente FROM clientes
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.lista_clientes.insert("", END, values=i)
        self.desconecta_bd()
    def onDoubleClick(self, event):
        self.limpa_tela()
        self.lista_clientes.selection()

        for n in self.lista_clientes.selection():
            col1, col2, col3, col4 = self.lista_clientes.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
    def deleta_cliente(self):                            
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" DELETE FROM clientes WHERE cod = ? """, (self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()  
    def altera_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone_cliente = ?, cidade_cliente = ?
            WHERE cod = ?""", (self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def  busca_cliente(self):
        self.conecta_bd()
        self.lista_clientes.delete(*self.lista_clientes.get_children())
        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute( """ SELECT cod, nome_cliente, telefone_cliente, cidade_cliente FROM  clientes
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC """ % nome)
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.lista_clientes.insert("", END, values=i)
        self.limpa_cliente()    
        self.desconecta_bd()      
# Classe Aplicacao
class Aplicacao(Funcao): 
    def __init__(self): 
        self.root = root 
        self.tela() 
        self.frames_de_tela() 
        self.widgets_frame_1() 
        self.lista_frame_2() 
        self.montaTabelas()
        self.select_lista()
        self.Menus()
        root.mainloop() 
    def tela(self): 
        self.root.title("Cadastro de Clientes") 
        self.root.configure(background= '#008080') 
        self.root.geometry('700x500') 
        self.root.resizable(True, True) 
        self.root.maxsize(width= 900, height=700)     
        self.root.minsize(width=400, height=300) 
    def frames_de_tela(self):
        self.frame_1 = Frame(self.root, bd= 1, bg= '#F8F8FF', highlightbackground= '#008B8B',  
                             highlightthickness= 3) 
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46) 

        self.frame_2 = Frame(self.root, bd= 1, bg= '#F8F8FF', highlightbackground= '#008B8B', 
                             highlightthickness= 3) #Configuração frame_2
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46) 
    def widgets_frame_1(self): 
        #Botão Limpar
        self.bt_limpar = Button(self.frame_1, text= "Limpar", bg= '#008080', font = ('verdana', 8, 'bold'),
                                bd= 2, command= self.limpa_tela)
        self.bt_limpar.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        #Botão Buscar
        self.bt_buscar = Button(self.frame_1, text= "Buscar", bg= '#008080', font = ('verdana', 8, 'bold'), bd= 2, command= self.busca_cliente)
        self.bt_buscar.place(relx= 0.3, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        #Botão Novo
        self.bt_novo = Button(self.frame_1, text= "Novo", bg= '#008080', font = ('verdana', 8, 'bold'), bd= 2, command= self.add_cliente)
        self.bt_novo.place(relx= 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        #Botão Alterar
        self.bt_alterar = Button(self.frame_1, text= "Alterar", bg= '#008080', font = ('verdana', 8, 'bold'), bd= 2, command= self.altera_cliente)
        self.bt_alterar.place(relx= 0.7, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        #Botão Apagar
        self.bt_apagar = Button(self.frame_1, text= "Apagar", bg= '#008080', font = ('verdana', 8, 'bold'), bd= 2, command= self.deleta_cliente)
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
    def lista_frame_2(self): #Cliando a função grid
        self.lista_clientes = ttk.Treeview(self.frame_2, height= 3, columns=('col1', 'col2', 'col3', 'col4')) #Especificando a quantidade de colunas da grid
        self.lista_clientes.heading('#0', text="") #Criando uma coluna vazia
        self.lista_clientes.heading('#1', text="Código") #Descrevendo a coluna
        self.lista_clientes.heading('#2', text="Nome") #Descrevendo a coluna
        self.lista_clientes.heading('#3', text="Telefone") #Descrevendo a coluna
        self.lista_clientes.heading('#4', text="Cidade") #Descrevendo a coluna

        #Configurando o tamanho de cada coluna dentro da grid
        self.lista_clientes.column('#0', width= 1) 
        self.lista_clientes.column('#1', width= 50)
        self.lista_clientes.column('#2', width= 200)
        self.lista_clientes.column('#3', width= 125)
        self.lista_clientes.column('#4', width= 125)

        #Configurando as posições das colunas
        self.lista_clientes.place(relx= 0.01, rely= 0.1, relwidth= 0.95, relheight= 0.85)

        #Criando um scrool na grid
        self.scroollista = Scrollbar(self.frame_2, orient= 'vertical') #Direcionando o scrool para o frame_2
        self.lista_clientes.configure(yscroll=self.scroollista.set) #Direcionando o scrool para a grid
        self.scroollista.place(relx= 0.96, rely= 0.1, relwidth= 0.04, relheight= 0.85) #Configurando o scrool na grid
        self.lista_clientes.bind("<Double-1>", self.onDoubleClick)
    def Menus(self): #Criando uma função de menu
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy() #Criando uma saída fechabdo a tela

        menubar.add_cascade(label= "Opções", menu= filemenu)
        menubar.add_cascade(label= "Sobre", menu= filemenu2)

        filemenu.add_command(label= "Sair", command= Quit)
        filemenu2.add_command(label= "Limpa Cliente", command= self.limpa_tela)
Aplicacao() #Chamando a classe com suas funções


class Node:
    def __init__(self, data):
        # 1 -construtor do nó
        self.data = data
        self.nextNode = None

    def  getData(self):
        # 2 - retorna o dado armazenado no nó
        return self.data

    def setData(self, data):
        # 3 - atribui o valor a o nó
        self.data = data

    def getNextNode(self):
        # 4 - retorna a referencia do proximo nó
        return self.nextNode

    def setNextNode(self,newNode):
        self.nextNode = newNode

class Node2:
    #classe que define um nodo duplo de uma estutura de dados (lista duplamente encadeada)
    def __init__(self,data):
        #construtor do nó
        self.data =data
        self.nextNode = None
        self.antNode = None

    def getAntNode(self):
        #retorna a referencia do nó anterior
        return self.antNode

    def setAntNode(self, newNode):
        # ajusta a referencia do nó anterior
        self.antNode =  newNode

class List:
    # classe para uma lista encadeada, eata classe tem dois ponteiros:
    # firstNode - aponta para o primeiro nodo da lista
    # lastNode - aponta para o ultimo nodo da lista
    # ao iniciar a lista ambos os ponteiros apontam para NULO

    def __init__(self):
        #construtor da lista
        self.firstNode = None
        self.lastNode = None

    #@property
    def imprimir(self):
        #@override do Estatuto String
        if self.isEmpty():
            return "A lista está vazia"
        correntNode = self.firstNode
        string = "A lista é "
        while correntNode is not None:
            string += str( " "+correntNode.getData() )
            correntNode = correntNode.getNextNode()
        return string

    def insertAtBegin(self, value):
        #insere no inicio da lista
        newNode = Node(value)#instacia um novo node
        if self.isEmpty():# inserção na llista vazia
            self.firstNode = self.lastNode = newNode
        else: #insersão para lista não vazia
            newNode.setNextNode(self.firstNode)
            self.firstNode  =  newNode

    def insertAtEnd(self, value):
        #insere no final da lista
        newNode =Node(value)
        if self.isEmpty(): # se a lista está vazia
            self.firstNode = self.lastNode = newNode
        else:
            self.lastNode.setNextNode(newNode)
            self.lastNode = newNode

    def removeFromBegin(self):
        #remove o nodo inicial
        if self.isEmpty():
            raise IndexError("remoção de uma lista vazia ")
        firstNodeValue = self.firstNode.getData()
        if self.firstNode is self.lastNode:
            self.firstNode = self.lastNode = None
        else:
            self.firstNode = self.firstNode.getNextNode()
        return firstNodeValue

    def removeFromEnd(self):
        #remove o ultimo da lista
        if self.isEmpty():
            raise IndexError("remoção de lista vazia")
        lastNodeValue = self.lastNode.getData()
        if self.firstNode is self. lastNode:
            self.firstNode = self.lastNode = None
        else:
            currentNode =  self.firstNode
            while currentNode.getNextNode() is not self.lastNode:
                currentNode =  currentNode.getNextNode()
            currentNode.setNextNode(None)
            self.lastNode = currentNode
        return lastNodeValue
    def isEmpty(self):
        #A lista está vazia? True e False
        return self.firstNode is None


##############################################################################################
######################### começando a brincar con listas encadeadas ##########################
##############################################################################################

def instuctions():
    #imprime instuções para usuário
    print("Ente com uma opção: \n"
          "1 - Para insetir no inicio da lista\n"
          "2 - Para inserir no final da lista\n"
          "3 - Para deletar no começo da lista\n"
          "4 - Para deletar no final da lista\n"
          "5 - Para sair")

listaObjetos = List() #instanciando um objeto
instuctions()
choice = input("? ")

while choice !="5":
    if choice =="1":
        listaObjetos.insertAtBegin(input("Entre com o valor: "))
        print(listaObjetos.imprimir())
    elif choice == "2":
        listaObjetos.insertAtEnd(input("Entre com o valor: "))
        print(listaObjetos.imprimir())
    elif choice == "3":
        try:
            value = listaObjetos.removeFromBegin()
        except IndexError as message:
            print("Falha na operação "+message)
        else:
            print(value +" Valor removido")
            print(listaObjetos.imprimir())
    elif choice == "4":
        try:
            value = listaObjetos.removeFromEnd()
        except IndexError as message:
            print("Falha na operação "+ message)
        else:
            print(value+" removido da lista")
            print(listaObjetos.imprimir())
    else:
        print("Operação inválida: "+choice)
    instuctions()
    choice = input("\n? ")
print("Fim do programa")






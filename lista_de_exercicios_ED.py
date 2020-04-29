# #revertendo uma lista
# lista = [1,2,3,4,5,6,7,8,9]
#
# def reverter(lista):
#     lista.reverse()
#     print(lista)
#
# reverter(lista)
#
# #intercalando duas listas
#
# l = ['A','B','C']
# k = ['D','E','F','F']
#
# def intercala(L,K):
#     intercalada = []
#     for a,b in zip(L, K):
#         intercalada.append(a)
#         intercalada.append(b)
#     return intercalada
#
# Intercalada = intercala(l, k)
#
# print(Intercalada)

class no:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class lista_encadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0


    def adicionar(self, elemento ):
        if self.inicio:
            apontador = self.inicio
            while(apontador.next):
                
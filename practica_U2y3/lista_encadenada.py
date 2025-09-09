class Nodo:
    __item : int
    __siguiente : None

    def __init__(self, item):
        self.__item = item
        self.__siguiente = None

    def getItem(self):
        return self.__item
    def getSiguiente(self):
        return self.__siguiente
    
    def setItem(self, item):
        self.__item = item
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

class ListaEncadenada:
    __cantidad : int
    __cab : Nodo

    def __init__(self):
        self.__cab = None
        self.__cantidad = 0

    def vacia(self):
        return self.__cab is None
    
    def insertar(self, x, pos):
        if self.__cantidad >= 0:
            if pos>=1 and pos<=self.__cab+2:
                for i in range(self.__cab, pos-2, -1):
                    self.__arreglo[i+1] = self.__arreglo[i]
                self.__arreglo[pos-1] = x
                self.__cab += 1
                return x
        nuevo_nodo = Nodo(x)
        nuevo_nodo.setSiguiente(self.__cab)
        self.__cab = nuevo_nodo
        self.__cantidad += 1

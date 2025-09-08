class Celda:
    __item: int
    __siguiente: None

    def __init__(self, item):
        self.__item = item
        self.__siguiente = None
    
    def getitem(self):
        return self.__item
    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    def setitem(self, item):
        self.__item = item

class PilaEncadenada:
    __cantidad: int
    __tope: Celda

    def __init__(self):
        self.__tope = None

    def vacia(self):
        return self.__tope is None

    def insertar(self, x):
        nueva_celda = Celda(x)
        nueva_celda.setSiguiente(self.__tope)
        self.__tope = nueva_celda
        self.__cantidad += 1
       
    def suprimir(self):
        elem_eliminado = self.__tope.getitem()
        self.__tope = self.__tope.getSiguiente()
        self.__cantidad -= 1
        return elem_eliminado

    def mostrar(self):
        aux = self.__tope
        while aux is not None:
            print(int(aux.getitem()))
            aux = aux.getSiguiente()
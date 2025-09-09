import numpy as np 

"""---Declaro una lista---"""
class ListaSecuencial:
    __cantidad: int
    __tope: int
    __arreglo: np.ndarray

    def __init__(self, cantidad=0):
        self.__cantidad = cantidad
        self.__tope = -1
        self.__arreglo = np.empty(self.__cantidad, dtype=int)

    def vacia(self):
        return self.__tope == -1
    def llena(self):
        return self.__tope == self.__cantidad - 1
    
    """---Método insertar un elemento nuevo en la lista---"""
    def insertar(self, x, pos):
        if self.__cantidad >= 0:
            if pos>=1 and pos<=self.__tope+2:
                for i in range(self.__tope, pos-2, -1):
                    self.__arreglo[i+1] = self.__arreglo[i]
                self.__arreglo[pos-1] = x
                self.__tope += 1
                return x

# si el arreglo tiene 5 elementos entonces:
# tope = 4
# si quiero insertar en la posicion 3 seria en indice 2 entonces:
# 3-2= 1 que es la posicion a donde anterior donde voy a insertar es decir que el 
# elemento de esa posicion no se va a mover. 
# 0|1|2|3|4
# 0|1| |->2|3|4

    """---Método suprimir elemento de la lista---"""
    def suprimir(self, pos):
        #if self.vacia() or pos<0 or pos>=self.__cantidad:
        elem_removido= self.__arreglo[pos-1]
        for i in range (pos-1, self.__cantidad-1):
            self.__arreglo[i] = self.__arreglo[i+1]
        self.__cantidad -= 1
        print (f"El elemento removido es {elem_removido}")

    def recuperar(self, pos):
        elem_recuperar = self.__arreglo[pos-1]
        print(f"El elemento en la posicion {pos} es {elem_recuperar}")
       
    def buscar(self, elemento):
        for i in range (self.__cantidad):
            if self.__arreglo[i]==elemento:
                return (f"La posición del elemento es {i}")
        return -1

    def mostrar(self):
        if (not self.vacia()):
            for i in range(self.__tope, -1, -1):
                print(int(self.__arreglo[i]))
        else:
            print("lista vacia")


def prueba_insert(num):
    
    while num >= 0:
        num=int(input("ingrese numero positivo a insertar"))
        i=int(input("ingrese posicion"))
        lista.insertar(num, i)
        
    
    # print("La lista es: ")
    # lista.mostrar()

if __name__ == "__main__":
    lista = ListaSecuencial(5)
    print("Ingrese un numero entero positivo para empezar: ")
    n = int(input())
    prueba_insert(n)
    print("La lista es: ")
    lista.mostrar()
    # print ("Ingresar posicion del elemento a recuperar")
    # pos_recu = int(input())
    # lista.recuperar(pos_recu)
    
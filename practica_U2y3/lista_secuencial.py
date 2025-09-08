import numpy as np 

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
        
    def mostrar(self):
        if (not self.vacia()):
            for i in range(self.__tope, -1, -1):
                print(int(self.__arreglo[i]))
        else:
            print("Pila vacia")


def prueba_insert(num):
    lista = ListaSecuencial(5)
    
    while num >= 0:
        num=int(input("ingrese numero positivo a insertar"))
        i=int(input("ingrese posicion"))
        lista.insertar(num, i)
        
    
    print("La lista es: ")
    lista.mostrar()

if __name__ == "__main__":
    print("Ingrese un numero entero positivo para empezar: ")
    n = int(input())
    prueba_insert(n)
   

# si el arreglo tiene 5 elementos entonces:
# tope = 4
# si quiero insertar en la posicion 3 seria en indice 2 entonces:
# 3-2= 1 que es la posicion a donde anterior donde voy a insertar es decir que el 
# elemento de esa posicion no se va a mover. 
# 0|1|2|3|4
# 0|1| |->2|3|4

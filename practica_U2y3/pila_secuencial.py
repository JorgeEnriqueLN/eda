import numpy as np

class PilaSecuencial:
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
    
    def insertar(self, x):
        if self.__tope < self.__cantidad - 1: #esto se puede reemplazar por self.llena()
            self.__tope += 1
            self.__arreglo[self.__tope] = x
            return x
        else:
            return 0
        
    # def insertar(self, x):    #Es el mismo insertar pero usando el método llena
    #     if != self.llena(): 
    #         self.__tope += 1
    #         self.__arreglo[self.__tope] = x
    #         return x
    #     else:
    #         return 0
        
    def suprimir(self):
        x = int 
        if self.vacia():
            print("Pila vacia")
            return 0
        else:
            x = self.__tope - 1
            return x
        
    def mostrar(self):
        if (not self.vacia()):
            for i in range(self.__tope, -1, -1):
                print(int(self.__arreglo[i]))
        else:
            print("Pila vacia")

def conversionabinario(num):
    pila = PilaSecuencial(5)
    while num >= 2:
        resto = num % 2
        pila.insertar(resto)
        num = num // 2
    pila.insertar(num)
    print("El numero en binario es: ")
    pila.mostrar()

if __name__ == "__main__":
    print("Ingrese un numero entero a convertir: ")
    n = int(input())
    conversionabinario(n)
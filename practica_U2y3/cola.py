import numpy as np

class Cola:
    __cantidad: int
    __inicio: int
    __final: int
    __arreglo: np.ndarray

    def __init__(self, cantidad=0):
        self.__cantidad = cantidad
        self.__inicio = 0
        self.__final = -1
        self.__arreglo = np.zeros(self.__cantidad, dtype=int)

    def vacia(self):
        if self.__final == -1:
            return 0

    def insertar(self, x):
        if self.__final < self.__cantidad - 1:
            self.__final += 1
            self.__arreglo[self.__final] = x
        else:
            return 0
        return x

    def suprimir(self):
        if self.vacia():
            print("Cola vacia")
            return 0
        else:
            for i in range(self.__inicio, self.__final):
                self.__arreglo[i] = self.__arreglo[i + 1]
            self.__final -= 1

    def mostrar(self):
        if self.vacia():
            print("Cola vacia")
        else:
            for i in range(self.__inicio, self.__final + 1):
                print(int(self.__arreglo[i]))
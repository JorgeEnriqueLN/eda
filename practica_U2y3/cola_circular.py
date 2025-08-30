import numpy as np

class Cola:
    def __init__(self, capacidad=10):
        # Aumentamos la capacidad por defecto para que sea más funcional
        self.__capacidad = capacidad
        self.__inicio = -1
        self.__final = -1
        self.__arreglo = np.empty(self.__capacidad, dtype=int)
        
    def vacia(self):
        # La cola está vacía si el índice de inicio es -1
        return self.__inicio == -1

    def insertar(self, x):
        if (self.__final + 1) % self.__capacidad == self.__inicio:
            # Cola llena: si la siguiente posición de final es igual a inicio, la cola está llena
            print("Cola llena")
            return None

        if self.vacia():
            self.__inicio = 0
            self.__final = 0
        else:
            # Usamos el operador módulo para una implementación de cola circular
            self.__final = (self.__final + 1) % self.__capacidad
            
        self.__arreglo[self.__final] = x
        return x

    def suprimir(self):
        if self.vacia():
            print("Cola vacia")
            return None
        
        elemento_suprimido = self.__arreglo[self.__inicio]
        
        if self.__inicio == self.__final:
            # Si solo queda un elemento, la cola se vacía
            self.__inicio = -1
            self.__final = -1
        else:
            # Desplazamos solo el índice de inicio, una operación O(1)
            self.__inicio = (self.__inicio + 1) % self.__capacidad
        
        return elemento_suprimido

    def mostrar(self):
        if self.vacia():
            print("Cola vacia")
            return

        # Para mostrar los elementos en el orden correcto en una cola circular
        i = self.__inicio
        while True:
            print(self.__arreglo[i], end=' ')
            if i == self.__final:
                break
            i = (i + 1) % self.__capacidad
        print()
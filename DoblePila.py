import numpy as np

class DoblePila:
    __tope1:int = None
    __tope2:int = None
    __dimension:int = None
    __arreglo:np.ndarray = None
    __tipo:type = None

    def __init__(self, dimension: int, tipo:type) -> None:
        self.__dimension = dimension
        self.__tope1 = 0
        self.__tope2 = self.__dimension - 1
        self.__tipo = tipo
        self.__arreglo = np.empty(self.__dimension, dtype=tipo)
    
    def apilarPila1(self, elemento):
        assert self.__tope1 <= self.__tope2, "No queda espacio en la doble pila"
        assert isinstance(elemento, self.__tipo), "Solo se pueden agregar elementos del tipo {0} a la doble pila, no {1}".format(self.__tipo, type(elemento))
        self.__arreglo[self.__tope1] = elemento
        self.__tope1 += 1

    
    def apilarPila2(self, elemento):
        assert self.__tope1 <= self.__tope2, "No queda espacio en la doble pila"
        assert isinstance(elemento, self.__tipo), "Solo se pueden agregar elementos del tipo {0} a la doble pila, no {1}".format(self.__tipo, type(elemento))
        self.__arreglo[self.__tope2] = elemento
        self.__tope2 -= 1
    

    def desapilarPila1(self):
        assert self.__tope1 > 0, "No quedan elementos en la pila 1"
        self.__tope1 -= 1
        elemento = self.__arreglo[self.__tope1]
        return elemento
    

    def desapilarPila2(self):
        assert self.__tope2 < self.__dimension - 1, "No quedan elementos en la pila 2"
        self.__tope2 += 1
        elemento = self.__arreglo[self.__tope2]
        return elemento
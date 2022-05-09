from typing import Callable, Any
from os import system

class Menu:

    __functions: dict[str, tuple[str, Callable, tuple[Any]]] = {
        '0': ('Salir', lambda: None, ())
    }
    __name: str
    __clear: bool

    def __init__(self, name: str = 'Menu', clear: bool = True):

        self.__name = name
        self.__clear = clear

    def registrarOpcion(self, key: str, description: str, value: Callable, *args):

        if key in self.__functions:
            raise Exception('La opcion ya existe')

        self.__functions[key] = (description, value, args)

    def __menu(self):

        print(f'\n===={self.__name}====')
        print('Opciones:')
        for key in self.__functions:
            print(key, '-', self.__functions[key][0])
        print('==========\n')

    def iniciar(self):

        while True:
            self.__menu()
            opcion = input('Ingrese la opcion seleccionada: ')
            if self.__clear: system('cls')
            if opcion == '0': break
            if opcion in self.__functions:
                entry = self.__functions[opcion]
                entry[1](*entry[2])
            else:
                print('Opcion invalida')


def Opcion1():

    print('La opcion 1 fue ejecutada')


def Opcion2():

    print('La opcion 2 fue ejecutada')


if __name__ == "__main__":

    menu = Menu()
    menu.registrarOpcion('1', 'Se ejecutara la opcion 1', Opcion1)
    menu.registrarOpcion('2', 'Se ejecutara la opcion 2', Opcion2)
    menu.registrarOpcion('3', 'Se ejecutara la opcion 3',
        lambda: print('La opcion 3 fue ejecutada')
    )
    menu.iniciar()

from __future__ import annotations
from csv import reader


class ViajeroFrecuente:
    __num_viajero: int
    __dni: str
    __nombre: str
    __apellido: str
    __millas_acum: int

    def __init__(self, numero: int, dni: str, nombre: str, apellido: str, millas: int):
        self.__num_viajero = numero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas

    def cantidadTotaldeMillas(self):
        return self.__millas_acum

    def acumularMillas(self, millas) -> float:
        self.__millas_acum += millas
        return self.__millas_acum

    def canjearMillas(self, millas):
        if self.__millas_acum >= millas:
            self.__millas_acum -= millas
        else:
            print('No posee las suficientes millas acumuladas para el canje')

        return self.__millas_acum

    def obtenerNumero(self) -> int:
        return self.__num_viajero

    def mostrar(self) -> None:
        print(f"{self.__num_viajero}, {self.__dni}, {self.__nombre}, {self.__apellido}, {self.__millas_acum}")

    def __gt__(self, otro: ViajeroFrecuente) -> bool:
        if type(otro) != ViajeroFrecuente:
            raise TypeError("No se puede comparar un viajero frecuente con otro tipo de valor")

        return self.__millas_acum > otro.__millas_acum

    def __add__(self, millas: int) -> ViajeroFrecuente:
        if type(millas) != int:
            raise TypeError("No se pueden acumular las millas de un viajero frecuente con un tipo de dato no entero")

        self.acumularMillas(millas)

        return self

    def __sub__(self, millas: int) -> ViajeroFrecuente:
        if type(millas) != int:
            raise TypeError("No se puede restar un viajero frecuente con un valor no entero")

        return self.__add__(-millas)

    def __eq__(self, otro: ViajeroFrecuente | object | int) -> bool:
        if type(otro) == ViajeroFrecuente:
            return self.__millas_acum == otro.cantidadTotaldeMillas()
        elif type(otro) == int:
            return self.__millas_acum == otro
        else:
            raise TypeError("No se puede comparar un viajero frecuente con un valor que no sea un entero u otro viajero")

    def __req__(self, otro: ViajeroFrecuente | int) -> bool:
        return self == otro

    def __radd__(self, millas: int) -> ViajeroFrecuente:
        return self + millas

    def __rsub__(self, millas: int) -> ViajeroFrecuente:
        return self - millas

    @staticmethod
    def leerArchivo(filePath: str) -> list[ViajeroFrecuente]:
        with open(filePath, "r") as file:
            fileReader = reader(file, delimiter=',')
            next(fileReader, None)

            lista: list[ViajeroFrecuente] = []
            for line in fileReader:
                lista.append(
                    ViajeroFrecuente(
                        int(line[0]),
                        line[1],
                        line[2],
                        line[3],
                        int(line[4])
                    )
                )

            return lista

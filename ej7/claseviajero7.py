from __future__ import annotations
from csv import reader

class Viajero:

	__numViajero: int
	__dni: str
	__nombre: str
	__apellido: str
	__millasAcum: float

	def __init__(self, numViajero: int, dni: str, nombre: str, apellido: str, millasAcum: float):

		self.__numViajero = numViajero
		self.__dni = dni
		self.__nombre = nombre
		self.__apellido = apellido
		self.__millasAcum = millasAcum

	def cantidadTotaldeMillas(self) -> float:

		return self.__millasAcum

	def acumularMillas(self, millas: float) -> float:

		self.__millasAcum += millas
		return self.__millasAcum

	def canjearMillas(self, millas: float) -> float:

		if self.__millasAcum >= millas:
			self.__millasAcum -= millas
		else:
			print("Las millas que ud. tiene no son suficientes")

		return self.__millasAcum

	def obtenerNumero(self) -> int:

		return self.__numViajero

	def mostrar(self) -> None:

		print(f"{self.__numViajero}, {self.__dni}, {self.__nombre}, {self.__apellido}, {self.__millasAcum}")

	def __gt__(self, otro: Viajero) -> bool:

		return self.__millasAcum > otro.__millasAcum

	def __add__(self, millas: float) -> Viajero:

		self.__millasAcum += millas

		return self

	def __sub__(self, millas: float) -> Viajero:

		return self + (-millas)

	def __eq__(self, otro: Viajero | object | int) -> bool:

		if(type(otro) == Viajero):
			return self.__millasAcum == otro.cantidadTotaldeMillas()
		elif(type(otro) == int):
			return self.__millasAcum == otro
		else:
			raise TypeError("No puede compararse un viajero con un valor que no sea entero u otro viajero")

	def __req__(self, otro: Viajero | object | int) -> bool:

		return self == otro

	def __radd__(self, millas: int) -> Viajero:

		return self + millas

	def __rsub__(self, millas: int) -> Viajero:

		return self - millas

    @staticmethod
	def leerArchivo(filePath: str) -> list[Viajero]:

		with open(filePath, "r") as file:
			fileReader = reader(file, delimiter=',')
			next(fileReader, None)

			lista: list[Viajero] = []
			for line in fileReader:
				lista.append(
					Viajero(
						int(line[0]),
						line[1],
						line[2],
						line[3],
						float(line[4])
					)
				)
		return lista

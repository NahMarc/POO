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

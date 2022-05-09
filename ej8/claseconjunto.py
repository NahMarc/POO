from __future__ import annotations

class Conjunto:

	__conjunto: list[int]

	def __init__(self, conjunto: list[int] = []):

		self.__conjunto = conjunto.copy()

	def __add__(self, other: Conjunto) -> Conjunto:

		resultado: list[int] = self.__conjunto.copy()

		for elemento in other.__conjunto:
			if elemento not in resultado:
				resultado.append(elemento)

		return Conjunto(resultado)

	def __sub__(self, other: Conjunto) -> Conjunto:

		resultado: list[int] = []

		for elemento in self.__conjunto:
			if elemento not in other.__conjunto:
				resultado.append(elemento)

		return Conjunto(resultado)

	def __eq__(self, other: Conjunto) -> bool:

		if(type(other) != Conjunto):
			raise TypeError("El objeto no es conjunto")

		if len(self.__conjunto) != len(other.__conjunto):
			return False

		for elemento in self.__conjunto:
			if elemento not in other.__conjunto:
				return False

		return True

	def __str__(self) -> str:

		return '{ ' + str(self.__conjunto)[1:-1] + ' }'

	def __repr__(self) -> str:

		return self.__str__()

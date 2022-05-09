from os import path
from csv import reader
from typing import Literal
from claseregistro import Registro
from clasemenu import Menu

def leerArchivo(path: str) -> list[list[Registro]]:

	lista: list[list[Registro]] = []

	for dia in range(30):
		horas = []

		for hora in range(24):
			horas.append(None)

		lista.append(horas)

	with open(path, "r") as file:
		fileReader = reader(file, delimiter=",")
		next(fileReader, None)

		for line in reader(file, delimiter=','):
			dia = int(line[0]) - 1
			hora = int(line[1]) - 1

			lista[dia][hora] = Registro(float(line[2]), float(line[3]), int(line[4]))

		return lista

def obtenerValores(
	lista: list[list[Registro]],
	variable: Literal["getTemperatura", "getHumedad", "getPresion"]
) -> tuple[int, int, int, int]:
	menor = mayor = getattr(lista[0][0], variable)()
	diaMenor = horaMenor = diaMayor = horaMayor = 0

	for dia in range(30):
		for hora in range(24):
			valor = getattr(lista[dia][hora], variable)()

			if valor < menor:
				menor = valor
				diaMenor = dia
				horaMenor = hora

			if valor > mayor:
				mayor = valor
				diaMayor = dia
				horaMayor = hora

	return (diaMenor + 1, horaMenor + 1, diaMayor + 1, horaMayor + 1)

def inciso1(lista: list[list[Registro]]) -> None:

	temperaturas = obtenerValores(lista, "getTemperatura")
	humedades = obtenerValores(lista, "getHumedad")
	presiones = obtenerValores(lista, "getPresion")

	print(f"Menor temperatura, dia: {temperaturas[0]} hora: {temperaturas[1]}")
	print(f"Mayor temperatura, dia: {temperaturas[2]} hora: {temperaturas[3]}")
	print(f"Menor humedad, dia: {humedades[0]} hora: {humedades[1]}")
	print(f"Mayor humedad, dia: {humedades[2]} hora: {humedades[3]}")
	print(f"Menor presion, dia: {presiones[0]} hora: {presiones[1]}")
	print(f"Mayor presion, dia: {presiones[2]} hora: {presiones[3]}")

def inciso2(lista: list[list[Registro]]) -> None:

	for hora in range(24):
		acum = 0

		for dia in range(30):
			acum +=	lista[dia][hora].getTemperatura()

		print("%2d: %.2f" % (hora + 1, acum / 30))

def inciso3(lista: list[list[Registro]]) -> None:

	dia = int(input("Ingrese el día: "))
	horas = lista[dia]

	for hora in range(24):
		print("%2d: %3.2f - %3.2f - %5d" % (hora + 1, horas[hora].getTemperatura(), horas[hora].getHumedad(), horas[hora].getPresion()))

def test():

	Registro(1, 2, 3)

if __name__ == "__main__":

	test()
	lista = leerArchivo(path.join(path.dirname(__file__) + "/mes.csv"))

	menu = Menu()
	menu.registrarOpcion("1", "Mostrar para cada variable el día y hora de menor y mayor valor.", inciso1, lista)
	menu.registrarOpcion("2", "Indicar la temperatura promedio mensual por cada hora.", inciso2, lista)
	menu.registrarOpcion("3", "Dado un número de día listar los valores de las tres variables para cada hora del día dado.", inciso3, lista)
	menu.iniciar()

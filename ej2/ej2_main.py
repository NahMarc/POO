from os import path
from claseviajero import Viajero

def obtenerViajero(viajeros: list[Viajero]) -> Viajero:

	num = int(input("Ingrese No. del viajero: "))

	for viajero in viajeros:
		if(viajero.obtenerNumero() == num):
			return viajero
	print("No existe viajero asociado a ese numero")
	return obtenerViajero(viajeros)

def test():
	Viajero(1, "0", "Juan", "Lendro", 23)

if __name__ == "__main__":

	test()

	viajeros = Viajero.leerArchivo(path.dirname(__file__) + "/Listaviajeros.csv")
	viajero = obtenerViajero(viajeros)

	print("""
	1 Consultar Millas Acumuladas
	2 Acumular Millas
	3 Canjear Millas Acumuladas
	0 Salir
	""")

	opcion = int(input("Seleccione la opcion que desee: "))
	while opcion != 0:
		print()
		if opcion == 1:
			print(f"La cantidad de millas que acumuló es: {viajero.cantidadTotaldeMillas()}")
		elif opcion == 2:
			millas = int(input("Ingrese la cantidad de millas que va a acumular: "))
			print(f"La cantidad actualizada de millas que acumulo es: {viajero.acumularMillas(millas)}")
		elif opcion == 3:
			millas = int(input("Ingrese las millas que va a canjear: "))
			print(f"La cantidad actualizada de millas que acumulo es: {viajero.canjearMillas(millas)}")
		else:
			print("Opcion no disponible, repita la operacion")

		opcion = int(input("Ingrese la opcion: "))

	print()
	print("¡Gracias por elegirnos!")

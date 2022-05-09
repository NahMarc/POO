from claseviajero6 import Viajero
from os import path

def test():

	Viajero(1, "35000000", "Juan", "Perez", 200)

if __name__ == '__main__':

	test()
	viajeros: list[Viajero] = Viajero.leerArchivo(path.dirname(__file__) + "/Listaviajeros.csv")

	masMillas = max(viajeros).cantidadTotaldeMillas()
	for viajero in viajeros:
		if viajero.cantidadTotaldeMillas() == masMillas:
			viajero.mostrar()

	print('Sobrecargas')

	viajero = viajeros[0]
	viajero.mostrar()
	viajero += 100
	viajero.mostrar()
	viajero -= 100
	viajero.mostrar()

from claseviajero7 import Viajero
from os import path

def test():

	viajero = Viajero(1, "35000000", "Juan", "Perez", 200)

	assert viajero.cantidadTotaldeMillas() == 200
	assert viajero.obtenerNumero() == 1

	assert viajero > Viajero(0, "", "", "", 100)
	assert (viajero + 100).cantidadTotaldeMillas() == 300
	assert (viajero - 50).cantidadTotaldeMillas() == 150

	assert viajero == 300
	assert (100 + viajero).cantidadTotaldeMillas() == 400
	assert (50 - viajero).cantidadTotaldeMillas() == 250
	assert viajero == Viajero(1, "35000000", "Juan", "Perez", 200)



if __name__ == '__main__':

	test()
	viajeros = Viajero.leerArchivo(path.dirname(__file__) + "/Listaviajeros.csv")

	viajero = viajeros[0]

	print(viajero == viajeros[0])
	print(viajero == viajeros[1])
	print(viajero == 100)
	print(viajero == 200)

	viajero = 100 + viajero
	viajero.mostrar()

	viajero = 100 - viajero
	viajero.mostrar()

from ViajeroFrecuente import ViajeroFrecuente
from os import path


def test():
    viajero = ViajeroFrecuente(1, "0", "Alberto", "Leandro", 23)

    assert viajero.cantidadTotaldeMillas() == 23
    assert viajero.obtenerNumero() == 1

    viajero.acumularMillas(7)
    assert viajero.cantidadTotaldeMillas() == 30

    viajero.canjearMillas(10)
    assert viajero.cantidadTotaldeMillas() == 20

    assert viajero > ViajeroFrecuente(0, "", "", "", 15)
    assert (viajero + 100).cantidadTotaldeMillas() == 120
    assert (viajero - 50).cantidadTotaldeMillas() == 70

    assert viajero == 70
    assert (100 + viajero).cantidadTotaldeMillas() == 170
    assert (50 - viajero).cantidadTotaldeMillas() == 120
    assert viajero == ViajeroFrecuente(1, "0", "Juan", "Lendro", 120)


if __name__ == '__main__':
    test()
    viajeros = ViajeroFrecuente.leerArchivo(path.dirname(__file__) + "/viajeros.csv")

    viajero = viajeros[0]

    print(viajero == viajeros[0])
    print(viajero == viajeros[1])
    print(viajero == 100)
    print(viajero == 200)

    viajero = 100 + viajero
    viajero.mostrar()

    viajero = 100 - viajero
    viajero.mostrar()

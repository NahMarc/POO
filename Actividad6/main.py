from ViajeroFrecuente import ViajeroFrecuente
from os import path

def test():
    viajero = ViajeroFrecuente(1, "0", "Juan", "Lendro", 23)

    assert viajero.cantidadTotaldeMillas() == 23
    assert viajero.obtenerNumero() == 1

    viajero.acumularMillas(7)
    assert viajero.cantidadTotaldeMillas() == 30

    viajero.canjearMillas(10)
    assert viajero.cantidadTotaldeMillas() == 20

    assert viajero > ViajeroFrecuente(0, "", "", "", 15)
    assert (viajero + 100).cantidadTotaldeMillas() == 120
    assert (viajero - 50).cantidadTotaldeMillas() == 70


if __name__ == '__main__':
    test()
    viajeros: list[ViajeroFrecuente] = ViajeroFrecuente.leerArchivo(path.dirname(__file__) + "/viajeros.csv")

    masMillas = max(viajeros).cantidadTotaldeMillas()
    for viajero in viajeros:
        if viajero.cantidadTotaldeMillas() == masMillas:
            viajero.mostrar()

    print('\nSobrecargas')

    viajero = viajeros[0]
    viajero.mostrar()
    viajero += 100
    viajero.mostrar()
    viajero -= 100
    viajero.mostrar()


from ViajeroFrecuente import ViajeroFrecuente
from os import path


def obtenerViajero(viajeros: list[ViajeroFrecuente]) -> ViajeroFrecuente:
    num = int(input("Ingrese el numero de viajero: "))

    i = 0
    while i < len(viajeros) and viajeros[i].obtenerNumero() != num:
        i += 1

    if i == len(viajeros):
        raise ValueError("ese viajero no existe")

    return viajeros[i]

def test():
    viajero = ViajeroFrecuente(1, "0", "Juan", "Lendro", 23)

    assert viajero.cantidadTotaldeMillas() == 23
    assert viajero.obtenerNumero() == 1

    viajero.acumularMillas(7)
    assert viajero.cantidadTotaldeMillas() == 30

    viajero.canjearMillas(10)
    assert viajero.cantidadTotaldeMillas() == 20


if __name__ == "__main__":
    test()

    viajeros = ViajeroFrecuente.leerArchivo(path.dirname(__file__) + "/viajeros.csv")
    viajero = obtenerViajero(viajeros)

    print("""
    1- Consultar Cantidad de Millas
    2- Acumular Millas
    3- Canjear Millas
    0- Salir
    """)

    opcion = int(input("Ingrese numero de opcion: "))
    while opcion != 0:
        print()
        if opcion == 1:
            print(f"La cantidad de millas actual es: {viajero.cantidadTotaldeMillas()}")
        elif opcion == 2:
            millas = int(input("Ingrese las millas a acumular: "))
            print(f"La nueva cantidad de millas es: {viajero.acumularMillas(millas)}")
        elif opcion == 3:
            millas = int(input("Ingrese las millas a canjear: "))
            print(f"La nueva cantidad de millas es: {viajero.canjearMillas(millas)}")
        else:
            print("Opcion invalida")

        opcion = int(input("Ingrese numero de opcion: "))

    print()
    print("Fin del programa")

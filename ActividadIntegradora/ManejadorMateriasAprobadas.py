from MateriaAprobada import MateriaAprobada
from csv import reader


class ManejadorMateriasAprobadas:
    __materiasaprobadas: list[MateriaAprobada]

    def __init__(self, ruta: str):
        self.__materiasaprobadas = ManejadorMateriasAprobadas.leerArchivo(ruta)


    @staticmethod
    def leerArchivo(rutaArchivo: str) -> list[MateriaAprobada]:
        with open(rutaArchivo, "r") as csv_file:
            csv_reader = reader(csv_file, delimiter=";")
            next(csv_reader, None)

            return list(map(
                lambda line: MateriaAprobada(
                    int(line[0]),
                    line[1],
                    line[2],
                    float(line[3]),
                    line[4],
                ),
                csv_reader
            ))

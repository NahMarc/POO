import numpy as np
from csv import reader
from Alumno import Alumno
from ManejadorMateriasAprobadas import ManejadorMateriasAprobadas


class ManejadorAlumnos:
    __alumnos: np.ndarray[Alumno, np.dtype[np.object0]]
    __ManejadorMateriasAprobadas: ManejadorMateriasAprobadas
    def __init__(self, alumnosPath: str, materiasaprobadasPath: str):
        self.__alumnos = np.array( # type: ignore
            ManejadorAlumnos.leerArchivo(alumnosPath)
        )
        self.__ManejadorMateriasAprobadas = ManejadorMateriasAprobadas(materiasaprobadasPath)

    def obtenerPromedioAlumno(self, dni: int) -> Alumno | None:
        for alumno in self.__alumnos:
            if alumno.getDni() == dni:
                return alumno

        return None

    @staticmethod
    def leerArchivo(ruta: str) -> list[Alumno]:
        with open(ruta, "r") as csv_file:
            csv_reader = reader(csv_file, delimiter=";")
            next(csv_reader, None)

            return list(map(
                lambda line: Alumno(
                    int(line[0]),
                    line[1],
                    line[2],
                    line[3],
                    int(line[4]),
                ),
                csv_reader
            ))




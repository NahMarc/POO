import numpy as np
from Alumno import Alumno
from MateriaAprobada import MateriaAprobada
from ManejadorAlumnos import ManejadorAlumnos
from ManejadorMateriasAprobadas import ManejadorMateriasAprobadas


def test():
    alumno = Alumno("38075249", "Carrasan", "Nahuel", "LCC", 2)
    assert alumno.getDni() == "38075249"
    assert alumno.getApellido() == "Carrasan"
    assert alumno.getNombre() == "Nahuel"
    assert alumno.getCarrera() == "LCC"
    assert alumno.getAnio() == 2

    materiaaprobada = MateriaAprobada("38075249", "Sistemas Digitales", "07/07/23", 8.0, "P")
    assert materiaaprobada.getDni() == "38075249"
    assert materiaaprobada.getNombreMateria() == "Sistemas Digitales"
    assert materiaaprobada.getFecha() == "07/07/23"
    assert materiaaprobada.getNota() == 8.0
    assert materiaaprobada.getAprobacion() == "P"


def menu():
    #Carga de arreglo numpy
    with open("alumnos.csv", 'r') as file:
        alumnos = []
        next(file)
        for line in file:
            line = line.split(';')
            a = Alumno(line[0], line[1], line[2], line[3], line[4])
            alumnos.append(a)
        np.array(alumnos)

    #Carga lista materiasAprobadas
    materiasaprobadas = []
    ManejadorMateriasAprobadas.cargarDatos(materiasaprobadas)

    print("Menú")
    print("1 - Informar promedio de alumno.")
    print("2 - Ver aprobados como promocionales por materia")
    print("3 - Mostrar lista ordenada")
    print(" - -1 Salir - ")
    option = int(input("Ingrese opcion > "))


    while (option != -1):

        if(option == 1):
            ManejadorAlumnos.promedio(alumnos, materiasaprobadas)

        if(option == 2):
            ManejadorAlumnos.promocionales(alumnos, materiasaprobadas)

        if (option == 3):
            ManejadorAlumnos.ordenar(alumnos)

        option = int(input("Ingrese opcion > "))


if __name__ == "__main__":
    test()
    menu()

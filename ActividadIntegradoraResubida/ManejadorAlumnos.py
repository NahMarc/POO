class ManejadorAlumnos:
    def promedio(alumnos, materiasaprobadas):
        dni = input("Ingrese Dni del alumno > ")
        prom = float(0)
        cant = 0
        for i in range(len(materiasaprobadas)):
            if(materiasaprobadas[i].getDni() == dni):
                prom += materiasaprobadas[i].getNota()
                cant += 1
        if prom == 0:
            print("El alumno no tiene notas registradas o no existe.")
        elif prom != 0:
            print("El promedio para el alumno dni ", dni, " es ", prom/cant)
        return

    def getAlumno(alumnos, dni):
        i = 0
        band = False
        while i < len(alumnos) and band == False:
            if dni == alumnos[i].getDni():
                band = True
            i += 1
        return i

    def promocionales(alumnos, materiasaprobadas):
        mat = input("Ingrese nombre de la materia a buscar: ")
        print("Dni - Apellido y nombre - Fecha - Nota - Año que cursa")
        for i in range(len(materiasaprobadas)):
            if (mat == materiasaprobadas[i].getNombreMateria()) and (materiasaprobadas[i].getNota() >= 7):
                dni = materiasaprobadas[i].getDni()
                id = ManejadorAlumnos.getAlumno(alumnos, dni)
                print(alumnos[id].getDni(), " - ", alumnos[id].getNyA(), " - ", materiasaprobadas[i].getFecha(), " - ", materiasaprobadas[i].getNota(), " - ", alumnos[id].getAnio())


    def ordenar(alumnos):
        alumnos.sort()
        for i in range(len(alumnos)):
            print(alumnos[i].getNyA())

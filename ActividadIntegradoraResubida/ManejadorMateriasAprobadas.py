from MateriaAprobada import MateriaAprobada


class ManejadorMateriasAprobadas:

    def cargarDatos(materiasaprobadas):
        with open("materiasAprobadas.csv", 'r') as filemat:
            next(filemat)
            for line in filemat:
                line = line.split(";")
                m = MateriaAprobada(line[0], line[1], line[2], float(line[3]), line[4])
                materiasaprobadas.append(m)
        return materiasaprobadas

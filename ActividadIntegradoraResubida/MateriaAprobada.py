class MateriaAprobada:
    __dni: ""
    __nombreMateria: ""
    __fecha: ""
    __nota: float()
    __aprobacion: ""

    def __init__(self, dni, nombreMateria, fecha, nota, aprobacion):
        self.__dni = dni
        self.__nombreMateria = nombreMateria
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion

    def getDni(self):
        return self.__dni

    def getNombreMateria(self):
        return self.__nombreMateria

    def getFecha(self):
        return self.__fecha

    def getNota(self):
        return self.__nota

    def getAprobacion(self):
        return self.__aprobacion


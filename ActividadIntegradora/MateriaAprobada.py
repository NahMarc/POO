class MateriaAprobada:
    __dni = int
    __nombremateria = str
    __fecha = str
    __nota = float
    __aprobacion = str

    def __init__(self, dni: str, nombremateria: str, fecha: str, nota: float, aprobacion: str):
        self.__dni = dni
        self.__nombremateria = nombremateria
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion


    def getDni(self):
        return self.__dni

    def getNombreMateria(self):
        return self.__nombremateria

    def getFecha(self):
        return self.__fecha

    def getNota(self):
        return self.__nota

    def getAprobacion(self):
        return self.__aprobacion





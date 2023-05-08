class Alumno:
    __dni = int
    __apellido = str
    __nombre = str
    __carrera = str
    __aniocursado = int

    def __init__(self, dni: int, apellido: str, nombre: str, carrera: str, aniocursado: int):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__aniocursado = aniocursado

    def getDni(self):
        return self.__dni

    def getApellido(self):
        return self.apellido

    def getNombre(self):
        return self.__nombre

    def getCarrera(self):
        return self.__carrera

    def getAnioCursado(self):
        return self.__aniocursado

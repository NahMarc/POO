class Alumno:
    __dni: ""
    __apellido: ""
    __nombre: ""
    __carrera: ""
    __anio: 0

    def __init__(self, dni, apellido, nombre, carrera, anio):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__anio = anio

    def getDni(self) -> int:
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getNyA(self):
        return (self.__apellido, self.__nombre)

    def getCarrera(self) -> str:
        return self.__carrera

    def getAnio(self) -> str:
        return self.__anio

    def __gt__(self, otro):
        return self.getNyA() > otro.getNyA()

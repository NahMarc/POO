class email:
    __idCuenta = str
    __dominio = str
    __tipoDominio = str
    __contrasena = str | None

    def __init__(self, idCuenta: str, dominio: str, tipoDominio: str, contrasena: str | None = None):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contrasena = contrasena

    def __str__(self) -> str:
        return self.retornaEmail()

    def retornaEmail(self):
        return self.__idCuenta + '@' + self.__dominio + '.' + self.__tipoDominio

    def getDominio(self):
        return self.__dominio

    def getIdCuenta(self):
        return self.__idCuenta

    def modificarContrasena(self, contrasenaActual: str, nuevaContrasena: str) -> None:
        if self.__contrasena == contrasenaActual:
            self.__contrasena = nuevaContrasena
            print("La contraseña ha sido modificada")
        else:
            print("La contraseña actual no es correcta")



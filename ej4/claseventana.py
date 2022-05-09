class Ventana:

    __titulo: str
    __x1: int
    __y1: int
    __x2: int
    __y2: int

    def __init__(self, titulo: str, x1: int = 0, y1: int = 0, x2: int = 400, y2: int = 400):

        self.__titulo = titulo
        self.__x1 = x1  # punto superior izquierdo
        self.__y1 = y1
        self.__x2 = x2  # punto inferior derecho
        self.__y2 = y2
        self.__validarPuntos()

    def __validarPuntos(self) -> None:

        if (
                self.__x1 < 0 or self.__y1 < 0 or
                self.__x2 > 500 or self.__y2 > 500 or
                self.__x1 > self.__x2 or self.__y1 > self.__y2
        ):
            raise ValueError('Las coordenadas poseen valores incorrectos')

    def getTitulo(self) -> str:

        return self.__titulo

    def alto(self) -> int:
        alto = self.__y2 - self.__y1
        return alto

    def ancho(self):
        ancho = self.__x2 - self.__x1
        return ancho

    def mostrar(self):

        print(f'Punto1: ({self.__x1}, {self.__y1})')
        print(f'Punto2: ({self.__x2}, {self.__y2})')

    def bajar(self, desplazamiento: int = 1):

        self.__y1 += desplazamiento
        self.__y2 += desplazamiento
        self.__validarPuntos()

    def subir(self, desplazamiento: int = 1):

        self.bajar(-desplazamiento)

    def moverDerecha(self, desplazamiento: int):

        self.__x1 += desplazamiento
        self.__x2 += desplazamiento
        self.__validarPuntos()

    def moverIzquierda(self, desplazamiento: int):

        self.moverDerecha(-desplazamiento)

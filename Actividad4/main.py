from ventana import Ventana

def test():
	Ventana('test')
	Ventana('test', 1)
	Ventana('test', 1, 2)
	Ventana('test', 1, 2, 3)
	Ventana('test', 1, 2, 3, 4)
	ventana = Ventana('test', 100, 200, 300, 300)

	assert ventana.getTitulo() == 'test'
	assert ventana.alto() == 100
	assert ventana.ancho() == 200


if __name__ == '__main__':

    test()

    print('==== Ventana Inicio ====')
    ventanaInicio= Ventana('Inicio')
    ventanaInicio.mostrar()

    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaInicio.getTitulo(),ventanaInicio.alto(),ventanaInicio.ancho()))
    print('==== Ventana Cargar ====')

    ventanaCargar= Ventana('Cargar',10,20)
    ventanaCargar.mostrar()

    print('*** Mueve a la derecha ***')

    ventanaCargar.moverDerecha(10)
    ventanaCargar.mostrar()

    print('*** Mueve a la izquierda ***')

    ventanaCargar.moverIzquierda(10)
    ventanaCargar.mostrar()

    print('*** Bajar ***')

    ventanaCargar.bajar(10)
    ventanaCargar.mostrar()

    print('==== Ventana Borrar ====')

    ventanaBorrar = Ventana('Borrar', 10,20,100,200)
    ventanaBorrar.mostrar()

    print('*** Subir ***')

    ventanaBorrar.subir(5)
    ventanaBorrar.mostrar()

    print('*** Subir ***')

    ventanaBorrar.subir()
    ventanaBorrar.mostrar()

    print('*** Bajar ***')

    ventanaBorrar.bajar()
    ventanaBorrar.mostrar()

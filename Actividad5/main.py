from os import path
from PlanAhorro import PlanAhorro
from Menu import Menu
from csv import reader


def leerArchivo(path: str) -> list[PlanAhorro]:
	with open(path, 'r') as file:
		fileReader = reader(file, delimiter=';')
		next(fileReader, None)

		return list(map(lambda line: PlanAhorro.leerPlan(line), fileReader))

def opcion1(lista: list[PlanAhorro]):
	for plan in lista:
		plan.mostrar()

		valor = float(input('Ingrese el nuevo valor del vehículo: '))
		plan.actualizarValor(valor)

def opcion2(lista: list[PlanAhorro]):
	valor = float(input('Ingrese el valor de la cuota: '))

	for plan in lista:
		if plan.valorCuota() < valor:
			plan.mostrar()

def opcion3(lista: list[PlanAhorro]):
	for plan in lista:
		print(f'El plan {plan.codigo()} tiene un monto de {plan.montoParaLicitar()}')

def opcion4(lista: list[PlanAhorro]):
	codigo = int(input('Ingrese el código del plan: '))
	cuotas = int(input('Ingrese la cantidad de cuotas: '))

	for plan in lista:
		if plan.codigo() == codigo:
			plan.modificarCuotasParaLicitar(cuotas)

def test():
	plan = PlanAhorro(1, 'Ford', 'Fiesta', 20000)

	assert plan.codigo() == 1
	valorCuota = plan.valorCuota()
	assert valorCuota == 22000.0
	assert plan.montoParaLicitar() == 22000.0

if __name__ == '__main__':
	test()
	listaPlanes = leerArchivo(path.dirname(__file__) + '/planes.csv')

	menu = Menu()
	menu.registrarOpcion('a', 'Actualizar el valor del vehículo de cada plan', opcion1, listaPlanes)
	menu.registrarOpcion('b', 'Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado', opcion2, listaPlanes)
	menu.registrarOpcion('c', 'Mostrar el monto que se debe haber pagado para licitar el vehículo (cantidad de cuotas para licitar * importe de la cuota)', opcion3, listaPlanes)
	menu.registrarOpcion('d', 'Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar', opcion4, listaPlanes)
	menu.iniciar()

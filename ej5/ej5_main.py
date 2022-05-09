from os import path
from claseplanahorro import PlanAhorro
from clasemenu5 import Menu
from csv import reader

def leerArchivo(path: str) -> list[PlanAhorro]:
	with open(path, 'r') as file:
		fileReader = reader(file, delimiter=';')
		next(fileReader, None)

		return list(map(lambda line: PlanAhorro.leerPlan(line), fileReader))

def opcionA(lista: list[PlanAhorro]):
	for plan in lista:
		plan.mostrar()

		valor = float(input('Actualice el valor del vehículo: '))
		plan.actualizarValor(valor)

def opcionB(lista: list[PlanAhorro]):

	valor = float(input('Ingrese el valor de la cuota: '))

	for plan in lista:
		if plan.valorCuota() < valor:
			plan.mostrar()

def opcionC(lista: list[PlanAhorro]):

	for plan in lista:
		print(f'El plan {plan.codigo()} tiene un monto de {plan.montoParaLicitar()}')

def opcionD(lista: list[PlanAhorro]):

	codigo = int(input('Ingrese el código del plan: '))
	cuotas = int(input('Ingrese la cantidad de cuotas: '))

	for plan in lista:
		if plan.codigo() == codigo:
			plan.modificarCuotasParaLicitar(cuotas)

def test():
	PlanAhorro(1, 'Ford', 'Ka', 30000)

if __name__ == '__main__':

	test()
	listaPlanes = leerArchivo(path.dirname(__file__) + '/planes.csv')

	menu = Menu()
	menu.registrarOpcion('A', 'Actualizar el valor del vehículo de cada plan', opcionA, listaPlanes)
	menu.registrarOpcion('B', 'Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado', opcionB, listaPlanes)
	menu.registrarOpcion('C', 'Mostrar el monto que se debe haber pagado para licitar el vehículo (cantidad de cuotas para licitar * importe de la cuota)', opcionC, listaPlanes)
	menu.registrarOpcion('D', 'Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar', opcionD, listaPlanes)
	menu.iniciar()

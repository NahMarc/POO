from __future__ import annotations


class PlanAhorro:
	__codigo: int
	__modelo: str
	__version: str
	__valor: float
	__valorCuota: float
	__cuotas: int = 1
	__cuotasParaLicitar: int = 1

	def __init__(self, codigo: int, modelo: str, version: str, valor: float):
		self.__codigo = codigo
		self.__modelo = modelo
		self.__version = version
		self.actualizarValor(valor)

	def valorCuota(self) -> float:
		return self.__valorCuota

	def actualizarValor(self, valor: float):
		self.__valor = valor
		self.__valorCuota = (self.__valor / self.__cuotas) + self.__valor * 0.10

	def codigo(self) -> int:
		return self.__codigo

	def montoParaLicitar(self) -> float:
		return self.__cuotasParaLicitar * self.__valorCuota

	def modificarCuotasParaLicitar(self, cuotas: int):
		self.__cuotasParaLicitar = cuotas

	def mostrar(self):
		print(f'Código: {self.__codigo} Modelo: {self.__modelo} Versión: {self.__version} Valor: {self.__valor} Cantidad de cuotas: {self.__cuotas} Cantidad de cuotas para licitar: {self.__cuotasParaLicitar} Valor cuota: {self.__valorCuota}')

	@staticmethod
	def leerPlan(line: list[str]) -> PlanAhorro:
		cuotas = int(line[4])
		cuotasParaLicitar = int(line[5])

		if cuotas != PlanAhorro.__cuotas:
			PlanAhorro.__cuotas = cuotas
		if cuotasParaLicitar != PlanAhorro.__cuotasParaLicitar:
			PlanAhorro.__cuotasParaLicitar = cuotasParaLicitar

		return PlanAhorro(int(line[0]), line[1], line[2], float(line[3]))

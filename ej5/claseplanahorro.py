class PlanAhorro:

	__codigo: int
	__modelo: str
	__version: str
	__valor: float
	__valorCuota: float
	__cuotasPlan: int = 1
	__cuotasLicitar: int = 1

	def __init__(self, codigo: int, modelo: str, version: str, valor: float):

		self.__codigo = codigo
		self.__modelo = modelo
		self.__version = version
		self.actualizarValor(valor)

	def valorCuota(self) -> float:

		return self.__valorCuota

	def actualizarValor(self, valor):

		self.__valor = valor
		self.__valorCuota = (self.__valor / self.__cuotasPlan) + self.__valor * 0.10

	def codigo(self) -> int:

		return self.__codigo

	def montoParaLicitar(self) -> float:

		return self.__cuotasLicitar * self.__valorCuota

	def modificarCuotasParaLicitar(self, cuotas: int):

		self.__cuotasLicitar = cuotas

	def mostrar(self):

		print(f'Código: {self.__codigo} Modelo: {self.__modelo} Versión: {self.__version} Valor: {self.__valor} Cantidad de cuotas: {self.__cuotasPlan} Cantidad de cuotas para licitar: {self.__cuotasLicitar} Valor cuota: {self.__valorCuota}')

	@staticmethod
	def leerPlan(line: list[str]) -> PlanAhorro:

		cuotasPlan = int(line[4])
		cuotasLicitar = int(line[5])

		if cuotasPlan != PlanAhorro.__cuotasPlan:
			PlanAhorro.__cuotasPlan = cuotasPlan
		if cuotasLicitar != PlanAhorro.__cuotasLicitar:
			PlanAhorro.__cuotasLicitar = cuotasLicitar

		return PlanAhorro(int(line[0]), line[1], line[2], float(line[3]))

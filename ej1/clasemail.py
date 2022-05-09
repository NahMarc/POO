class Email:

	__Id: str
	__Dom: str
	__TipoDom: str
	__Contra: str | None

	def __init__(self, Id: str, Dom: str, TipoDom: str, Contra: str | None = None):

		self.__Id = Id
		self.__Dom = Dom
		self.__TipoDom = TipoDom
		self.__Contra = Contra

	def retornaEmail(self) -> str:

		return self.__Id + "@" + self.__Dom + "." + self.__TipoDom

	def getDominio(self) -> str:

		return self.__Dom

	def getId(self) -> str:

		return self.__Id

	def modificarContraseña(self, ContraActual: str, NuevaContra: str) -> None:

		if self.__Contra == ContraActual:
			self.__Contra = NuevaContra
			print("La contraseña se modificó con éxito")
		else:
			print("Contraseña incorrecta intente otra vez")
	
	def __str__(self) -> str:
        
		return self.retornaEmail()
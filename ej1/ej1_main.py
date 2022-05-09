from clasemail import Email
from os import path
import re
import csv

def EmailfromStr(string: str) -> Email:

	matches = re.search(r"(.+)@(.+)\.(.+)", string)
	if(matches == None):
		raise Exception("Email is not valid")
	return Email(matches.group(1), matches.group(2), matches.group(3))

def LeerArchivo(filePath: str) -> list[Email]:

	with open(filePath, "r") as file:
		reader = csv.reader(file, delimiter=',')
		next(reader, None)
		emails: list[Email] = []

		for line in reader:
			emails.append(EmailfromStr(line[0]))

		return emails

def test():

	email = Email("alumnopoo", "gmail", "com")

	assert email.getDominio() == "gmail"
	assert email.getId() == "alumnopoo"

if __name__ == "__main__":

	test()
	nombre = input("Nombre: ")
	email = Email(
		input("Nombre de usuario: "), 
		input("Dominio: "),
		input("Tipo de dominio (sin punto): "),
		input("Contraseña: ")
	)

	print()
	print("Estimado " + nombre + " te enviaremos tus mensajes a la dirección " + email.retornaEmail())
	print()
	email.modificarContraseña(input("Contraseña vieja: "), input("Contraseña nueva: "))
	print()
	EmailfromStr(input("email: "))
	print()
	emailsDelArchivo = LeerArchivo(path.dirname(__file__) + "/E-mails.csv")
	identificador = input("Ingresar Id de cuenta: ")
	contador = 0

	for email in emailsDelArchivo:
		if email.getId() == identificador:
			contador += 1
	
	if contador == 0:
		print("No existe email con ese Id")
	elif contador == 1:
		print("El Id de ese email es unico")
	else:
		print("El Id está repetido")

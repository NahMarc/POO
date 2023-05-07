from email import email
from os import path
import csv
import re


def crearCuenta(string: str) -> email:
        matches = re.search(r"(.+)@(.+)\.(.+)", string)
        if (matches == None):
            raise Exception("Correo no apto para crear cuenta")

        return email(matches.group(1), matches.group(2), matches.group(3))


def leerArchivo(filePath: str) -> list[email]:
    with open(filePath, "r") as file:
        reader = csv.reader(file, delimiter=',')
        next(reader, None)
        emails: list[email] = []

        for line in reader:
            emails.append(crearCuenta(line[0]))

        return emails


def test():
    Email = email("alumnopoo", "gmail", "com", "123")
    email("alumnopoo", "gmail", "com")

    assert Email.getDominio() == "gmail"


if __name__ == "__main__":
    test()

    nombre = input("Nombre: ")
    Email = email(input("Nombre de usuario: "), input("Dominio: "), input("Tipo de dominio: "), input("Contraseña: "))

    print()
    print("Estimado " + nombre + " te enviaremos tus mensajes a la dirección " + Email.retornaEmail())

    print()
    Email.modificarContrasena(input("Contraseña vieja: "), input("Contraseña nueva: "))
    print()

    crearCuenta(input("email: "))
    print()

    emailsDelArchivo = leerArchivo(path.dirname(__file__) + "/emails.csv")
    identificador = input("Ingresar identificador de cuenta: ")
    contador = 0

    for email in emailsDelArchivo:
        if email.getIdCuenta() == identificador:
            contador += 1

    if contador == 0:
        print("El email con ese identificador no existe")
    elif contador == 1:
        print("El email con ese identificador es unico")
    else:
        print("El email con ese identificador esta repetido")



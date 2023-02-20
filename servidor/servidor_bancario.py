#!/usr/bin/python3

import zmq
import json


def registrar(informacion, socket):

    """
    Metodo que se encarga de registrar nuevos usuarios
    """

    # Contenido del mensaje

    nombre = informacion[1]
    contra = informacion[2]
    primer_ingreso = informacion[3]

    # Abir archivo

    try:
        with open("Datos_Bancarios.json") as file:
            archivo = json.load(file)

            if nombre in archivo.keys():
                socket.send_string("Rechasado")

                print(
                    "Peticion rechasada. El usuario \"{}\""
                    " ya esta registrado".format(nombre))

            else:
                archivo[nombre] = [nombre, contra, primer_ingreso]

                with open("Datos_Bancarios.json", "w") as file:
                    json.dump(archivo, file, indent=4)

                socket.send_string("Anadido a la base de datos")

                print(
                    "El usuario {} ha sido anadido a la base de datos".format(
                        nombre))

    except FileNotFoundError:
        archivo = {}
        archivo[nombre] = [nombre, contra, primer_ingreso]
        with open("Datos_Bancarios.json", "w") as file:
            json.dump(archivo, file, indent=4)

            socket.send_string("Anadido a la base de datos")

            print(
                "El usuario {} ha sido anadido a la base de datos".format(
                    nombre))


def inicio_sesion(informacion, socket):

    """
    Metodo que se encarga buscar si el nombre de usuario y la contrasena
    son validos
    """

    # Contenido del mensaje

    nombre = informacion[1]
    contra = informacion[2]

    # Abir archivo

    try:
        with open("Datos_Bancarios.json") as file:
            archivo = json.load(file)

            if nombre in archivo.keys():

                contra_reg = archivo[nombre][1]

                if contra != contra_reg:
                    socket.send_string("contrasena incorrecta")
                    print(
                        "Usuario \"{}\" encontrado."
                        " Contrasena incorrecta".format(nombre))
                else:
                    socket.send_string("contrasena correcta")
                    print(
                        "Usuario \"{}\" encontrado."
                        " Contrasena correcta".format(nombre))
            else:
                socket.send_string("nombre no registrado")
                print("Usuario \"{}\" no encontrado".format(nombre))

    except FileNotFoundError:
        socket.send_string("nombre no registrado")
        print("Usuario \"{}\" no encontrado".format(nombre))


def agregar_monto(informacion, socket):

    """
    Metodo que se encarga de agregar fondos a la cuenta
    y envia si se tuvo exito o no
    """

    # Contenido del mensaje

    nombre = informacion[1]

    try:
        monto_agregar = int(informacion[2])

        # Abrir archivo Json

        with open("Datos_Bancarios.json") as file:
            archivo = json.load(file)

        registro_usuario = archivo[nombre]

        dinero_anterior = int(registro_usuario[2])

        registro_usuario[2] = str(dinero_anterior + monto_agregar)

        with open("Datos_Bancarios.json", "w") as file:
            json.dump(archivo, file, indent=4)

        socket.send_string("Monto anadido")

        print("Monto anadido")

    except ValueError:
        socket.send_string("ValueError")


def consultar(informacion, socket):

    """
    Metodo que se encarga de consultar cuandos fondos tiene
    la cuenta y enviar esa cantidad
    """

    # Contenido del mensaje

    nombre = informacion[1]

    # Abrir archivo Json

    with open("Datos_Bancarios.json") as file:
        archivo = json.load(file)

    registro_usuario = archivo[nombre]

    fondos = registro_usuario[2]

    # Enviar informacion. Fondos

    socket.send_string(fondos)
    print('Enviado: Fondos registrados')


def sacar(informacion, socket):

    """
    Metodo que se encarga de pretender sacar fondos de la cuenta
    y envia si se tuvo exito o no
    """

    # Contenido del mensaje

    nombre = informacion[1]

    try:
        monto_sacar = int(informacion[2])

        # Abrir archivo Json

        with open("Datos_Bancarios.json") as file:
            archivo = json.load(file)

        registro_usuario = archivo[nombre]

        dinero_anterior = int(registro_usuario[2])

        if dinero_anterior >= monto_sacar:

            registro_usuario[2] = str(dinero_anterior - monto_sacar)

            with open("Datos_Bancarios.json", "w") as file:
                json.dump(archivo, file, indent=4)

            socket.send_string("Monto retirado")

            print("Monto retirado")

        else:

            socket.send_string("mas de lo registrado")

            print("Error: Desea sacar mas dinero de lo que tiene registrado")

    except ValueError:
        socket.send_string("ValueError")


def mensajeria():

    """
    Metodo que se encarga de resivir mensajes y ejecutar segun lo requerido
    """

    # Crear contexto. Conectar socket
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    # Resivir mensajes

    while True:

        mensaje = socket.recv()

        mensaje = mensaje.decode("utf-8")
        informacion = mensaje.split("/")
        opcion = informacion[0]

        if opcion == "Registrar":
            registrar(informacion, socket)
        elif opcion == "inicio sesion":
            inicio_sesion(informacion, socket)
        elif opcion == "Agregar":
            agregar_monto(informacion, socket)
        elif opcion == 'Consultar':
            consultar(informacion, socket)
        elif opcion == "Sacar":
            sacar(informacion, socket)


if __name__ == "__main__":
    mensajeria()

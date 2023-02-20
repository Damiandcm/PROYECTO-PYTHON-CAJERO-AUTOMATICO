#!/usr/bin/python3

import json
import pygame, sys, time
import tkinter as tk
from pygame.locals import *
from tkinter import ttk
from random import randint
from time import sleep
import zmq


class Cajero():
    """
`   Clase cajero, se encarga de producir la interfas y todas sus funciones
    """


    def __init__(self):

        """
        Constructor de cajero. Crea la configuracion fisica del cajero.
        Reproduce sonidos de inicio y bienbenida 
        """

        # Contexto. Conectar socket

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect('tcp://10.0.2.4:5555')

        # Ventana principal

        self.ventana = tk.Tk()
        self.ventana.geometry('589x750+700+30')
        self.ventana.title('Cajero automático')
        self.ventana.resizable(False, False)
        self.ventana.config(
            bg = 'black',
            highlightbackground= 'deepskyblue', highlightthickness = 2
        )

        # Botones arriba

        # Boton 1

        self.boton_up1 = tk.Button(self.ventana, width = 4, height = 2)
        self.boton_up1.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.boton_up1.config(bg = 'deepskyblue', bd = 7)

        # Boton 2

        self.boton_up2 = tk.Button(self.ventana, width = 4, height = 2)
        self.boton_up2.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.boton_up2.config(bg = 'deepskyblue', bd = 7)

        # Boton 3

        self.boton_up3 = tk.Button(self.ventana, width = 4, height = 2)
        self.boton_up3.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.boton_up3.config(bg = 'deepskyblue', bd = 7)

        # Boton 4

        self.boton_up4 = tk.Button(self.ventana, width = 4, height = 2)
        self.boton_up4.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.boton_up4.config(bg = 'deepskyblue', bd = 7)

        # Pantalla del cajero

        self.pantalla = tk.Frame(self.ventana, width = 400, height = 400)
        self.pantalla.grid_propagate(False)
        self.pantalla.config(bg = 'dodgerblue4')
        self.pantalla.grid(row = 0, column = 1, columnspan = 21, rowspan = 4)
        self.pantalla.config(bd = 10)
        self.pantalla.config(relief='ridge')
        self.pantalla.config(cursor="dot")

        # Boton 5

        self.boton_up5 = tk.Button(self.ventana, width = 4, height = 2)
        self.boton_up5.grid(row = 0, column = 22, padx = 10, pady = 10)
        self.boton_up5.config(bg = 'deepskyblue', bd = 7)

        # Boton 6

        self.boton_up6 = tk.Button(self.ventana, width = 4, height = 2)
        self.boton_up6.grid(row = 1, column = 22, padx = 10, pady = 10)
        self.boton_up6.config(bg = 'deepskyblue', bd = 7)

        # Boton 7

        self.boton_up7 = tk.Button(self.ventana, width = 4, height = 2)
        self.boton_up7.grid(row = 2, column = 22, padx = 10, pady = 10)
        self.boton_up7.config(bg = 'deepskyblue', bd = 7)

        # Boton 8

        self.boton_up8 = tk.Button(self.ventana, width = 4, height = 2)
        self.boton_up8.grid(row = 3, column = 22, padx = 10, pady = 10)
        self.boton_up8.config(bg = 'deepskyblue', bd = 7)

        # Botones por debajo

        self.boton_under1 = tk.Button(
            self.ventana, text = '1', width = 4, height = 2)
        self.boton_under1.grid(row = 7, column = 10,  pady = 5)
        self.boton_under1.config(bg='deepskyblue', bd = 5, cursor="spider")

        self.boton_under2 = tk.Button(
            self.ventana, text = '2', width = 4, height = 2)
        self.boton_under2.grid(row = 7, column = 11, pady = 5)
        self.boton_under2.config(bg='deepskyblue', bd = 5, cursor="spider")

        self.boton_under3 = tk.Button(
            self.ventana, text = '3', width = 4, height = 2)
        self.boton_under3.grid(row = 7, column = 12,  pady = 5)
        self.boton_under3.config(bg='deepskyblue', bd = 5, cursor="spider")

        self.boton_under4 = tk.Button(
            self.ventana, text = '4', width = 4, height = 2)
        self.boton_under4.grid(row = 6, column = 10,  pady = 5)
        self.boton_under4.config(bg='deepskyblue', bd = 5, cursor="spider")

        self.boton_under5 = tk.Button(
            self.ventana, text = '5', width = 4, height = 2)
        self.boton_under5.grid(row = 6, column = 11, pady = 5)
        self.boton_under5.config(bg='deepskyblue', bd = 5, cursor="spider")

        self.boton_under6 = tk.Button(
            self.ventana, text = '6', width = 4, height = 2)
        self.boton_under6.grid(row = 6, column = 12, pady = 5)
        self.boton_under6.config(bg='deepskyblue', bd = 5, cursor="spider")

        self.boton_under7 = tk.Button(
            self.ventana, text = '7', width = 4, height = 2)
        self.boton_under7.grid(row=5, column=10, pady=5)
        self.boton_under7.config(bg='deepskyblue', bd = 5, cursor="spider")

        self.boton_under8 = tk.Button(
            self.ventana, text = '8', width = 4, height = 2)
        self.boton_under8.grid(row=5, column=11, pady=5)
        self.boton_under8.config(bg='deepskyblue', bd=5, cursor="spider")

        self.boton_under9 = tk.Button(
            self.ventana, text = '9', width = 4, height = 2)
        self.boton_under9.grid(row = 5, column = 12, pady = 5)
        self.boton_under9.config(bg='deepskyblue', bd = 5, cursor="spider")

        self.boton_under10 = tk.Button(
            self.ventana, text = '❌', width = 4, height = 2)
        self.boton_under10.grid(row = 8, column = 10, pady = 5)
        self.boton_under10.config(bg='deepskyblue', bd = 5, cursor="spider")

        self.boton_under11 = tk.Button(
            self.ventana, text = '0', width = 4, height = 2)
        self.boton_under11.grid(row = 8, column = 11, pady = 5)
        self.boton_under11.config(bg='deepskyblue', bd = 5, cursor="spider")

        self.boton_under12 = tk.Button(
            self.ventana, text = '✅', width = 4, height = 2)
        self.boton_under12.grid(row = 8, column = 12, pady = 5)
        self.boton_under12.config(bg='deepskyblue', bd = 5, cursor="spider")

        # Sonido de inicio

        self.sonidos('Inicio')

        # Sonido bienvenida

        self.sonidos('Bienvenida')


    def sonidos(self, sonido):

        """
        Metodo Para reprodicir sonidos

        :param str sonido: Espesifica el sonido que se quiere reproducir
        """

        # Importar sonidos

        # Inciar pygame.init()

        pygame.init()
        pygame.mixer.init()

        if sonido == 'Inicio':
            # Sonido de inicio al abrir el programa,
            # este se ejecuta al principio y da un sonido
            # de bienvenida:

            intro = pygame.mixer.music.load(
                'y2mate.com - sonido de inicio de windows 7.mp3')
            pygame.mixer.music.play(2) 

            time.sleep(1.2)

        elif sonido == 'Bienvenida':
            # Sonido de de bienvenida, al abrir el programa,
            # este se ejecuta al principio y da un mensaje de
            # bienvenida a los clientes y da indicaciones:

            escena = pygame.mixer.music.load('bienvenida.mp3')
            pygame.mixer.music.play(0)
            pygame.mixer.music.set_volume(0.1)


        elif sonido == 'Espera':

            # Sonido de espera, al abrir el programa,
            # este se ejecuta al principio y funciona
            # como bucle infinito, hasta que el usuario
            # cierre la ventana:

            pygame.mixer.music.load('espera.mp3') 
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.02)


    def inicio(self):

        """
        Metodo que se encarga de mostrar la pagina de principal 'inicio'
        """

        # Texto: Bienvenida

        self.bienvenida = tk.Label(self.pantalla, text = '▶ Bienvenidos ◀')
        self.bienvenida.place(x = 100, y = 180)
        self.bienvenida.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 18), bd = 4, relief='solid')

        # Texto: Registrarse

        self.puntero_registrarse = tk.Label(
            self.pantalla, text = '↤  Registrarse')
        self.puntero_registrarse.place(x = 5, y = 25)
        self.puntero_registrarse.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 14), bd = 4, relief='solid')

        # Texto: Iniciar seción

        self.puntero_iniciar_secion = tk.Label(
            self.pantalla, text = 'Iniciar Sesión  ↦')
        self.puntero_iniciar_secion.place(x = 213, y = 25)
        self.puntero_iniciar_secion.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 14), bd = 4, relief='solid')

        # Texto: Salir

        self.puntero_salir = tk.Label(self.pantalla, text = 'Salir ↦')
        self.puntero_salir.place(x = 302, y = 325)
        self.puntero_salir.config(
            fg = '#003333', bg = 'red',
            font=('Libre-Baskerville', 14), bd = 4, relief='solid')

        # Boton: Para salir

        self.boton_up8.config(command = self.ventana.destroy)

        # Boton: Para registrar un nuevo usuario:

        self.boton_up1.config(command = self.registrar)

        # Boton para iniciar secion

        self.boton_up5.config(command = self.iniciar_sesion)

        # mainloop

        self.fin = self.ventana.mainloop()

    def registrar(self, error_registro=False):

        """
        Metodo que se encarga de destuir la pantalla "Inicio"
        y mostrar la pantalla registrar 
        """

        # Destruir Labels

        self.puntero_iniciar_secion.destroy()
        self.bienvenida.destroy()

        # Destruir punteros

        self.puntero_salir.destroy()
        self.puntero_iniciar_secion.destroy()
        self.puntero_registrarse.destroy()

        # Deshabilitar botones

        self.boton_up1.config(command = self.deshabilitar_boton)
        self.boton_up8.config(command = self.deshabilitar_boton)

        # Nueva página

        # Texto: Registrarse

        self.text_registro = tk.Label(
            self.pantalla, text = '▶ REGISTRARSE ◀') 
        self.text_registro.place(x = 113, y = 60)
        self.text_registro.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 12), bd = 4, relief='solid')

        # Texto: Nombre de usuario

        self.text_usuario = tk.Label(
            self.pantalla, text = 'Nombre de usuario: ')

        self.text_usuario.place(x = 5, y = 100)
        self.text_usuario.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 12), bd = 4, relief='solid')

        # Texto: Fondos iniciales

        self.text_fondos_in = tk.Label(
            self.pantalla, text='Fondos iniciales: ')
        self.text_fondos_in.place(x=5, y=180)
        self.text_fondos_in.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 12), bd = 4, relief='solid')

        # Texto: Nota: Fondos minimos

        self.text_nota_minimo = tk.Label(
            self.pantalla, 
            text='NOTA: Para poder crear una cuenta nescecita'
            ' iniciala\ncon un minimo de 5000 Colones')
        self.text_nota_minimo.place(x=13, y=280)
        self.text_nota_minimo.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 10), bd = 4, relief='solid')

        # Puntero: Continuar

        self.puntero_continuar_reg = tk.Label(
            self.pantalla, text = 'Continuar  ↦')
        self.puntero_continuar_reg.place(x = 263, y = 25)
        self.puntero_continuar_reg.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 12), bd = 4, relief='solid')

        # Entry: Nombre de usuario

        self.usuario = tk.StringVar()
        self.entrada_usuario = tk.Entry(
            self.pantalla, textvariable = self.usuario)
        self.entrada_usuario.place(x = 90, y = 140)
        self.entrada_usuario.config(bg = 'white', font = 60)

        # Puntero: Atras

        self.puntero_atras = tk.Label(self.pantalla, text = '↤  Atras')
        self.puntero_atras.place(x = 5, y = 25)
        self.puntero_atras.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 12), bd = 4, relief='solid')

        # Boton: Continuar. Agregar usuario

        self.boton_up5.config(command = self.agregar_usuario)

        # Boton: Atras

        self.boton_up1.config(
            command = lambda: self.volver_inicio('registrar'))

        # Texto/entrada: Entrada de numeros desde teclado numerico

        self.caja_numeros = tk.Label(self.pantalla, width=20, height=2)
        self.caja_numeros.grid_propagate(False)
        self.caja_numeros.place(x=112, y=220)

        # Habilitar botones under. Teclado numerico

        self.habilitar_numerico('Registro')

    def iniciar_sesion(self):

        """
        Metodo que se encarga de destruir la pantalla inicio y mostrar
        la pantalla inicio sesion
        """

        # Destruir Labels

        self.puntero_iniciar_secion.destroy()
        self.puntero_registrarse.destroy()
        self.bienvenida.destroy()
        self.puntero_salir.destroy()

        # Deshabilitar botones

        self.boton_up5.config(command = self.deshabilitar_boton)
        self.boton_up8.config(command = self.deshabilitar_boton)
        self.boton_up1.config(command=self.deshabilitar_boton)

        # Nueva página

        # Texto: Iniciar sesion

        self.text_iniciar_sesion = tk.Label(self.pantalla, text = 'Iniciar sesión')
        self.text_iniciar_sesion.place(x = 130, y = 80)
        self.text_iniciar_sesion.config(fg = '#003333', bg = 'deepskyblue', font=('Libre-Baskerville', 13), bd = 4, relief='solid')

        # Texto: Nombre de usuario

        self.text_usuario_ini = tk.Label(self.pantalla, text = 'Nombre de usuario: ')
        self.text_usuario_ini.place(x = 5, y = 120)
        self.text_usuario_ini.config(fg = '#003333', bg = 'deepskyblue', font=('Libre-Baskerville', 12), bd = 4, relief='solid')

        # Texto: Contraseña

        self.text_contra_ini = tk.Label(self.pantalla, text = 'Contraseña: ')
        self.text_contra_ini.place(x = 5, y = 200)
        self.text_contra_ini.config(fg = '#003333', bg = 'deepskyblue', font=('Libre-Baskerville', 12), bd = 4, relief='solid')

        # Puntero: Continuar

        self.puntero_continuar_ini = tk.Label(
            self.pantalla, text = 'Continuar  →')
        self.puntero_continuar_ini.place(x = 263, y = 25)
        self.puntero_continuar_ini.config(fg = '#003333', bg = 'deepskyblue', font=('Libre-Baskerville', 12), bd = 4, relief='solid')

        # Entry: Nombre de usuario

        self.usuario_ini = tk.StringVar()
        self.entrada_usuario_ini = tk.Entry(
            self.pantalla, textvariable = self.usuario_ini)
        self.entrada_usuario_ini.place(x = 87, y = 160)
        self.entrada_usuario_ini.config(bg = 'white', font = 60)

        # Texto/Entrada: Contraseña del usuario

        self.contra_ini = tk.Label(self.pantalla, width=20, height=2)
        self.contra_ini.grid_propagate(False)
        self.contra_ini.place(x = 112, y = 240)

        # Puntero: Atras

        self.puntero_atras = tk.Label(self.pantalla, text = '↤  Atras')
        self.puntero_atras.place(x = 5, y = 25)
        self.puntero_atras.config(fg = '#003333', bg = 'deepskyblue', font=('Libre-Baskerville', 12), bd = 4, relief='solid')

        # Boton: Continuar. Continuar con el menú

        self.boton_up5.config(command=self.leer_datos)

        # Boton: Atras

        self.boton_up1.config(
            command = lambda: self.volver_inicio('Inicio_sesion'))

        # Habilitar botones under. Teclado numerico

        self.habilitar_numerico('Inicio')

    
    def leer_datos(self):

        """
        Metodo que se encarga de enviar datos de inicio de sesion al servidor, 
        el cual responde si los datos enviados son validos o no
        """
        
        # Comunicarse con el servidor

        self.socket.send_string('{}/{}/{}'.format('inicio sesion', self.usuario_ini.get(), self.contra_inicio))

        mensaje = self.socket.recv().decode('utf-8')

        self.acceso(mensaje)
        

    def acceso(self, tipo_acceso):

        """
        Metodo que se encarga de destruir la pantalla 'inicio sesion'
        y muestra la pantalla 'menu' o una pantalla de error 
        """

        # Acceso al banco

        # Deshabilitar Labels

        self.text_iniciar_sesion.destroy()
        self.text_usuario_ini.destroy()
        self.text_contra_ini.destroy()

        # Destruir Texto/entrada

        self.contra_ini.destroy()

        # Destruir punteros

        self.puntero_continuar_ini.destroy()
        self.puntero_atras.destroy()

        # Destruir Entrys

        self.entrada_usuario_ini.destroy()

        # Deshabilitar boton

        self.boton_up1.config(command=self.deshabilitar_boton)
        self.boton_up5.config(command=self.deshabilitar_boton)

        # Deshabilitar teclado numerico

        self.deshabilitar_numerico()

        # Nueva página
        
        if tipo_acceso == 'contrasena correcta':

            # Ir al menu

            self.menu()            

        elif tipo_acceso == 'contrasena incorrecta':

            # Actualizar puntero atras

            self.puntero_atras = tk.Label(self.pantalla, text = '↤  Atras')
            self.puntero_atras.place(x=5, y=228)
            self.puntero_atras.config(
                fg = '#003333', bg = 'deepskyblue',
                font=('Libre-Baskerville', 14), bd = 4, relief='solid')

            # Actualizar boton atras

            self.boton_up3.config(
                command=lambda: self.volver_inicio_sesion('contrasena incorrecta'))
            
            # Texto: Error, contrasena incorrecta

            self.contra_incorrecta = tk.Label(
                self.pantalla, text='Error.\nContrasena incorrecta') 
            self.contra_incorrecta.place(x=65, y=55)
            self.contra_incorrecta.config(
                fg = '#003333', bg = 'deepskyblue',
                font=('Libre-Baskerville', 16), bd = 4, relief='solid')

        elif tipo_acceso == 'nombre no registrado':

            # Actualizar puntero atras

            self.puntero_atras = tk.Label(self.pantalla, text = '↤  Atras')
            self.puntero_atras.place(x=5, y=228)
            self.puntero_atras.config(
                fg = '#003333', bg = 'deepskyblue',
                font=('Libre-Baskerville', 14), bd = 4, relief='solid')

            # Actualizar boton atras

            self.boton_up3.config(
                command=lambda: self.volver_inicio_sesion('nombre no registrado'))

            # Texto: Error, nombre incorrecto. NO registrado

            self.nombre_incorrecto = tk.Label(
                self.pantalla, text='Error.\nNombre de usuario no registrado') 
            self.nombre_incorrecto.place(x=6, y=55)
            self.nombre_incorrecto.config(
                fg = '#003333', bg = 'deepskyblue',
                font=('Libre-Baskerville', 16), bd = 4, relief='solid')


    def volver_inicio_sesion(self, tipo_devolucion):

        """
        Metodo que se encarga de borrar distintas pantallas con 
        el objetivo de volver a la pantalla 'inicio sesion' 
        """

        # Volver a inicio de sesion

        # Destruir puntero atras

        self.puntero_atras.destroy()

        # Deshebilitar botones 

        self.boton_up3.config(command=self.deshabilitar_boton)

        if tipo_devolucion == 'contrasena correcta':

            # Ir a inicio

            self.destruir_menu()
            self.inicio()

        elif tipo_devolucion == 'contrasena incorrecta':

            # Destruir Labels

            self.contra_incorrecta.destroy()

            # volver a menu

            self.iniciar_sesion() 

        elif tipo_devolucion == 'nombre no registrado':

            # Destruir Labels

            self.nombre_incorrecto.destroy()

            # volver a menu

            self.iniciar_sesion() 


    def menu(self):

        """
        Metodo que se encarga de mostrar la pantalla menu
        Esta da las siguienbtes obciones: sacar fondos, 
        consultar fondos y depositar fondos
        """

        # Actualisar boton atras

        self.boton_up3.config(
            command=lambda: self.volver_inicio_sesion('contrasena correcta'))
        
        # Texto: Menu

        self.text_menu = tk.Label(self.pantalla, text='Menu') 
        self.text_menu.place(x=159, y=15)
        self.text_menu.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 14), bd = 4, relief='solid')

        # Puntero: Ingrasar dinero a la cuenta

        self.puntero_agregar = tk.Label(
            self.pantalla, text='Hacer deposito  ↦')
        self.puntero_agregar.place(x=199, y=125)
        self.puntero_agregar.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 14), bd = 4, relief='solid')

        # Puntero: Consultar fondos

        self.cons_fondos = tk.Label(
            self.pantalla, text='Consultar fondos  ↦')
        self.cons_fondos.place(x=180, y=222)
        self.cons_fondos.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 14), bd = 4, relief='solid')

        # Puntero: Sacar efectivo

        self.sac_efectiuvo = tk.Label(
            self.pantalla, text='Sacar efectivo  ↦')
        self.sac_efectiuvo.place(x=206, y=327)
        self.sac_efectiuvo.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 14), bd = 4, relief='solid')

        # Puntero: Salir

        self.puntero_salir = tk.Label(self.pantalla, text='↤  Salir')
        self.puntero_salir.place(x=5, y=323)
        self.puntero_salir.config(
            fg = '#003333', bg = 'red',
            font=('Libre-Baskerville', 14), bd = 4, relief='solid')

        # Puntero: Atras

        self.puntero_atras = tk.Label(
            self.pantalla, text = '↤  Atras')
        self.puntero_atras.place(x=5, y=228)
        self.puntero_atras.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 14), bd = 4, relief='solid')

        # Habilitar botones

        self.boton_up6.config(command=self.depositar)
        self.boton_up7.config(command=self.consultar)
        self.boton_up8.config(command=self.sacar_fondos)
        self.boton_up4.config(command=self.ventana.destroy)
 
    def sacar_fondos(self):

        """
        Metodo que se encarga de mostar la pantalla 'sacar fondos'.
        Esta pregunta cuantos fondos se pretenden sacar 
        """

        # Destruir pantalla menu

        self.destruir_menu()

        # Nueva pantalla

        # Puntero: Continuar. Sacar monto

        self.puntero_continuar_sac = tk.Label(
            self.pantalla, text='Continuar  ↦')
        self.puntero_continuar_sac.place(x=245, y=323)
        self.puntero_continuar_sac.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 14), bd = 4, relief='solid')

        # Puntero: Atras

        self.puntero_atras = tk.Label(
            self.pantalla, text='↤  Atras')
        self.puntero_atras.place(x=5, y=323)
        self.puntero_atras.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 14), bd = 4, relief='solid')

        # Boton: Atras

        self.boton_up4.config(command=lambda: self.volver_menu('sacar'))

        # Texto. Cuanto desea retirar?

        self.text_fondos_retirar = tk.Label(
            self.pantalla, text='Cuanto dinero desea retirar?')
        self.text_fondos_retirar.place(x=55, y=100)
        self.text_fondos_retirar.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 14), bd = 4, relief='solid')

        # Texto/entrada: Monto por ingresar desde el teclado numerico

        self.caja_monto_sac = tk.Label(self.pantalla, width=20, height=2)
        self.caja_monto_sac.grid_propagate(False)
        self.caja_monto_sac.place(x=110, y=190)


        # Boton: Continuar. Retirar Fondos

        self.boton_up8.config(command=self.monto_retirado)

        # Habilitar teclado numerico

        self.habilitar_numerico('sacar')


    def volver_menu(self, pantalla):

        """
        Metodo que se encarga de destruir distintas pantallas
        con el objetivo de volver al la pantalla 'menu'
        """

        if pantalla == 'querer_depositar':

            # Destruir Labels

            self.text_monto_agregar.destroy()

            # Destruir punteros
            
            self.puntero_atras.destroy()
            self.puntero_continuar_agr.destroy()

            # Destruir Texto/entrada
        
            self.caja_monto_ing.destroy()

            # Deshabilitar teclado numerico

            self.deshabilitar_numerico()

            # Deshabilitar boton atras  

            self.boton_up4.config(command=self.deshabilitar_boton)

            # Deshabilitar boton continuar

            self.boton_up8.config(command=self.deshabilitar_boton)

        elif pantalla == 'monto_agregado':

            # Destruir Labels

            self.text_agregado.destroy()

            # Destruir punteros
            
            self.puntero_atras.destroy()

            # Deshabilitar boton atras  

            self.boton_up4.config(command=self.deshabilitar_boton)

        elif pantalla == 'consultar':

            # Destuir Labels 

            self.Fondos_registrados.destroy()

            # Deshabilitar botones
            
            self.boton_up4.config(command=self.deshabilitar_boton)

            # Destruir punteros 

            self.puntero_atras.destroy()

        
        elif pantalla == 'sacar':

            # Deshabilitar teclado numerico

            self.deshabilitar_numerico()

            # Destruir Labels 

            self.text_fondos_retirar.destroy()

            # Destruir punteros

            self.puntero_continuar_sac.destroy()
            self.puntero_atras.destroy()

            # Destruir Texto/entrada

            self.caja_monto_sac.destroy()
            
            # Deshabilitar botones

            self.boton_up4.config(command=self.deshabilitar_boton)
            self.boton_up8.config(command=self.deshabilitar_boton)

        elif pantalla == 'retiro invalido. Mucho':
            
            # Destruir Labels 

            self.text_no_agregado.destroy()

            # Deshabilitar punterro atras

            self.puntero_atras.destroy()

            # Deshabilitar  

            self.boton_up4.config(command=self.deshabilitar_boton)


        elif pantalla == 'fondos retirados':

            # Destruir Labels 

            self.text_agregado.destroy()

            # Deshabilitar punterro atras

            self.puntero_atras.destroy()

            # Deshabilitar botones

            self.boton_up4.config(command=self.deshabilitar_boton)

        self.menu()


    def consultar(self):

        """
        Metodo que se encarga de mostrar una 
        pantalla con la informacion del dinero
        remanente en la cuenta.
        """

        # Destruir pantalla menu

        self.destruir_menu()

        # Nueva pantalla

        # Puntero: Atras

        self.puntero_atras = tk.Label(self.pantalla, text='↤  Atras')
        self.puntero_atras.place(x=5, y=323)
        self.puntero_atras.config(fg = '#003333', bg = 'deepskyblue', font=('Libre-Baskerville', 14), bd = 4, relief='solid')

        # Boton: Atras

        self.boton_up4.config(command=lambda: self.volver_menu('consultar'))

        # Consultar fondos al servidor

        self.socket.send_string('{}/{}'.format('Consultar', self.usuario_ini.get()))
        mensaje = self.socket.recv().decode("utf-8")

        # Texto. Fondos

        self.Fondos_registrados = tk.Label(
            self.pantalla,
            text='Sus fondos registrados son:\n{} Colones'.format(mensaje))
        self.Fondos_registrados.place(x=60, y=120)
        self.Fondos_registrados.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 14), bd = 4, relief='solid')
    

    def depositar(self):

        """
        Metodo que se encarga de mostrar la pantalla 'depositar'
        la cual pregunta la cantidad de dinero que se decea depositar
        """

        # Destruir pantalla menu

        self.destruir_menu()

        # Nueva pantalla

        # Texto: Ingrese el monto que desea agregar
        
        self.text_monto_agregar = tk.Label(
            self.pantalla, text='Ingrese el monto que\ndesea agregar')
        self.text_monto_agregar.place(x=86, y=120)
        self.text_monto_agregar.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 14), bd = 4, relief='solid')

        # Puntero: Continuar. Agregar monto

        self.puntero_continuar_agr = tk.Label(
            self.pantalla, text='Continuar  ↦')
        self.puntero_continuar_agr.place(x=245, y=323)
        self.puntero_continuar_agr.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 14), bd = 4, relief='solid')

        # Puntero: Atras
        self.puntero_atras = tk.Label(self.pantalla, text='↤  Atras')
        self.puntero_atras.place(x=5, y=323)
        self.puntero_atras.config(
            fg = '#003333', bg = 'deepskyblue',
            font=('Libre-Baskerville', 14), bd = 4, relief='solid')
        
        # Texto/entrada: Monto por ingresar desde el teclado numerico

        self.caja_monto_ing = tk.Label(
            self.pantalla, width=20, height=2)
        self.caja_monto_ing.grid_propagate(False)
        self.caja_monto_ing.place(x=110, y=190)
        
        # Boton: Continuar. Agegar monto

        self.boton_up8.config(command=self.monto_agregado)

        # Boton: Atras

        self.boton_up4.config(
            command=lambda: self.volver_menu('querer_depositar'))

        # Habilitar teclado numerico

        self.habilitar_numerico('Depositar')


    def monto_retirado(self):

        """
        Metodo que se encarga de pretender sacar efectivo 
        del bonco y de mostrar una pantalla de exito
        o error, al pretender hacer un retiro de efectivo
        """

        # Enviar monto al servidor


        self.socket.send_string(
            '{}/{}/{}'.format(
                'Sacar', self.usuario_ini.get(), self.sacar_monto))
        
        # Respuesta del servidor

        mensaje = self.socket.recv().decode("utf-8")

        if mensaje == 'Monto retirado':


            # Deshabilitar teclado numerico 

            self.deshabilitar_numerico()

            # Destruir Labels


            self.text_fondos_retirar.destroy()

            # Destruir Texto/entrada

            self.caja_monto_sac.destroy()

            # Destruir punteros
            
            self.puntero_continuar_sac.destroy()

            # Deshabilitar botones

            self.boton_up8.config(command=self.deshabilitar_boton)

            # Nueva pagina 

            # Actualizar boton atras

            self.boton_up4.config(
                command=lambda: self.volver_menu('fondos retirados'))

            # Texto: Monto retirado exitosamente

            self.text_agregado = tk.Label(
                self.pantalla, text='Monto retirado exitosamente')
            self.text_agregado.place(x=44, y=140)
            self.text_agregado.config(
                fg = '#003333', bg = 'deepskyblue',
                font=('Libre-Baskerville', 15), bd = 4, relief='solid')


        elif mensaje == 'mas de lo registrado':
            
            # Deshabilitar teclado numerico 

            self.deshabilitar_numerico()

            # Destruir Labels


            self.text_fondos_retirar.destroy()

            # Destruir Texto/entrada

            self.caja_monto_sac.destroy()

            # Destruir punteros

            self.puntero_continuar_sac.destroy()

            # Deshabilitar botones

            self.boton_up8.config(command=self.deshabilitar_boton)

            # Nueva pagina 

            # Actualizar boton atras

            self.boton_up4.config(
                command=lambda: self.volver_menu('retiro invalido. Mucho'))

            # Texto: Monto retirado exitosamente

            self.text_no_agregado = tk.Label(
                self.pantalla, text='Error:\nMonto mayor a los fondos totales')
            self.text_no_agregado.place(x=19, y=140)
            self.text_no_agregado.config(
                fg = '#003333', bg = 'deepskyblue',
                font=('Libre-Baskerville', 15), bd = 4, relief='solid')

        elif mensaje == 'ValueError':
            pass


    def monto_agregado(self):

        """
        Metodo que se encarga de agregar fondos a la cuenta
        y mostrar una pantalla con un mensaje de exito
        """

        # Enviar monto al servidor

        self.socket.send_string('{}/{}/{}'.format('Agregar', self.usuario_ini.get(), self.agregar_monto))
        mensaje = self.socket.recv().decode("utf-8")

        if mensaje == 'Monto anadido':

            # Deshabilitar teclado numerico 

            self.deshabilitar_numerico()

            # Destruir Labels

            self.text_monto_agregar.destroy()

            # Destruir Texto/entrada

            self.caja_monto_ing.destroy()

            # Destruir punteros
            
            self.puntero_continuar_agr.destroy()

            # Deshabilitar botones

            self.boton_up8.config(command=self.deshabilitar_boton)

            # Nueva pagina 

            # Actualizar boton atras

            self.boton_up4.config(command=lambda: self.volver_menu('monto_agregado'))

            # Texto: Monto agregado exitosamente

            self.text_agregado = tk.Label(self.pantalla, text='Monto agregado exitosamente')
            self.text_agregado.place(x=32, y=140)
            self.text_agregado.config(fg = '#003333', bg = 'deepskyblue', font=('Libre-Baskerville', 15), bd = 4, relief='solid')

        elif mensaje == 'ValueError':
            pass

    def destruir_menu(self):

        """
        Metodo que se encarga de destruir la pantalla 'menu'.
        """

        # Destruir Labels

        self.text_menu.destroy()

        # Destruir punteros

        self.puntero_agregar.destroy()
        self.cons_fondos.destroy()
        self.sac_efectiuvo.destroy()
        self.puntero_salir.destroy()
        self.puntero_atras.destroy()

        # Deshebilitar botones

        self.boton_up6.config(command=self.deshabilitar_boton)
        self.boton_up7.config(command=self.deshabilitar_boton)
        self.boton_up8.config(command=self.deshabilitar_boton)
        self.boton_up4.config(command=self.deshabilitar_boton)
        self.boton_up3.config(command=self.deshabilitar_boton)


    def habilitar_numerico(self, opcion):

        """
        Metodo que se encarga de habilitar el teclado numero
        y de nombrar distintos string que guardaran la informacion 
        digitada en el teclado numerico
        """

        # Habilitar teclado numerico

        self.sacar_monto = ''

        self.agregar_monto = ''
            
        self.contra_inicio = ''

        self.saldo_inicial = ''

        self.boton_under1.config(command=lambda: self.tec_num('1', opcion))
        self.boton_under2.config(command=lambda: self.tec_num('2', opcion))
        self.boton_under3.config(command=lambda: self.tec_num('3', opcion))
        self.boton_under4.config(command=lambda: self.tec_num('4', opcion))
        self.boton_under5.config(command=lambda: self.tec_num('5', opcion))
        self.boton_under6.config(command=lambda: self.tec_num('6', opcion))
        self.boton_under7.config(command=lambda: self.tec_num('7', opcion))
        self.boton_under8.config(command=lambda: self.tec_num('8', opcion))
        self.boton_under9.config(command=lambda: self.tec_num('9', opcion))
        self.boton_under10.config(command=lambda: self.tec_num('', opcion, True))
        self.boton_under11.config(command=lambda: self.tec_num('0', opcion))

        
    def tec_num(self, numero, objetivo, borrar=False):

        """
        Metodo que se encarga de eligir a cual string 
        se anade la informacion digitada en el teclado 
        numerico o borrarla
        """

        # Escribir en pantalla lo seleccionado en el tecclado numerico

        if borrar:
                self.saldo_inicial = ''
                self.contra_inicio = ''
                self.agregar_monto = ''
                self.sacar_monto = ''


        if objetivo == 'Registro':
            self.saldo_inicial += numero

            self.boton_under12.config(command=self.agregar_usuario)
            self.caja_numeros.config(text=self.saldo_inicial)
            
            

        elif objetivo == 'Inicio':
            self.contra_inicio += numero

            self.boton_under12.config(command=self.leer_datos)
            self.contra_ini.config(text=self.contra_inicio)

        elif objetivo == 'Depositar':
            self.agregar_monto += numero

            self.boton_under12.config(command=self.monto_agregado)
            self.caja_monto_ing.config(text=self.agregar_monto)

        elif objetivo == 'sacar':
            self.sacar_monto += numero

            self.boton_under12.config(command=self.monto_retirado)
            self.caja_monto_sac.config(text=self.sacar_monto)


    def volver_inicio(self, pantalla):

        """
        Metodo que se encarga de destruir distintas
        pantallas con el fin de volver a la pantalla 'inicio'
        """

        if pantalla == 'agregar_usuario':

            # Destruir labels

            self.text_registro_exitoso.destroy()
            self.text_nuevo_usuario.destroy()
            self.text_contra.destroy()
            self.puntero_atras.destroy()


            # Desabilitar botones

            self.boton_up1.config(command = self.deshabilitar_boton)
            self.boton_up5.config(command = self.deshabilitar_boton)

        elif pantalla == 'registrar':

            # Destruir labels

            self.puntero_atras.destroy()
            self.puntero_continuar_reg.destroy()
            self.text_usuario.destroy()
            self.text_registro.destroy()
            self.text_fondos_in.destroy()
            self.caja_numeros.destroy()
            self.text_nota_minimo.destroy()

            # Destruir entrys

            self.entrada_usuario.destroy()

            # Deshabilitar botones

            self.boton_up1.config(command = self.deshabilitar_boton)
            self.boton_up5.config(command = self.deshabilitar_boton)
            self.deshabilitar_numerico()

        elif pantalla == 'agregar_usuario. Error':

            # Destruir labels

            self.puntero_atras.destroy()
            self.invalido.destroy()

            # Desabilitar botones

            self.boton_up1.config(command = self.deshabilitar_boton)
            self.boton_up5.config(command = self.deshabilitar_boton)

        elif pantalla == 'Inicio_sesion':

            # Destruir Labels

            self.text_iniciar_sesion.destroy()
            self.text_usuario_ini.destroy()
            self.text_contra_ini.destroy()
            
            # Destruir punteros 

            self.puntero_continuar_ini.destroy()
            self.puntero_atras.destroy()

            # Destruir Entrys

            self.entrada_usuario_ini.destroy()

            # Deshabilitar botones 

            self.boton_up1.config(command=self.deshabilitar_boton)
            self.boton_up5.config(command=self.deshabilitar_boton)

            # Destruir text/entrada

            self.contra_ini.destroy()

            # Deshabilitar botones under. Teclado numerico

            self.deshabilitar_numerico()

        # volver a inicio

        self.inicio()

    def deshabilitar_numerico(self):

        """
        Metodo que se encarga de destruir el teclado numerico
        """

        # Deshabilitar teclado numerico

        self.boton_under1.config(command=self.deshabilitar_boton)
        self.boton_under2.config(command=self.deshabilitar_boton)
        self.boton_under3.config(command=self.deshabilitar_boton)
        self.boton_under4.config(command=self.deshabilitar_boton)
        self.boton_under5.config(command=self.deshabilitar_boton)
        self.boton_under6.config(command=self.deshabilitar_boton)
        self.boton_under7.config(command=self.deshabilitar_boton)
        self.boton_under8.config(command=self.deshabilitar_boton)
        self.boton_under9.config(command=self.deshabilitar_boton)
        self.boton_under10.config(command=self.deshabilitar_boton)
        self.boton_under11.config(command=self.deshabilitar_boton)
        self.boton_under12.config(command=self.deshabilitar_boton)


    def agregar_usuario(self):

        """
        Metodo que se encarga de destruir la pantalla 'registrar'
        e intenta agregar un usuario
        """

        # Deshabilitar botones

        self.boton_up5.config(command = self.deshabilitar_boton)
        self.deshabilitar_numerico()

        # Actualizar boton Atras

        self.boton_up1.config(
            command = lambda: self.volver_inicio('agregar_usuario'))

        # Destruir labels

        self.text_registro.destroy()
        self.text_usuario.destroy()
        self.puntero_continuar_reg.destroy()
        self.text_fondos_in.destroy()
        self.caja_numeros.destroy()
        self.text_nota_minimo.destroy()

        # Destruir Entry

        self.entrada_usuario.destroy()

        # Optener Nombre de usuario:

        try:
            saldo_inicial = int(self.saldo_inicial)
            if ' ' not in self.usuario.get() and self.usuario.get() != '' and saldo_inicial >= 5000:

                # self.socket.send_string('Registrar/' + self.usuario.get())
                # self.mensaje = self.socket.recv().decode('utf-8')

                # Conteseña

                contra = str(randint(1000, 9999))

                
                # Guardar datos en el servidor 

                self.socket.send_string(
                    '{}/{}/{}/{}'.format('Registrar', self.usuario.get(), contra, self.saldo_inicial))
                mensaje = self.socket.recv().decode("utf-8")
                
                # Error, Nombre de usuario ya rejgstrado
                
                if mensaje == 'Rechasado':

                    # Labels

                    # Texto: Nombre invalido

                    self.invalido = tk.Label(
                        self.pantalla,
                        text='Nombre de usuario invalido.\nEse nombre ya ha sido registrado') 
                    self.invalido.place(x=3, y=130)
                    self.invalido.config(
                        fg = '#003333', bg = 'deepskyblue',
                        font=('Libre-Baskerville', 16), bd = 4, relief='solid')

                    # Actualizar boton Atras

                    self.boton_up1.config(
                    command = lambda: self.volver_inicio('agregar_usuario. Error'))

                else:
                    # Labels

                    # Texto: Registro exitoso

                    self.text_registro_exitoso = tk.Label(
                        self.pantalla,
                        text = 'Registro Exitoso\nDebe recordar los siguientes '
                        'datos\npara poder iniciar seción')
                    self.text_registro_exitoso.place(x = 30, y = 100)
                    self.text_registro_exitoso.config(
                        fg = '#003333', bg = 'deepskyblue',
                        font=('Libre-Baskerville', 13), bd = 4, relief='solid')

                    # Texto: Nombre de usuario

                    self.text_nuevo_usuario = tk.Label(
                        self.pantalla, text = 'Nombre de usuario: {}'.format(
                            self.usuario.get()))
                    self.text_nuevo_usuario.place(x=30, y=200)
                    self.text_nuevo_usuario.config(
                        fg = '#003333', bg='deepskyblue',
                        font=('Libre-Baskerville', 13), bd=4, relief='solid')

                    # Texto contraseña

                    self.text_contra = tk.Label(
                        self.pantalla, text = 'Contraseña: {}'.format(contra))
                    self.text_contra.place(x = 30, y = 250)
                    self.text_contra.config(
                        fg = '#003333', bg = 'deepskyblue',
                        font=('Libre-Baskerville', 13), bd=4, relief='solid')

            else:
                self.registrar()
        except ValueError:
            self.registrar()

    def deshabilitar_boton(self):

        """
        Metodo que se encarga de deshabilitar botones
        que tienen alguna funcion, para evitar errores
        """

        pass


def registro():

    # Construir cajero

    cajero = Cajero()
    cajero.inicio()


if __name__ == '__main__':
    registro()

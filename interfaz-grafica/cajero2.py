#!/usr/bin/python3

import json
import pygame
import tkinter as tk
from tkinter import ttk
from random import randint
import time
import zmq


class Cajero():

    def __init__(self):

        # Importar sonidos

        # Inciar pygame.init()
        pygame.mixer.init()

        self.intro = pygame.mixer.Sound ("intro.mp3")
        pygame.mixer.Sound.play(self.intro) 
        """Sonido de inicio al abrir el programa,
        este se ejecuta al principio y da un sonido
        de bienvenida"""

        pygame.mixer.music.load ("espera.mp3") 
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        """Sonido de espera, al abrir el programa,
        este se ejecuta al principio y funciona
        como bucle infinito, hasta que el usuario
        cierre la ventana"""

        self.boton = pygame.mixer.Sound ("boton.mp3")
        pygame.mixer.Sound.play(self.boton)
        """Sonido perteneciente a los botones
        funciona solamente cuando el usuario ejecuta
        una determinada función"""

        time.sleep(3)
        self.escena = pygame.mixer.Sound ("bienvenida.mp3")
        pygame.mixer.Sound.play(self.escena) 
        """Sonido de de bienvenida, al abrir el programa,
        este se ejecuta al principio y da un mensaje de 
        bienvenida a los clientes y da indicaciones"""


        # Contexto. Conectar socket

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://10.0.2.4:5555")

        # Ventana principal

        self.ventana = tk.Tk()
        self.ventana.geometry('589x750+700+30')
        self.ventana.title('Cajero automático')
        self.ventana.resizable(False, False)
        self.ventana.config(
            bg = 'black',
            highlightbackground= "deepskyblue", highlightthickness = 2
        )

        # Botones arriba

        # Boton 1

        self.boton_up1 = tk.Button(self.ventana, width = 4, height = 2)
        self.boton_up1.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.boton_up1.config(bg = 'deepskyblue', bd = 7)

        #self.boton.play() #  de sonido

        # Boton 2

        self.boton_up2 = tk.Button(self.ventana, width = 4, height = 2)
        self.boton_up2.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.boton_up2.config(bg = 'deepskyblue', bd = 7)

        #pygame.mixer.Sound.play(self.boton) #  de sonido


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


    def inicio(self):

        # Texto: Bienvenida

        self.bienvenida = tk.Label(self.pantalla, text = '▶ Bienvenidos ◀')
        self.bienvenida.place(x = 118, y = 180)
        self.bienvenida.config(fg = '#003333', bg = 'deepskyblue', font=('Libre-Baskerville', 12), bd = 4, relief='solid')



        # Texto: Registrarse

        self.puntero_registrarse = tk.Label(
            self.pantalla, text = '↤  Registrarse')
        self.puntero_registrarse.place(x = 5, y = 25)
        self.puntero_registrarse.config(fg = '#003333', bg = 'deepskyblue', font=('Libre-Baskerville', 12), bd = 4, relief='solid')


        # Texto: Iniciar seción

        self.puntero_iniciar_secion = tk.Label(
            self.pantalla, text = 'Iniciar Sesión  ↦')
        self.puntero_iniciar_secion.place(x = 235, y = 25)
        self.puntero_iniciar_secion.config(fg = '#003333', bg = 'deepskyblue', font=('Libre-Baskerville', 12), bd = 4, relief='solid')

        # Texto: Salir

        self.puntero_salir = tk.Label(self.pantalla, text = 'Salir ↦')
        self.puntero_salir.place(x = 312, y = 325)
        self.puntero_salir.config(fg = '#003333', bg = 'red', font=('Libre-Baskerville', 12), bd = 4, relief='solid')


        # Boton: Para salir

        self.boton_up8.config(command = self.ventana.destroy)

        # Boton: Para registrar un nuevo usuario:

        self.boton_up1.config(command = self.registrar)

        # mainloop

        self.fin = self.ventana.mainloop()

    def registrar(self):

        # Destruir Labels

        self.puntero_iniciar_secion.destroy()
        self.puntero_registrarse.destroy()
        self.bienvenida.destroy()
        self.puntero_salir.destroy()

        # Desavilitar botones

        self.boton_up1.config(command = self.desavilitar_boton)
        self.boton_up8.config(command = self.desavilitar_boton)

        # Nueva página

        # Texto: Registrarse

        self.text_registro = tk.Label(self.pantalla, text = '▶ REGISTRARSE ◀') 
        self.text_registro.place(x = 113, y = 60)
        self.text_registro.config(fg = '#003333', bg = 'deepskyblue', font=('Libre-Baskerville', 12), bd = 4, relief='solid')

        # Texto: Nombre de usuario

        self.text_usuario = tk.Label(self.pantalla, text = 'Nombre de usuario: ')
        self.text_usuario.place(x = 5, y = 100)
        self.text_usuario.config(fg = '#003333', bg = 'deepskyblue', font=('Libre-Baskerville', 12), bd = 4, relief='solid')

        # Texto: Fondos iniciales

        self.text_fondos_in = tk.Label(self.pantalla, text='Fondos iniciales: ')
        self.text_fondos_in.place(x=5, y=180)
        self.text_fondos_in.config(fg = '#003333', bg = 'deepskyblue', font=('Libre-Baskerville', 12), bd = 4, relief='solid')

        # Texto: Nota: Fondos minimos

        self.text_nota_minimo = tk.Label(
            self.pantalla, 
            text='NOTA: Para poder crear una cuenta nescecita iniciala\ncon un minimo de 5000 Colones'
        )
        self.text_nota_minimo.place(x=13, y=280)
        self.text_nota_minimo.config(fg = '#003333', bg = 'deepskyblue', font=('Libre-Baskerville', 10), bd = 4, relief='solid')

        # Puntero: Continuar

        self.puntero_continuar_reg = tk.Label(
            self.pantalla, text = 'Continuar  ↦')
        self.puntero_continuar_reg.place(x = 263, y = 25)
        self.puntero_continuar_reg.config(fg = '#003333', bg = 'deepskyblue', font=('Libre-Baskerville', 12), bd = 4, relief='solid')

        # Entry: Nombre de usuario

        self.usuario = tk.StringVar()
        self.entrada_usuario = tk.Entry(
            self.pantalla, textvariable = self.usuario)
        self.entrada_usuario.place(x = 90, y = 140)
        self.entrada_usuario.config(bg = 'white', font = 60)

        # Puntero: Atras

        self.puntero_atras_reg = tk.Label(self.pantalla, text = '↤  Atras')
        self.puntero_atras_reg.place(x = 5, y = 25)
        self.puntero_atras_reg.config(fg = '#003333', bg = 'deepskyblue', font=('Libre-Baskerville', 12), bd = 4, relief='solid')

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

        self.habilitar_numerico()

    def habilitar_numerico(self):

        # Habilitar teclado numerico

        self.saldo_inicial = ''

        self.boton_under1.config(command=lambda: self.tec_num('1', 'Registro'))
        self.boton_under2.config(command=lambda: self.tec_num('2', 'Registro'))
        self.boton_under3.config(command=lambda: self.tec_num('3', 'Registro'))
        self.boton_under4.config(command=lambda: self.tec_num('4', 'Registro'))
        self.boton_under5.config(command=lambda: self.tec_num('5', 'Registro'))
        self.boton_under6.config(command=lambda: self.tec_num('6', 'Registro'))
        self.boton_under7.config(command=lambda: self.tec_num('7', 'Registro'))
        self.boton_under8.config(command=lambda: self.tec_num('8', 'Registro'))
        self.boton_under9.config(command=lambda: self.tec_num('9', 'Registro'))
        self.boton_under10.config(command=lambda: self.tec_num('', 'Registro', True))
        self.boton_under11.config(command=lambda: self.tec_num('0', 'Registro'))
        self.boton_under12.config(command=self.agregar_usuario)
    
    def tec_num(self, numero, objetivo, borrar=False):

        # Escribir en pantalla lo seleccionado en el tecclado numerico

        if borrar:
            self.saldo_inicial = ''
        self.saldo_inicial += numero

        if objetivo == 'Registro':
            self.caja_numeros.config(text=self.saldo_inicial)


    def volver_inicio(self, pantalla):

        if pantalla == 'agregar_usuario':

            # Destruir labels

            self.text_registro_exitoso.destroy()
            self.text_nuevo_usuario.destroy()
            self.text_contra.destroy()

            # Desabilitar botones

            self.boton_up1.config(command = self.desavilitar_boton)
            self.boton_up5.config(command = self.desavilitar_boton)

        elif pantalla == 'registrar':

            # Destruir labels

            self.puntero_atras_reg.destroy()
            self.puntero_continuar_reg.destroy()
            self.text_usuario.destroy()
            self.text_registro.destroy()
            self.text_fondos_in.destroy()
            self.caja_numeros.destroy()
            self.text_nota_minimo.destroy()

            # Destruir entrys

            self.entrada_usuario.destroy()

            # Desavilitar botones

            self.boton_up1.config(command = self.desavilitar_boton)
            self.boton_up5.config(command = self.desavilitar_boton)
            self.desavilitar_teclado_num()

        # volver a inicio

        self.inicio()

    def desavilitar_teclado_num(self):

        # Desavilitar teclado numerico

        self.boton_under1.config(command=self.desavilitar_boton)
        self.boton_under2.config(command=self.desavilitar_boton)
        self.boton_under3.config(command=self.desavilitar_boton)
        self.boton_under4.config(command=self.desavilitar_boton)
        self.boton_under5.config(command=self.desavilitar_boton)
        self.boton_under6.config(command=self.desavilitar_boton)
        self.boton_under7.config(command=self.desavilitar_boton)
        self.boton_under8.config(command=self.desavilitar_boton)
        self.boton_under9.config(command=self.desavilitar_boton)
        self.boton_under10.config(command=self.desavilitar_boton)
        self.boton_under11.config(command=self.desavilitar_boton)
        self.boton_under12.config(command=self.desavilitar_boton)


    def agregar_usuario(self):

        # Desavilitar botones

        self.boton_up5.config(command = self.desavilitar_boton)
        self.desavilitar_teclado_num()

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

                # Labels

                # Texto registro exitoso

                self.text_registro_exitoso = tk.Label(
                    self.pantalla,
                    text = 'Registro Exitoso\nDebe recordar los siguientes '
                    'datos\npara poder iniciar seción')
                self.text_registro_exitoso.place(x = 40, y = 100)
                self.text_registro_exitoso.config(
                    fg = '#003333', bg = '#ACACAC', font = 40)

                # Texto nombre de usuario

                self.text_nuevo_usuario = tk.Label(
                    self.pantalla, text = 'Nombre de usuario: {}'.format(
                        self.usuario.get()))
                self.text_nuevo_usuario.place(x = 30, y = 200)
                self.text_nuevo_usuario.config(
                    fg = '#003333', bg = '#ACACAC', font = 40)

                # Texto contraseña

                self.text_contra = tk.Label(
                    self.pantalla, text = 'Contraseña: {}'.format(contra))
                self.text_contra.place(x = 30, y = 250)
                self.text_contra.config(fg = '#003333', bg = '#ACACAC', font = 40)

                # Guardar datos en el servidor 

                self.socket.send_string('{}/{}/{}/{}'.format('Registrar', self.usuario.get(), contra, self.saldo_inicial))
                message = self.socket.recv().decode("utf-8")
                

            else:
                self.registrar()
        except ValueError:
            self.registrar()

    def desavilitar_boton(self):
        pass


def registro():
    cajero = Cajero()
    cajero.inicio()


if __name__ == '__main__':
    registro()


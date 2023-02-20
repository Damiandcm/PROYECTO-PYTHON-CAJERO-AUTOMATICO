# PROYECTO-PYTHON-CAJERO-AUTOMATICO

Integrantes:
1. Isaac Damían Campos Montero - C11571
2. Sebastián Jesús Fallas Fallas - C12765
3. Steven Gerardo Chacón Salazar -  C12023

El presente repositorio corresponde a la creación de un sistema de cajero automático, el cual por medio de sockets es capaz
de almacenar información en un servidor local, el usuario tiene la posibilidad de realizar diferentes acciones:

1) Depositar y retirar fondos de la cuenta cliente.
2) Consultar los fondos e información de la cuenta cliente.
3) Mostrar el estado de movimiento de la cuenta cliente.
4) Información del cliente.
5) Salir


***Sobre Este Repositorio***

Este repositorio es donde se crea PROYECTO-PYTHON-CAJERO-AUTOMATICO, las herramientas, procesos y funciones que se evidencian dentro del programa son gracias al uso de las diferentes bibliotecas y características que forman parte del lenguaje de programación Python, en este caso el proyecto presenta el objetivo de mostrar al usuario un programa con una interfaz gráfica útil para el cliente, donde sea capaz de realizar diferentes acciones (tramites) los cuales se pueden realizar en un cajero automático de cualquier sistemas bancario actual.

De esta manera, el código presenta un sistema el cual está conectado a un servidor de una máquina virtual (Virtual-Machine) que se encarga de recibir, enviar y gestionar los datos de los clientes, como la información del cliente y fondos bancarios. Dicho servidor funciona con el uso de socket los cuales sirven como un canal eficaz de comunicación de datos por medio de la red, que utiliza archivos JSON, de este modo estos archivos son interpretados por el servidor como texto plano o como variables. 

El programa tiene la capacidad de registrar usuarios en el sistema y almacenar sus datos directamente en el servidor, en este caso el usuario debe insertar un nombre de usuario que desee y el programa proporcionará una contraseña personalizada automáticamente, la cual deberá recordar para poder iniciar sesión la próxima vez, de esta manera la próxima vez que el usuario acceda, el sistema ya poseerá los datos de ese cliente y podrá iniciar correctamente con el usuario y contraseña que le corresponde.

La interfaz gráfica presente en el proyecto permite al usuario interactuar y realizar las funciones deseadas. Dicha interfaz fue creada con Tkinter, lo que permite introducir un estilo personalizado, diferentes botones y ventanas interactivas. Por otro lado este también integra sonidos al iniciar el programa y en medio de todo el proceso que desee realizar el cliente, esto gracias a la librería Pygame que permite insertar diferentes archivos de audio y programarlos con funciones determinadas.


Respecto a las funciones integradas:

1) Depositar y retirar fondos de la cuenta cliente.

-El cliente tiene la posibilidad de depositar o retirar fondos de su cuenta bancaria, en este caso el servidor que almacena los datos recibe la solicitud hecha por el usuario y ejecuta la función correspondiente. Si el usuario deposita fondos, el servidor almacena la cantidad de fondos depositada y la guarda en su cuenta cliente, de otro modo si el usuario retira fondos, el servidor extrae los fondos de los datos almacenados y se verá reflejado como un rebajo en la cuenta.


2) Consultar los fondos e información de la cuenta cliente.

-EL cliente puede consultar los fondos de su cuenta, también como su información cuenta, en este caso el programa accede a los datos almacenados en el servidor y muestra la información solicitada en pantalla.


3) Mostrar el estado de movimiento de la cuenta cliente.

-En caso de que el cliente lo desee, puede consultar los movimientos realizados en su cuenta y el programa refleja en pantalla los movimientos almacenados en el servidor ya sea que haya depositado o retirado fondos.


4) Información del cliente.

-EL cliente puede consultar la información personal, de esta manera el programa muestra la información que se encuentra en el servidor respecto a la información del cliente.


5) Salir

-El programa tiene la capacidad si el usuario lo desea de poder salir del programa de cajero al presionar un botón, en este caso el programa se cierra.




***Requisitos***

El programa fue ejecutado en el sistema operativo de Linux, por lo tanto, es necesario lo siguientes requisitos para su correcta ejecución y funcionamiento, de lo contrario el programa no funcionará de la manera esperada.

*LIBRERIA JSON*

Para instalar esta librería se deben ejecutar los siguientes comandos:
```
sudo apt update
sudo apt install python3-json
```
*LIBRERIA PYGAME*

Para instalar esta librería se deben ejecutar los siguientes comandos:
```
sudo apt update
sudo apt install python3-pygame
```
*PIP*

Para instalar este módulo se deben ejecutar los siguientes comandos:
```
sudo apt update
sudo apt install python3-pip
```
*LIBRERIA TKINTER*

Para instalar esta librería se deben ejecutar los siguientes comandos:
```
sudo apt update
sudo apt install python3-tk
```
*LIBRERIA ZMQ*

Para instalar esta librería se deben ejecutar los siguientes comandos:
```
sudo apt update
sudo apt install python3-zmq
```
*LIBRERIA JSON*

Para instalar esta librería se deben ejecutar los siguientes comandos:
```
sudo apt update
sudo apt install python3-json
```


**CARPETAS:
1. INTERFAZ GRAFICA DE USUARIO  
2. SERVIDOR
3. EJEMPLO DE SERVIDOR
4. ARCHIVO_JSON

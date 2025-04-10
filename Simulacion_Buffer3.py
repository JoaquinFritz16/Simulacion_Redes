import time
import random

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conected = []
        self.buffer = []

    def agregar_conexion(self, nodo):
        if nodo not in self.conected:
            self.conected.append(nodo)
            nodo.conected.append(self)
            print(f"{self.nombre} se ha conectado con {nodo.nombre}")

    def enviar_message(self, message):
        if self.conected:
            print(f"{self.nombre} enviando mensaje: '{message}'")
            for nodo in self.conected:
                nodo.recibir_message(message, self)

    def recibir_message(self, message, nodo):
        
        if random.random() > 0.2:
            print(f"{self.nombre} ha recibido un mensaje de {nodo.nombre}: '{message}'")
            self.buffer.append((message, nodo))
        else:
            print(f"{self.nombre} perdió un mensaje de {nodo.nombre}: '{message}'")

    def procesar_buffer(self):
        print(f"{self.nombre} procesando mensajes en el buffer...")
        while self.buffer:
            message, nodo = self.buffer.pop(0)
            print(f"{self.nombre} procesó el mensaje de {nodo.nombre}: '{message}'")

    def remove_conection(self, nodo):
        if nodo in self.conected:
            self.conected.remove(nodo)
            nodo.conected.remove(self)
            print(f"{self.nombre} se ha desconectado de {nodo.nombre}")
        else:
            print(f"{self.nombre} no está conectado a {nodo.nombre}")

server = Nodo("Servidor")
cliente1 = Nodo("Cliente 1")
cliente2 = Nodo("Cliente 2")
cliente3 = Nodo("Cliente 3")

server.agregar_conexion(cliente1)
server.agregar_conexion(cliente2)
cliente1.agregar_conexion(cliente3)


print("\n--- Enviando mensajes ---")
time.sleep(2)
server.enviar_message("Hola, ¿cómo estás?")
cliente1.enviar_message("Hola, estoy bien. ¿Y tú?")
cliente2.enviar_message("No me importa cliente 1, trabaja más")
cliente3.enviar_message("Hola, cliente 2. ¿Qué tal?")


print("\n--- Procesando buffers ---")
time.sleep(2)
server.procesar_buffer()
cliente1.procesar_buffer()
cliente2.procesar_buffer()
cliente3.procesar_buffer()
time.sleep(2)
cliente1.remove_conection(cliente3)
print("Simulacion de conexion de cliente 1 y cliente 3")
server.enviar_message("¡HOLA A TODOS DE NUEVO!")
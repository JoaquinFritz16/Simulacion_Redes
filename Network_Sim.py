class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conected = []
    def agregar_conexion(self, nodo):
        if nodo not in self.conected:
            self.conected.append(nodo)
            nodo.conected.append(self)
            print(f"{self.nombre} se ha conectado con {nodo.nombre}")

        print(f"{self.nombre} esta conectado con {nodo}")
    def enviar_message(self, message):
        if self.conected:
            print(f"{self.nombre} enviando mensaje: '{message}'")
            for nodo in self.conected:
                nodo.recibir_message(message, self)
    def recibir_message(self, message, nodo):
        print(f"{self.nombre} ha recibido un mensaje de {nodo.nombre}: '{message}'")
server = Nodo("Servidor")
cliente1 = Nodo("Cliente 1")
cliente2 = Nodo("Cliente 2")
cliente3 = Nodo("Cliente 3")

server.agregar_conexion(cliente1)
server.agregar_conexion(cliente2)
cliente1.agregar_conexion(cliente3)

server.enviar_message("Hola, ¿cómo estás?")
cliente1.enviar_message("Hola, estoy bien. ¿Y tú?")
cliente2.enviar_message("No me importa cliente 1, trabaja más")
cliente3.enviar_message("Hola, cliente 2. ¿Qué tal?")
import threading
import time

condicion = threading.Condition()
buffer = []

def receptor():
    for i in range(5):
        time.sleep(1)
        with condicion:
            buffer.append(f"Paquete {i}")
            print(f"Receptor: Paquete {i} recibido")
            condicion.notify()

def procesador():
    while True:
        with condicion:
            while not buffer:
                print("Procesador: Esperando paquetes...")
                condicion.wait()
            paquete = buffer.pop(0)
            print(f"Procesador: Procesando {paquete}")
        if paquete == "Paquete 4":
            break

h1 = threading.Thread(target=receptor)
h2 = threading.Thread(target=procesador)

h2.start()
h1.start()
h1.join()
h2.join()
import threading
import time

impresora_color = threading.Semaphore(2)

def imprimir_trabajo(id_trabajo):
    with impresora_color:
        print(f"Trabajo {id_trabajo} imprimiendo...")
        time.sleep(1)
        print(f"Trabajo {id_trabajo} terminado")

hilos = [threading.Thread(target=imprimir_trabajo, args=(i,)) for i in range(10)]
for h in hilos: h.start()
for h in hilos: h.join()
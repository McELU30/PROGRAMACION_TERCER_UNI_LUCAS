import threading

descargas = 0
lock = threading.Lock()

def registrar_descarga():
    global descargas
    with lock:
        descargas += 1
        print(f"Descargas totales: {descargas}")

hilos = [threading.Thread(target=registrar_descarga) for _ in range(100)]
for h in hilos: h.start()
for h in hilos: h.join()
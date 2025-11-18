# Archivo: three_licenses_semaphore.py
# Controla acceso concurrente con 3 licencias disponibles.
import threading
import time

licenses = threading.Semaphore(3)

def usar_software(id):
    print(f"Diseñador {id} intenta ejecutar el software...")
    with licenses:
        print(f"Diseñador {id} ejecutando (licencia ocupada).")
        time.sleep(1.2)  # tiempo de uso de la licencia
        print(f"Diseñador {id} terminó y liberó la licencia.")

if __name__ == "__main__":
    threads = []
    for i in range(1, 16):
        t = threading.Thread(target=usar_software, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("Todos los diseñadores terminaron.")

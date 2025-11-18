# Archivo: db_connections_semaphore.py
# Simula un pool de 8 conexiones usando Semaphore.
import threading
import time
from concurrent.futures import ThreadPoolExecutor

pool = threading.Semaphore(8)

def simular_conexion(id):
    print(f"Tarea {id} intentando entrar...")
    with pool:  # acquire/release automático con context manager en Python 3.9+
        print(f"Tarea {id} conectada. (uso de conexión)")
        time.sleep(1)  # simula trabajo con la BD
        print(f"Tarea {id} liberando conexión.")

if __name__ == "__main__":
    n = 20
    threads = []
    for i in range(1, n+1):
        t = threading.Thread(target=simular_conexion, args=(i,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print("Todas las tareas finalizadas.")

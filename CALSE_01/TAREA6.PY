import threading
import time

def cargar_cache():
    print("Cargando configuración en caché...")
    time.sleep(2)
    print("Caché lista")

def usar_configuracion():
    print("Usando configuración")

hilo_cache = threading.Thread(target=cargar_cache)
hilo_cache.start()
hilo_cache.join()  # Espera a que termine
usar_configuracion()
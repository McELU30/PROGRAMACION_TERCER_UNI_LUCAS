# Archivo: inventory_mutex.py
# Demuestra exclusión mutua para evitar inconsistencias en el stock.
import threading
import time

stock = 50
stock_lock = threading.Lock()

def procesar_pedido(name):
    global stock
    # cada hilo quita 1 unidad (simulamos un pedido)
    with stock_lock:
        print(f"{name} lee stock = {stock}")
        if stock > 0:
            nuevo = stock - 1
            time.sleep(0.1)  # simula trabajo
            stock = nuevo
            print(f"{name} escribe stock = {stock}")
        else:
            print(f"{name} no hay stock")

if __name__ == "__main__":
    t1 = threading.Thread(target=procesar_pedido, args=("Pedido-1",))
    t2 = threading.Thread(target=procesar_pedido, args=("Pedido-2",))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(f"Stock final: {stock} (debería ser 48 si ambos pidieron 1)")

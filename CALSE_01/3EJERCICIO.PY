# Archivo: producer_consumer_condition.py
# Sincroniza productor (fabrica) y consumidor (inspector) con Condition.
import threading
import time

condition = threading.Condition()
pdf_terminado = False

def fabrica():
    global pdf_terminado
    print("Fábrica: Generando PDF...")
    time.sleep(1.5)  # simula tiempo de producción
    with condition:
        pdf_terminado = True
        print("Fábrica: PDF terminado. Notificando inspector...")
        condition.notify()  # despierta al inspector

def inspector():
    print("Inspector: listo para escanear, esperando PDF...")
    with condition:
        while not pdf_terminado:
            condition.wait()
        print("Inspector: PDF recibido, procedo a escanear...")
        time.sleep(0.8)
        print("Inspector: escaneo finalizado.")

if __name__ == "__main__":
    t_inspector = threading.Thread(target=inspector)
    t_fabrica = threading.Thread(target=fabrica)

    t_inspector.start()
    t_fabrica.start()
    t_fabrica.join()
    t_inspector.join()
    print("Proceso terminado.")

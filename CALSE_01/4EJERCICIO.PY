# Archivo: shared_file_logger.py
# Varios hilos escriben en el mismo archivo sin entrelazado de bytes.
import threading
import time
import os

file_lock = threading.Lock()
log_file = "log.txt"

def escribir_log(writer_id):
    for i in range(3):
        mensaje = f"Writer {writer_id} - mensaje {i+1} at {time.strftime('%H:%M:%S.%f')}"
        with file_lock:
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(mensaje + os.linesep)
        time.sleep(0.2)

if __name__ == "__main__":
    # limpiar archivo previo
    if os.path.exists(log_file):
        os.remove(log_file)

    threads = []
    for i in range(1, 6):
        t = threading.Thread(target=escribir_log, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("Escritura de logs finalizada. Revisa log.txt")

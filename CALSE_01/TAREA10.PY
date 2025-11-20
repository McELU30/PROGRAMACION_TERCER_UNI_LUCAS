import threading

usuario = {"email": "a@correo.com", "telefono": "123"}
lock_usuario = threading.Lock()

def actualizar_email():
    with lock_usuario:
        copia = usuario.copy()
        copia["email"] = "nuevo@correo.com"
        usuario.update(copia)
        print("Email actualizado")

def actualizar_telefono():
    with lock_usuario:
        copia = usuario.copy()
        copia["telefono"] = "456"
        usuario.update(copia)
        print("Teléfono actualizado")

h1 = threading.Thread(target=actualizar_email)
h2 = threading.Thread(target=actualizar_telefono)

h1.start()
h2.start()
h1.join()
h2.join()

print("Usuario final:", usuario)
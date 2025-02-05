import tkinter as tk
from tkinter import messagebox

class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.items = []

    def vacia(self):
        return len(self.items) == 0

    def insertar(self, item):
        self.items.append(item)

    def suprimir(self):
        if not self.vacia():
            return self.items.pop()
        return None

    def mostrar(self):
        return self.items

def VerificaMovimiento(pila_origen, pila_destino):
    if pila_origen.vacia():
        return False, "La pila de origen está vacía."

    disco_origen = pila_origen.suprimir()
    pila_origen.insertar(disco_origen)

    if not pila_destino.vacia():
        disco_destino = pila_destino.suprimir()
        pila_destino.insertar(disco_destino)
    else:
        disco_destino = -1

    if not pila_destino.vacia() and disco_destino < disco_origen:
        return False, "No puedes mover un disco más grande sobre uno más pequeño."

    return True, ""

def mover_disco_manual(origen, destino):
    valido, mensaje = VerificaMovimiento(pilas[origen], pilas[destino])
    if valido:
        pilas[destino].insertar(pilas[origen].suprimir())
        actualizar_interfaz()
        if len(pilas[2].mostrar()) == n:
            messagebox.showinfo("¡Juego completado!", "¡Felicidades, has completado el juego!")
    else:
        messagebox.showinfo("Movimiento inválido", mensaje)

def seleccionar_pila(pila):
    global seleccion
    if seleccion is None:
        seleccion = pila
        label_seleccion.config(text=f"Pila seleccionada: {pila + 1}")
    else:
        mover_disco_manual(seleccion, pila)
        seleccion = None
        label_seleccion.config(text="Pila seleccionada: Ninguna")

def actualizar_interfaz():
    canvas.delete("all")
    ancho_torre = 5
    alto_disco = 20
    ancho_canvas = canvas.winfo_width()
    alto_canvas = canvas.winfo_height()
    x_offset = ancho_canvas // 6
    y_offset = alto_canvas - 30

    colores = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan", "magenta", "brown"]

    for i, pila in enumerate(pilas):
        x_centro = (2 * i + 1) * x_offset
        canvas.create_rectangle(x_centro - ancho_torre // 2, y_offset - n * alto_disco, x_centro + ancho_torre // 2, y_offset, fill="black")
        for j, disco in enumerate(pila.mostrar()):
            ancho_disco_actual = (disco + 1) * 10
            color_disco = colores[disco % len(colores)]
            canvas.create_rectangle(x_centro - ancho_disco_actual // 2, y_offset - (j + 1) * alto_disco, x_centro + ancho_disco_actual // 2, y_offset - j * alto_disco, fill=color_disco)
            canvas.create_text(x_centro, y_offset - (j + 0.5) * alto_disco, text=str(disco + 1), fill="white")

def iniciar_juego():
    global n, pilas, seleccion
    n = int(entry.get())
    pilas = [Pila(n), Pila(n), Pila(n)]
    seleccion = None
    for i in reversed(range(n)):
        pilas[0].insertar(i)
    actualizar_interfaz()

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Torres de Hanoi")

frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, text="Ingrese el número de discos:")
label.pack(side=tk.LEFT)

entry = tk.Entry(frame)
entry.pack(side=tk.LEFT)

button = tk.Button(frame, text="Iniciar Juego", command=iniciar_juego)
button.pack(side=tk.LEFT)

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Añadir etiqueta para mostrar la pila seleccionada
label_seleccion = tk.Label(root, text="Pila seleccionada: Ninguna")
label_seleccion.pack()

# Añadir botones para seleccionar las pilas
botones_frame = tk.Frame(root)
botones_frame.pack()

boton_pila_0 = tk.Button(botones_frame, text="Pila 1", command=lambda: seleccionar_pila(0))
boton_pila_0.pack(side=tk.LEFT)

boton_pila_1 = tk.Button(botones_frame, text="Pila 2", command=lambda: seleccionar_pila(1))
boton_pila_1.pack(side=tk.LEFT)

boton_pila_2 = tk.Button(botones_frame, text="Pila 3", command=lambda: seleccionar_pila(2))
boton_pila_2.pack(side=tk.LEFT)

root.mainloop()
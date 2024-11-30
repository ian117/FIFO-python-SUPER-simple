
# remember to sudo apt-get install python3-tk
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from collections import deque

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Archivos FIFO")
root.geometry("1200x700")

# Cola FIFO para los nombres de archivos
file_queue = deque()

# Funciones de la aplicación
def agregar_archivo():
    archivo = filedialog.askopenfilename(title="Selecciona un archivo")
    if archivo:
        file_queue.append(archivo)
        messagebox.showinfo("Archivo Agregado", f"Archivo '{archivo}' agregado a la cola.")
        actualizar_lista()

def sacar_archivo():
    if file_queue:
        archivo_eliminado = file_queue.popleft()
        messagebox.showinfo("Archivo Eliminado", f"Archivo más antiguo eliminado: {archivo_eliminado}")
        actualizar_lista()
    else:
        messagebox.showwarning("Cola Vacía", "No hay archivos en la cola para eliminar.")

def mostrar_archivos():
    if file_queue:
        archivos = "\n".join(file_queue)
        messagebox.showinfo("Archivos en Cola", f"Archivos en la cola:\n{archivos}")
    else:
        messagebox.showinfo("Cola Vacía", "No hay archivos en la cola.")

def actualizar_lista():
    lista_archivos.delete(0, tk.END)
    for archivo in file_queue:
        lista_archivos.insert(tk.END, archivo)

# Crear botones y lista
boton_agregar = tk.Button(root, text="Agregar Archivo", command=agregar_archivo)
boton_agregar.pack(pady=5)

boton_sacar = tk.Button(root, text="Sacar Archivo Más Antiguo", command=sacar_archivo)
boton_sacar.pack(pady=5)

boton_mostrar = tk.Button(root, text="Mostrar Archivos en Cola", command=mostrar_archivos)
boton_mostrar.pack(pady=5)

lista_archivos = tk.Listbox(root, height=50, width=140)
lista_archivos.pack(pady=10)

# Iniciar la interfaz gráfica
root.mainloop()

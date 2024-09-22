import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime

# Función para agregar un nuevo evento
def agregar_evento():
    fecha = fecha_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_text.get("1.0", "end-1c")

    # Validación de que los campos no estén vacíos
    if fecha and hora and descripcion:
        tree.insert('', 'end', values=(fecha, hora, descripcion))
        fecha_entry.set_date(datetime.now())  # Reiniciar la fecha al día actual
        hora_entry.delete(0, 'end')
        descripcion_text.delete("1.0", "end")
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

# Función para eliminar un evento seleccionado con confirmación
def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar el evento?")
        if confirmar:
            tree.delete(selected_item)
    else:
        messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Personal UEA-2024")
root.configure(bg="#f0f8ff")  # Fondo color azul claro

# Frame para mostrar la lista de eventos
frame_lista = tk.Frame(root, bg="#f0f8ff")
frame_lista.pack(pady=20)

# TreeView para mostrar la lista de eventos
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings', height=8)
tree.heading('Fecha', text="Fecha (dd/mm/aaaa)")
tree.heading('Hora', text="Hora")
tree.heading('Descripción', text="Descripción")
tree.pack()

# Frame para la entrada de datos
frame_entrada = tk.Frame(root, bg="#f0f8ff")
frame_entrada.pack(pady=20)

# Etiquetas y campos de entrada
tk.Label(frame_entrada, text="Fecha (dd/mm/aaaa):", bg="#f0f8ff", fg="#00008b").grid(row=0, column=0, padx=10, pady=5)
fecha_entry = DateEntry(frame_entrada, date_pattern="dd/MM/yyyy", bg="#fafad2", fg="#000000")
fecha_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_entrada, text="Hora:", bg="#f0f8ff", fg="#00008b").grid(row=1, column=0, padx=10, pady=5)
hora_entry = tk.Entry(frame_entrada, bg="#fafad2", fg="#000000")
hora_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_entrada, text="Descripción:", bg="#f0f8ff", fg="#00008b").grid(row=2, column=0, padx=10, pady=5)
descripcion_text = tk.Text(frame_entrada, height=5, width=40, bg="#fafad2", fg="#000000")
descripcion_text.grid(row=2, column=1, padx=10, pady=5)

# Frame para los botones de acción
frame_botones = tk.Frame(root, bg="#f0f8ff")
frame_botones.pack(pady=20)

# Botones para agregar, eliminar y salir
agregar_btn = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento, bg="#20b2aa", fg="white")
agregar_btn.grid(row=0, column=0, padx=10)

eliminar_btn = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento, bg="#dc143c", fg="white")
eliminar_btn.grid(row=0, column=1, padx=10)

salir_btn = tk.Button(frame_botones, text="Salir", command=root.quit, bg="#ff4500", fg="white")
salir_btn.grid(row=0, column=2, padx=10)

# Iniciar la aplicación
root.mainloop()


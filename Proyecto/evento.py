import tkinter as tk
from tkinter import ttk
import json

class CalendarioApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calendario")
        self.geometry("800x600")

        self.agregar_btn = tk.Button(self, text="Agregar evento", command=self.mostrar_formulario)
        self.agregar_btn.pack()

    def mostrar_formulario(self):
        formulario = tk.Toplevel(self)
        formulario.title("Agregar evento")
        formulario.geometry("800x600")

        # Estilo de los widgets
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 12))

        
        # Campo de título
        tk.Label(formulario, text="Título", font=("Arial", 12)).grid(row=0, column=0, pady=10, padx=10, sticky="w")
        titulo_entry = tk.Entry(formulario, font=("Arial", 12), width=30)
        titulo_entry.grid(row=0, column=1, pady=10, padx=10)

        # Campo de fecha y hora
        tk.Label(formulario, text="Fecha y hora", font=("Arial", 12)).grid(row=1, column=0, pady=10, padx=10, sticky="w")
        fecha_hora_entry = tk.Entry(formulario, font=("Arial", 12), width=30)
        fecha_hora_entry.grid(row=1, column=1, pady=10, padx=10)

        # Campo de duración
        tk.Label(formulario, text="Duración", font=("Arial", 12)).grid(row=2, column=0, pady=10, padx=10, sticky="w")
        duracion_entry = tk.Entry(formulario, font=("Arial", 12), width=10)
        duracion_entry.insert(0, "60")
        duracion_entry.grid(row=2, column=1, pady=10, padx=10)
        tk.Label(formulario, text="minutos", font=("Arial", 12)).grid(row=2, column=2, pady=10, padx=10, sticky="w")

        # Campo de descripción
        tk.Label(formulario, text="Descripción", font=("Arial", 12)).grid(row=3, column=0, pady=10, padx=10, sticky="nw")
        descripcion_text = tk.Text(formulario, font=("Arial", 12), height=5, width=30)
        descripcion_text.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        # Campo de importancia
        tk.Label(formulario, text="Importancia", font=("Arial", 12)).grid(row=4, column=0, pady=10, padx=10, sticky="w")
        importancia_var = tk.IntVar()
        tk.Checkbutton(formulario, text="Normal", variable=importancia_var, onvalue=0, offvalue=1).grid(row=4, column=1)
        tk.Checkbutton(formulario, text="Importante", variable=importancia_var, onvalue=1, offvalue=0).grid(row=4, column=2)

        # Campo de recordatorio
        tk.Label(formulario, text="Recordatorio (DD/MM/AAAA HH:MM)", font=("Arial", 12)).grid(row=5, column=0, pady=10, padx=10, sticky="w")
        recordatorio_entry = tk.Entry(formulario)
        recordatorio_entry.grid(row=5, column=1)

        # Campo de etiquetas
        tk.Label(formulario, text="Etiquetas (separadas por comas)", font=("Arial", 12)).grid(row=6, column=0, pady=10, padx=10, sticky="w")
        etiquetas_entry = tk.Entry(formulario)
        etiquetas_entry.grid(row=6, column=1)

        # Botón de guardar
        self.guardar_btn = tk.Button(formulario, text="Guardar", font=("Arial", 12), command=self.guardar_eventos)
        self.guardar_btn.grid(row=7, column=1)

    def __json__(self):
        return {
            'titulo': self.titulo_entry.get(),
            'fyh': self.fecha_hora_entry.get(),
            'duracion' : self.duracion_entry.get(),
            'descripccion' : self.descripcion_text.get(),
            'importancia': self.importancia_var.get(),
            'recodatorio': self.recordatorio_entry.get(),
            'etiquetas': self.etiquetas_entry.get(),

        }
    
    with open("eventos.json") as f:
            evento = json.load(f)

    def guardar_eventos(evento):
        with open('eventos.json', 'w') as f:
            json.dumps(evento)

    def buscar_eventos(titulo=None, etiqueta=None):
        resultados = []
        for evento in evento:
            if titulo and titulo.lower() not in evento["titulo"].lower():
                continue
            if etiqueta and etiqueta.lower() not in [etiq.lower() for etiq in evento["etiquetas"]]:
                continue
                resultados.append(evento)
                return resultados


if __name__ == "__main__":
    app = CalendarioApp()
    app.mainloop()

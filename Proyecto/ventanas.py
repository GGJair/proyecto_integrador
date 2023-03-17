import datetime
import tkinter as tk
import calendar

class VentanaCalendario():
    def __init__(self, master):
        
        # Inicializar la fecha de inicio de la semana en la fecha actual
        hoy = datetime.date.today()
        self.fecha_inicio_semana = hoy - datetime.timedelta(days=hoy.weekday())


        self.master = master
        self.master.title("Calendario Semanal")
        
        # Frame para los botones de navegación
        self.frame_botones = tk.Frame(self.master)
        self.frame_botones.pack(side="top", fill="x")
        
        # Botón para la semana anterior
        self.boton_anterior = tk.Button(self.frame_botones, text="< Semana anterior", command=self.anterior_semana)
        self.boton_anterior.pack(side="left")
        
        # Botón para la semana siguiente
        self.boton_siguiente = tk.Button(self.frame_botones, text="Siguiente semana >", command=self.siguiente_semana)
        self.boton_siguiente.pack(side="right")
        
        # Frame para el calendario
        self.frame_calendario = tk.Frame(self.master)
        self.frame_calendario.pack(side="top", fill="both", expand=True)
        
        # Variables de control
        self.mes = tk.StringVar()
        self.anio = tk.StringVar(value=datetime.date.today().year)
        self.mes.set(calendar.month_name[datetime.date.today().month])
        self.anio = tk.StringVar(value=datetime.date.today().year)
        self.semana = tk.StringVar(value=datetime.date.today().day)
        
        # Desplegable para seleccionar el mes
        self.menu_mes = tk.OptionMenu(self.frame_botones, self.mes, *calendar.month_name[1:])
        self.menu_mes.pack(side="left")
        
        # Desplegable para seleccionar el año
        self.menu_anio = tk.OptionMenu(self.frame_botones, self.anio, *[str(year) for year in range(datetime.date.today().year-10, datetime.date.today().year+11)])
        self.menu_anio.pack(side="left")

        self.dibujar_calendario()
        


    

        
        
    def dibujar_calendario(self):
        # Obtener la fecha actual
        mes = list(calendar.month_name).index(self.mes.get())
        anio = int(self.anio.get())

        # Obtener los días de la semana seleccionada
        dias_semana = [self.fecha_inicio_semana + datetime.timedelta(days=i) for i in range(7)]

        # Dibujar etiquetas para los días de la semana
        dias_labels = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"] 
        for i in range(len(dias_labels)):
            dia_label = tk.Label(self.frame_calendario, text=dias_labels[i], font=("Helvetica", 12), bg="white", padx=10, pady=5)
            dia_label.grid(row=0, column=i)

        # Dibujar las fechas de la semana seleccionada
        for i in range(len(dias_semana)):
            dia = dias_semana[i]
            dia_str = "{:02d}/{:02d}".format(dia.day, dia.month)
            dia_label = tk.Label(self.frame_calendario, text=dia_str, font=("Helvetica", 12), bg="white", padx=10, pady=5)
            dia_label.grid(row=1, column=i)

        
    def anterior_semana(self):
        # Obtener la semana actual
        semana_actual = int(self.semana.get())

        # Actualizar la semana
        nueva_semana = max(semana_actual - 1, 0)
        self.semana.set(nueva_semana)

        # Actualizar la fecha de inicio de la semana
        self.fecha_inicio_semana -= datetime.timedelta(days=7)

        # Dibujar el nuevo calendario
        self.dibujar_calendario()

    def siguiente_semana(self):
         # Obtener la semana actual
        semana_actual = int(self.semana.get())

        # Actualizar la semana
        nueva_semana = min(semana_actual + 1, 4)
        self.semana.set(nueva_semana)

        # Actualizar la fecha de inicio de la semana
        self.fecha_inicio_semana += datetime.timedelta(days=7)

        # Dibujar el nuevo calendario
        self.dibujar_calendario()
    

# Crear la ventana raíz
root = tk.Tk()

# Llamar a la clase VentanaCalendario
ventana_calendario = VentanaCalendario(root)

# Mostrar la interfaz
root.mainloop()

#Importar la librería 'tkinter' y renombrarla como 'tk'
import tkinter as tk

#Crea un nuevo objeto ventana
ventana = tk.Tk()

#Creamos un cuadro 'frame1' en (DONDE)
frame1 = tk.Frame(ventana)

#Creamos un cuadro 'frame2' en (DONDE)
frame2 = tk.Frame(frame1)

#Creamos un objeto 'entrada1' en (DONDE)
entrada1 = tk.Entry(ventana)

#Creamos un objeto 'boton1' en (DONDE, text="TEXTO")
boton1 = tk.Button(ventana, text="Presionar")

#Creamos un objeto 'etiqueta1' en (DONDE, text="TEXTO")
etiqueta1 = tk.Label(ventana, text="etiqueta")

#Creamos un objeto 'labelframe1' en (DONDE, text="TEXTO", bg="COLOR", padx=10, pady=10)
labelframe1 = tk.LabelFrame(ventana, text="label", bg="orange3", padx=10, pady=10)

#------------------FUNCIONES------------------------------------------------------------------------------------------------

def presionar_boton1():
    #le asignamos a la variable 'text' lo que esté en el campo de entrada
    text = entrada1.get()
    print(text)

#Si ocurre el evento disparador de la funcion (precionar el boton con la tecla '<Button-1>') se imprime 'boton precionado'
def one_click(evento):
    print("boton precionado")

#Retorna cualquier tecla precionada
def on_key_press(event):
    chatr_event = str(event.char)
    print(f"Tecla  {chatr_event} presionada")

#Retorna el (ANCHO X ALTO) de la ventana
def tamaño_ventana(event):
    print(f"TAMAÑO_VENTANA: {event.width} X {event.height}")

#Retorna las coordenadas del mouse dentro de la ventana (SIN CONTAR LOS VORDES)
def coordenadas_mouse(event):
    print(f"COORDENADAS_MOUSE: X:{event.x} - Y: {event.y}")

def one_click_A(event):
    print(f"{event.widget['text']} presionado")

    

#------------------CONFIG_FRAME---------------------------------------------------------------------------------------------

#Asignamos las propiedades a 'frame1'(ANCHO, ALTO, COLOR, BORDE)
frame1.configure(width=300, height=300, bg="orange4", bd=1)

#Asignamos las propiedades a 'frame2'(ANCHO, ALTO, COLOR, BORDE)
frame2.configure(width=10, height=10, bg="orange2", bd=0)

#------------------CONFIG_BUTTON---------------------------------------------------------------------------------------------

#Asignamos las propiedades a 'boton1'(fg=COLOR_LETRA,bg=COLOR_FONDO,font=("FUENTE",TAMAÑO,"ESTILO"),command=FUNCION_ASIGNADA_AL_BOTON)
boton1.config(fg="snow", bg="gray1", font=("Arial", 54, "italic"), command=presionar_boton1)

#Si se preciona el boton con la tecla '<Button-1>' se ejecutara la funcion 'one_click'
boton1.bind("<Button-1>",one_click_A)

#------------------CONFIG_LABEL---------------------------------------------------------------------------------------------

#Asignamos las propiedades a 'etiqueta1'(text=TEXTO,fg=COLOR_LETRA,bg=COLOR_FONDO,font=("FUENTE",TAMAÑO,"ESTILO"))
etiqueta1.config(text="n", fg="snow", bg="gray1", font=("Arial", 54, "italic"))

#------------------CONFIG_LABEL_FRAME---------------------------------------------------------------------------------------

#Asignamos las propiedades a 'labelframe1'(ANCHO, ALTO)
labelframe1.config(width=10, height=10)

#------------------CONFIG_ENTRY---------------------------------------------------------------------------------------------

#Asignamos las propiedades a 'entrada1'(fg=COLOR_LETRA,bg=COLOR_FONDO,font=("FUENTE",TAMAÑO,"ESTILO"))
entrada1.config(fg="snow", bg="gray1", font=("Arial", 54, "italic"))

#Dejamos un texto por defecto en la entrada
entrada1.insert(0, "Nombre")

#------------------CONFIG_VENTANA-------------------------------------------------------------------------------------------

#Le da el nombre al encabezado de la ventana (colocar antes de generar el loop)
ventana.title("ventana")

#Asignamos un tamaño a 'ventana' especificando ("ANCHOxALTO+CoordenadaHorizontal+CoordenadaVertical")
ventana.geometry("380x150+550+225")

#Asignamos un tamaño MÍNIMO a 'ventana' especificando (ANCHO, ALTO)
ventana.minsize(380, 150)

#Asignamos un tamaño MÁXIMO a 'ventana' especificando (ANCHO, ALTO)
ventana.maxsize(380, 150)

#Habilitar o deshabilitar la modificación manual del tamaño del objeto 'ventana' (ALTO, ANCHO) True/False
ventana.resizable(True, True)

#Agregar un logo al objeto 'ventana'(el cual debe ser una imagen y estar en la carpeta del proyecto con formato .ico)
ventana.iconbitmap("icono.ico")

#Cambiar color de fondo del objeto 'ventana'
ventana.configure(bg="khaki")

#Cambiar nivel de opacidad del objeto 'ventana'
ventana.attributes("-alpha", 1.0)

#Refresca la página cada (MILISEGUNDOS, FUNCIÓN)
ventana.after(0)

#Si se preciona el boton con la tecla '<KeyPress>'(CUALQUIER TECLA) se ejecutara la funcion 'on_key_press'
ventana.bind("<KeyPress>",on_key_press)

#Cuando dse mueve o modifica el tamaño de la ventana se llama a la funcion 'tamaño_ventana'
ventana.bind("<Configure>",tamaño_ventana)

#Detecla los movimientos del mouse dentro de la ventana (NO CUENTA LOS VORDES)
ventana.bind("<Motion>",coordenadas_mouse)

#------------------ORDEN_SALIDA---------------------------------------------------------------------------------------------

#'entrada1' aparecerá en 'ventana'
entrada1.pack()

#'boton1' aparecerá en 'ventana'
boton1.pack()

#'frame1' aparecerá en 'ventana'
frame1.pack()

#'frame2' aparecerá en 'frame1'
frame2.pack()

#'etiqueta1' aparecerá en 'ventana'
etiqueta1.pack()

#'labelframe1' aparecerá en 'ventana'
labelframe1.pack()

#Al objeto 'ventana' se le asigna un loop para que se mantenga abierto
ventana.mainloop()
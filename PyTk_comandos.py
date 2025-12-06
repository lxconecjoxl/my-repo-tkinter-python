#Importar la librería 'tkinter' y renombrarla como 'tk'
import tkinter as tk

#Crea un nuevo objeto ventana
ventana = tk.Tk()

#Creamos un cuadro 'frame"n"' en (DONDE)
frame1 = tk.Frame(ventana)
frame2 = tk.Frame(frame1)

#Creamos un objeto 'entrada "n"' en (DONDE)
entrada1 = tk.Entry(ventana)

#Creamos un objeto 'radio "n"' en (DONDE)
radio1=tk.Radiobutton(ventana)
radio2=tk.Radiobutton(ventana)

#Creamos un objeto 'check "n"' en (DONDE)
check1=tk.Checkbutton(ventana)
check2=tk.Checkbutton(ventana)

#Creamos un objeto 'labelframe "n"' en (DONDE)
labelframe1 = tk.LabelFrame(ventana)

#Creamos un objeto 'boton "n"' en (DONDE, text="TEXTO")
boton1 = tk.Button(ventana, text="Presionar",)

#Creamos un objeto 'etiqueta "n"' en (DONDE, text="TEXTO")
etiqueta1 = tk.Label(ventana, text="etiqueta")
etiqueta2 = tk.Label(ventana, text="etiqueta")

#Vatriable de control para radio_button
variable_control = tk.IntVar()

#Vatriable de control para check_button
variable_contro_check1=tk.BooleanVar()
variable_contro_check2=tk.BooleanVar()

#------------------FUNCIONES------------------------------------------------------------------------------------------------

def presionar_boton1():
    #le asignamos a la variable 'text' lo que esté en el campo de entrada
    print(f"{entrada1.get()}")


def selecciono():
    print(f"{variable_control.get()}")

#Si ocurre el evento disparador de la funcion (precionar el boton con la tecla '<Button-1>') se imprime 'boton precionado'
def one_click(evento):
    print("boton precionado")

#Retorna cualquier tecla precionada
def on_key_press(event):
    chatr_event = str(event.char)
    print(f"Tecla  {chatr_event} presionada")

#Retorna el (ANCHO X ALTO) de la ventana
def tamaño_ventana(event):
    print(f"TAMAÑO_VENTANA: {ventana.winfo_width()}x{ventana.winfo_height()}")

#Retorna las coordenadas del mouse dentro de la ventana (SIN CONTAR LOS VORDES)
def coordenadas_mouse(event):
    print(f"COORDENADAS_MOUSE: X:{event.x} - Y: {event.y}")

#Retorna el nombre del widget seleccionado
def one_click_A(event):
    print(f"{event.widget['text']} presionado")

   
#------------------CONFIG_FRAME---------------------------------------------------------------------------------------------

#Asignamos las propiedades a 'frame "n"'(ANCHO, ALTO, COLOR, BORDE)
frame1.configure(width=300, height=300, bg="orange4", bd=1)
frame2.configure(width=10, height=10, bg="orange2", bd=0)

#------------------CONFIG_BUTTON---------------------------------------------------------------------------------------------

#Asignamos las propiedades a 'boton "n"'(fg=COLOR_LETRA,bg=COLOR_FONDO,font=("FUENTE",TAMAÑO,"ESTILO"),esstado=AVILIRADO/DESAVILITADO, command=FUNCION_ASIGNADA_AL_BOTON)
boton1.config(fg="snow", bg="gray1", font=("Arial", 54, "italic"),state="disabled",command=selecciono)

#Si se preciona el boton con la tecla '<Button-1>' se ejecutara la funcion 'one_click'
#boton1.bind("<Button-1>",lambda event: selecciono)
boton1.bind("<Button-1>",one_click_A)

#------------------CONFIG_RADIO---------------------------------------------------------------------------------------------

#Asignamos las propiedades a 'radio "n"'(text=TEXTO,fg=COLOR_LETRA,bg=COLOR_FONDO,font=("FUENTE",TAMAÑO,"ESTILO"),value=VALOR_ASIGNADO,command=FUNCION_ASIGNADA_AL_RADIO)
radio1.config(text="Manzanas",fg="gray1", bg="khaki", font=("Arial", 54, "italic"), variable=variable_control,value=1)
radio2.config(text="Pera",fg="gray1", bg="khaki", font=("Arial", 54, "italic"), variable=variable_control,value=2)

#------------------CONFIG_CHECK---------------------------------------------------------------------------------------------

##Asignamos las propiedades a 'check "n"'(text=TEXTO,fg=COLOR_LETRA,bg=COLOR_FONDO,font=("FUENTE",TAMAÑO,"ESTILO"),
#                                        value=VALOR_ASIGNADO,
#                                        command=FUNCION_ASIGNADA_AL_check)
check1.config(text="Manzanas",fg="gray1", bg="khaki", font=("Arial", 54, "italic"), 
              variable=variable_contro_check1,
            #imprimo el nombre de la seleccion como marcada si el valor de la variable de control es 1, si no retorna el nombre de la seleccion como  
              command=lambda: print(f"{check1['text']} marcada" if variable_contro_check1.get() == 1 else f"{check1['text']} desmarcada"))

check2.config(text="Pera",fg="gray1", bg="khaki", font=("Arial", 54, "italic"), 
              variable=variable_contro_check2,
              #imprimo el nombre de la seleccion como marcada si el valor de la variable de control es 1, si no retorna el nombre de la seleccion como  
              command=lambda: print(f"{check2['text']} marcada" if variable_contro_check2.get() == 1 else f"{check2['text']} desmarcada"))

#------------------CONFIG_LABEL---------------------------------------------------------------------------------------------

#Asignamos las propiedades a 'etiqueta "n"'(text=TEXTO,fg=COLOR_LETRA,bg=COLOR_FONDO,font=("FUENTE",TAMAÑO,"ESTILO"))
etiqueta1.config(text="pollo1", fg="snow", bg="gray1", font=("Arial", 54, "italic"))
etiqueta2.config(text="pollo2", fg="snow", bg="gray1", font=("Arial", 54, "italic"))

#------------------CONFIG_LABEL_FRAME---------------------------------------------------------------------------------------

#Asignamos las propiedades a 'labelframe "n"'(text="TEXTO", bg="COLOR", padx=SEPARACION_EN_X, pady=SEPARACION_EN_Y, width=ANCHO, height=ALTO)
labelframe1.config(text="label", bg="orange3", padx=10, pady=10, width=10, height=10)

#------------------CONFIG_ENTRY---------------------------------------------------------------------------------------------

#Asignamos las propiedades a 'entrada "n"'(fg=COLOR_LETRA,bg=COLOR_FONDO,font=("FUENTE",TAMAÑO,"ESTILO"))
entrada1.config(fg="snow", bg="gray1", font=("Arial", 54, "italic"))

#Dejamos un texto por defecto en la entrada
entrada1.insert(0, "Nombre")

#------------------CONFIG_VENTANA-------------------------------------------------------------------------------------------

#Le da el nombre al encabezado de la ventana (colocar antes de generar el loop)
ventana.title("ventana")

#Asignamos un tamaño a 'ventana' especificando ("ANCHOxALTO+CoordenadaHorizontal+CoordenadaVertical")
ventana.geometry("780x261+0+0")

#Asignamos un tamaño MÍNIMO a 'ventana' especificando (ANCHO, ALTO)
#ventana.minsize(380, 150)

#Asignamos un tamaño MÁXIMO a 'ventana' especificando (ANCHO, ALTO)
#ventana.maxsize(380, 150)

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
#ventana.bind("<Configure>",tamaño_ventana)
ventana.bind("<Button-4>",tamaño_ventana)

#Detecla los movimientos del mouse dentro de la ventana (NO CUENTA LOS VORDES)
ventana.bind("<Button-5>",coordenadas_mouse)

#------------------ORDEN_SALIDA_PACK---------------------------------------------------------------------------------------------

#PACK 'entrada1' aparecerá en 'ventana'
#entrada1.pack()

#PACK 'check1' aparecerá en 'ventana'
#check1.pack()

#PACK 'check2' aparecerá en 'ventana'
#check2.pack()

#PACK 'check1' aparecerá en 'ventana'
#radio1.pack()

#PACK 'check2' aparecerá en 'ventana'
#radio2.pack()

#PACK 'frame1' aparecerá en 'ventana'
#frame1.pack()

#PACK 'frame2' aparecerá en 'frame1'
#frame2.pack()

#PACK 'etiqueta1' aparecerá en 'ventana'
#etiqueta1.pack(side="right",padx=15)

#PACK 'boton1' aparecerá en 'ventana'
#boton1.pack(side="right",padx=15)

#PACK 'labelframe1' aparecerá en 'ventana'
#labelframe1.pack()

#------------------ORDEN_SALIDA_GRIDE---------------------------------------------------------------------------------------------

#GRIDE 'etiquet "n"' aparecerá en 'ventana' en (row=FILA,column=COLUMNA, padx=SEPARACION_EN_X, pady=SEPARACION_EN_Y)
#etiqueta2.grid(row=1,column=0,padx=0, pady=0)
#etiqueta1.grid(row=0,column=1,padx=0, pady=0)

#------------------ORDEN_SALIDA_PLACE---------------------------------------------------------------------------------------------
#PLACE 'etiquet "n"' aparecerá en 'ventana' en (x=COORDENADA_X, y=COORDENADA_y)
#etiqueta1.place(x=0,y=0)
#etiqueta2.place(x=200,y=0)

#PLACE 'etiquet "n"' aparecerá en 'ventana' en (relx=COORDENADA_RELATIVA_X, rely=COORDENADA_RELATIVA_Y)(RELATIVA AL CONTENEDOR 'ventana')
#etiqueta1.place(relx=0.0, rely=0.0)
#etiqueta2.place(relx=0.50, rely=0.50)


#Al objeto 'ventana' se le asigna un loop para que se mantenga abierto
ventana.mainloop()

#   (solo puedes usar un formato a la vez pack o grid o place)
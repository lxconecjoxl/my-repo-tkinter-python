#Importar la libreria 'tkinter' y renombrarla como 'tk'
import tkinter as tk

#Crea un nuevo objeto ventana
ventana = tk.Tk()

#Creamos un cuadro 'frame1' con (DONDE)
frame1 = tk.Frame(ventana)

#Creamos un cuadro 'frame2' con (DONDE)
frame2 = tk.Frame(frame1)

#Creamos un objerto 'boton1' con (DONDE, text="TEXTO")
boton1 = tk.Button(frame1, text="hoala mundo")

#Creamos un objerto 'lebelframe' con (DONDE, text="TEXTO", bg="COLOR", padx=10, pady=10)
labelframe1 = tk.LabelFrame(ventana, text="label", bg="orange3", padx=10, pady=10)

#------------------CONFIG_VENTANA----------------------------------------------------------------------------------------------

#Le da el nombre al encabezado de la ventana (colocar antes de jnerar el loop)
ventana.title("ventana")

#Asignamos un tamaño a 'ventana' estesificando ("ANCHOxALTO+CoordenadaHorizontal+CoordenadaVertical")
ventana.geometry("400x400+550+225")

#Asignamos un tamaño MINIMO a 'ventana' estesificando (ANCHO, ALTO)
ventana.minsize(400,400)

#Asignamos un tamaño MAXIMO a 'ventana' estesificando (ANCHO, ALTO)
ventana.maxsize(400,400)

#Avilitar o desavilitar la modificacion manual del tamaño del objeto 'ventana' (ALTO, ANCHO) True/Folse
ventana.resizable(True,True)

#Agregar un logo al objeto 'ventana'(el cual deve ser ina imagen y estar en la carpeta del proyecto y formato .ico)
ventana.iconbitmap("icono.ico")

#Cambiar color de fondo del objeto'ventana'
ventana.configure(bg="khaki")

#Cambiar nivel de opasidad del objeto 'ventana'
ventana.attributes("-alpha",1.0)

#------------------CONFIG_FRAME----------------------------------------------------------------------------------------------

#Asignamos las propiedades a 'frame1'(ANCHO, ALTO, COLOR, BORDE)
frame1.configure(width=300, height=300, bg="orange4", bd=1)

#Asignamos las propiedades a 'frame2'(ANCHO, ALTO, COLOR, BORDE)
frame2.configure(width=200, height=200, bg="orange2", bd=0)

#------------------CONFIG_BUTTON----------------------------------------------------------------------------------------------

#------------------CONFIG_LABEL----------------------------------------------------------------------------------------------

#Asignamos las propiedades a 'labelframe1'(ANCHO, ALTO)
labelframe1.config(width=200,height=200)

#------------------ORDEN_SALIDA----------------------------------------------------------------------------------------------

#'labelframe1' aparevera en 'ventana'
labelframe1.pack()

#'boton1' aparevera en 'frame1'
boton1.pack()

#'frame1' aparevera en 'ventana'
frame1.pack()

#'frame2' aparevera en 'frame1'
frame2.pack()

#Al objeto 'ventana' se le asigna un loop para que se mantenga abierto
ventana.mainloop()


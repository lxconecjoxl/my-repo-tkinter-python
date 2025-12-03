import tkinter as tk
import time

#Crea un nuevo objeto ventana
ventana = tk.Tk()

#Creamos un objerto 'boton1' con (DONDE)
etiqueta1 = tk.Label(ventana)

#------------------FUNCIONES----------------------------------------------------------------------------------------------

def reloj():
    #Cambiamos el texto de la etiqueta por la %H(HORA) - %M(MINUTOS) - %S(SEGUNDOS) gracias a la libreria  time
    etiqueta1.config(text=time.strftime("%H - %M - %S"))

    #Le damos un formato al texto
    etiqueta1.config(fg="snow", bg= "gray1",font=("Arial",54,"italic"))

    #Hacemos que la ventana se refresque cada 1 segundo
    ventana.after(1000,reloj)

#------------------CONFIG_VENTANA----------------------------------------------------------------------------------------------

#Le da el nombre al encabezado de la ventana (colocar antes de jnerar el loop)
ventana.title("ventana")

#Asignamos un tamaño a 'ventana' estesificando ("ANCHOxALTO+CoordenadaHorizontal+CoordenadaVertical")
ventana.geometry("380x90+550+225")

#Avilitar o desavilitar la modificacion manual del tamaño del objeto 'ventana' (ALTO, ANCHO) True/Folse
ventana.resizable(False,False)

#Cambiar color de fondo del objeto'ventana'
ventana.configure(bg="khaki")

#------------------ORDEN_SALIDA----------------------------------------------------------------------------------------------

#'etiqueta1' aparevera en 'ventana'
etiqueta1.pack()

#Llamo a la fincion 'reloj'
reloj()

#Al objeto 'ventana' se le asigna un loop para que se mantenga abierto
ventana.mainloop()

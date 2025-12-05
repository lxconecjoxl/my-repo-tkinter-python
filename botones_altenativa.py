import tkinter as tk

def on_click(event):
    print(f"{event.widget['text']} presionado")

ventana = tk.Tk()

buttons = [tk.Button(ventana, text=f"Botón {i}") for i in range(3)]

for button in buttons:
    button.pack()
    button.bind("<Button-1>", on_click)

ventana.mainloop()
import tkinter as tk
from tkinter import ttk
import json

with open('errores.json', 'r') as file:
    data = json.load(file)

def obtenerValor():
    entrada = entrada_texto.get()
    print(entrada)
    for error in data['errores']:
        if error['error'] == entrada:
            descripcion.config(text=error['desc'])
            break
        else:
            descripcion.config(text="")


#Crear la ventana
ventana = tk.Tk()
ventana.title("Busqueda de error")
 
titulo = ttk.Label(ventana, text="Ingresa el Codigo", font="Calibri 24")
titulo.pack(padx=10, pady=10)

entrada_texto = ttk.Entry(ventana)
entrada_texto.pack(padx=10, pady=10)

btn_buscar = ttk.Button(ventana, text= "Buscar Codigo", command=obtenerValor)
btn_buscar.pack(padx=10, pady=10)

descripcion = ttk.Label(ventana, text="")
descripcion.pack(padx=10, pady=10)

ventana.mainloop() #Va al Final



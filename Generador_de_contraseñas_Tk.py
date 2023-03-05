from tkinter import *
import random

root = Tk()
root.title("Contraseña aleatoria")
root.geometry('160x45')

def envia_boton():
    global contraseña
    letras = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    numeros = '1234567890'
    simbolos = "-_=+'/?,<.>!@#$%^&*(){[]}`~\|"
    union = f"{letras}{numeros}{simbolos}"
    longitud = 16
    resultado = random.sample(union, longitud)
    contraseña = "".join(resultado)
    obtencion = pantalla.get
    pantalla.delete(0, END)
    pantalla.insert(0, str(contraseña))

pantalla = Entry(root, width=25)
pantalla.grid(row=0)

boton1 = Button(root, 
                text="Generar contraseña aleatoria",
                bg="blue",
                fg="white",
                command=envia_boton).grid(row=1)

mainloop()
from json.tool import main
import tkinter as tk
from tkinter.messagebox import *

alpha = "abcdefghijklmnopqrstuvwxyz"

"""
if i ever wanna run on cmd again

def encrypt(cleartext):
    cyphertext = ""
    for char in cleartext:
        if char in alpha:
            newpos = (alpha.find(char) + 13) % 26
            cyphertext += alpha[newpos]
        else:
            cyphertext += char
    return cyphertext

cleartext = input("texto limpio: ")
cleartext = cleartext.lower()
print("texto encriptado:", encrypt(cleartext))

"""

#ventana
frame = tk.Tk()
frame.title("Encriptación de texto")
frame.geometry('400x200')
  
def encrypt():
    inp = inputtxt.get(1.0, "end-1c")
    cyphertext = ""
    for char in inp:
        if char in alpha:
            newpos = (alpha.find(char) + 13) % 26
            cyphertext += alpha[newpos]
        else:
            cyphertext += char
    lbl.config(text = "Texto encriptado: "+cyphertext)
  
#cuadro de texto
explicacion = tk.Text(frame, height=3, width=50)
inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20)

explicacion.pack()
explicacion.insert(tk.END, "Introduce el texto no encriptado para obtener el texto encriptado y viceversa")
inputtxt.pack()

  
#boton
printButton = tk.Button(frame,
                        text = "Obtener", 
                        command = encrypt)
printButton.pack()
  
#labels
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()

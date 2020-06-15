import tkinter as tk
from playsound import playsound
import time


def playNote(note, btn):
    playsound('sounds/mp3Notes/' + note + '.mp3')
    btn.config(state='disabled')
    btn.update()
    btn.config(state='normal')


root = tk.Tk()

root.title("Tuner")
root.geometry("200x200")

window = tk.Label(root, text="Notes")

window.pack()

btnA = tk.Button(text="A", command=lambda: playNote("a3", btnA))
btnA.pack()
btnB = tk.Button(text="B", command=lambda: playNote("b3", btnB))
btnB.pack()
btnC = tk.Button(text="C", command=lambda: playNote("c3", btnC))
btnC.pack()
btnD = tk.Button(text="D", command=lambda: playNote("d3", btnD))
btnD.pack()
btnE = tk.Button(text="E", command=lambda: playNote("e3", btnE))
btnE.pack()
btnF = tk.Button(text="F", command=lambda: playNote("f3", btnF))
btnF.pack()
btnG = tk.Button(text="G", command=lambda: playNote("g3", btnG))
btnG.pack()

root.mainloop()

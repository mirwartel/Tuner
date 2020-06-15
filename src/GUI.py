import tkinter as tk
from playsound import playsound


def playNote(note, btn):
    pitch = str(sPitch.get())
    path = 'sounds/mp3Notes/' + note + pitch + '.mp3'
    playsound(path)

    btn.config(state='disabled')
    btn.update()
    btn.config(state='normal')


root = tk.Tk()

root.title("Tuner")

h1 = tk.Label(text="Notes")
h2 = tk.Label(text="Pitch")

h1.pack()

btnA = tk.Button(text="A", command=lambda: playNote("a", btnA))
btnB = tk.Button(text="B", command=lambda: playNote("b", btnB))
btnC = tk.Button(text="C", command=lambda: playNote("c", btnC))
btnD = tk.Button(text="D", command=lambda: playNote("d", btnD))
btnE = tk.Button(text="E", command=lambda: playNote("e", btnE))
btnF = tk.Button(text="F", command=lambda: playNote("f", btnF))
btnG = tk.Button(text="G", command=lambda: playNote("g", btnG))

btnA.pack(side="left")
btnB.pack(side="left")
btnC.pack(side="left")
btnD.pack(side="left")
btnE.pack(side="left")
btnF.pack(side="left")
btnG.pack(side="left")
h2.pack()
sPitch = tk.Scale(from_=3, to=5)
sPitch.pack()

root.mainloop()

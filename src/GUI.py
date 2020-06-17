import tkinter as tk
from playsound import playsound
import recorder

recording = False
lastFqIn = ""
globals = globals()



def showFqIn(fq):
    h3.configure(text=fq)
    h3.update()

def rec():
    globals["recording"] = True
    while True:
        if recording:
            note = recorder.record()
            print(note)
            root.after(1, showFqIn(note))
        else:
            break


def stopRec():
    globals["recording"] = False
    print("stoping recording")


def playNote(note, btn):
    pitch = str(sPitch.get())
    path = 'sounds/mp3Notes/' + note + pitch + '.mp3'
    playsound(path)

    btn.config(state='disabled')
    btn.update()
    btn.config(state='normal')


root = tk.Tk()
root.geometry("500x500")

root.title("Tuner")

h1 = tk.Label(text="Notes")
h2 = tk.Label(text="Pitch")
h1.pack(anchor="nw", side="right")
h2.pack(anchor="w")



btnA = tk.Button(text="A", command=lambda: playNote("a", btnA))
btnB = tk.Button(text="B", command=lambda: playNote("b", btnB))
btnC = tk.Button(text="C", command=lambda: playNote("c", btnC))
btnD = tk.Button(text="D", command=lambda: playNote("d", btnD))
btnE = tk.Button(text="E", command=lambda: playNote("e", btnE))
btnF = tk.Button(text="F", command=lambda: playNote("f", btnF))
btnG = tk.Button(text="G", command=lambda: playNote("g", btnG))

btnA.pack(anchor="n", side="left")
btnB.pack(anchor="n", side="left")
btnC.pack(anchor="n", side="left")
btnD.pack(anchor="n", side="left")
btnE.pack(anchor="n", side="left")
btnF.pack(anchor="n", side="left")
btnG.pack(anchor="n", side="left")

sPitch = tk.Scale(from_=3, to=5)
sPitch.pack(anchor="nw", side="left", before=btnA)


h3= tk.Label(text="Last recorded note =")
h3.pack(side="right", after=h1 )

btnRec = tk.Button(text="r", command=lambda: rec())
btnStopRec = tk.Button(text="s", command=lambda: stopRec())

btnRec.pack(side="right")
btnStopRec.pack(side="right")

root.mainloop()

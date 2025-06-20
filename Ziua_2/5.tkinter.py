## ALIAS tk
import tkinter 

fereastra = tkinter.Tk()

## Business logic
def scrie_buna_dimineata():
    print("Buna dimineata")

## UI 
buton = tkinter.Button(fereastra, text="Salutare", command=scrie_buna_dimineata)
buton.grid()

counter = 1

label = tkinter.Label(fereastra, text=f"{counter}")
label.grid()

def incrementeaza():
    global counter
    counter += 1
    label.config(text=f"{counter}")

plus_buton = tkinter.Button(fereastra, text="+", command=incrementeaza)
plus_buton.grid()


fereastra.mainloop()


from tkinter import *
from tkinter import messagebox
import os
import time

window = Tk()
window.title('KeyLogin')
window.geometry('250x200')

def keylogin():
    eblan = float(entry.get())

    if eblan == 691272661:
        os.system('"BANDA.exe"')
    else:
        print('Не верный ключ')
        messagebox.showerror(title='Не верный ключ!', message='Не верный ключ! Программа закроется через 5 секунд!')
        time.sleep(5)
        exit()

entry = Entry()
entry.place(x = 60, y = 50)

btnl = Button(window, bg = 'black', fg = 'white', text = 'Подтвердить', command = keylogin)
btnl.place(x = 80, y = 75)

window.mainloop()
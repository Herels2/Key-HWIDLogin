import os
import time

eblan = float(input('Введите ключ: '))

if eblan == 216532852:
    os.system('"C:/Windows/System32/notepad.exe"')
else:
    print('Не верный ключ! Программа закроется через 5 секунд!')
    time.sleep(5)
    exit()
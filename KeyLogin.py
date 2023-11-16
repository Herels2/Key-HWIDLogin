import time
import requests
import os
import subprocess
import ctypes

ctypes.windll.kernel32.SetConsoleTitleA(b"KeyLogin")

print('')
print('    ██╗░░██╗███████╗██╗░░░██╗██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗')
print('    ██║░██╔╝██╔════╝╚██╗░██╔╝██║░░░░░██╔══██╗██╔════╝░██║████╗░██║')
print('    █████═╝░█████╗░░░╚████╔╝░██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║')
print('    ██╔═██╗░██╔══╝░░░░╚██╔╝░░██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║')
print('    ██║░╚██╗███████╗░░░██║░░░███████╗╚█████╔╝╚██████╔╝██║██║░╚███║')
print('    ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝')
print('')

key = input('Введи ключ: ')
url = requests.get('https://pastebin.com/XXXXXXXX')

try:
    if key in url.text:
        print('Верный ключ!')
        subprocess.call('BANDA.exe')
        time.sleep(5)
        exit()
    else:
        print('Не верный ключ!')
        time.sleep(5)
        exit()
except:
    print('Напиши разработчику в дискорд sterrist(Если не верный ключ НЕ пиши!)')
import subprocess
import time
import requests
import os

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('https://pastebin.com/XXXXXXXX')

try:
    if hwid in r.text:
        pass
    else:
        print('Ошибка, данный HWID не был найден в базе данных')
        print(f'HWID: {hwid}')
        time.sleep(5)
        os._exit()
except:
    print('Ошибка, не удаётся соединится с базой данных')
    time.sleep(5)
    os._exit()

print('Доступ разрешен')
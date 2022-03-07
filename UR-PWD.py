import os
import random
import time,sys
from colorama import Fore, Style


RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
END = '\033[0m'
print()

hola = "UR-PWD Generador de passwords"
time.sleep(1)
for l in hola:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(0.1)

print()
print()
time.sleep(2)
print("Iniciando UR-PWD... \033[0;32m[\033[0;m\033[1;31m0\033[0;m%\033[0;32m]\033[0;m\n")
time.sleep(0.4)
print("Iniciando UR-PWD... \033[0;32m[\033[0;m\033[1;31m10\033[0;m%\033[0;32m]\033[0;m\n")
time.sleep(0.4)
print("Iniciando UR-PWD... \033[0;32m[\033[0;m\033[1;31m20\033[0;m%\033[0;32m]\033[0;m\n")
time.sleep(0.4)
print("Iniciando UR-PWD... \033[0;32m[\033[0;m\033[1;31m30\033[0;m%\033[0;32m]\033[0;m\n")
time.sleep(0.4)
print("Iniciando UR-PWD... \033[0;32m[\033[0;m\033[1;31m40\033[0;m%\033[0;32m]\033[0;m\n")
time.sleep(0.4)
print("Iniciando UR-PWD... \033[0;32m[\033[0;m\033[1;31m50\033[0;m%\033[0;32m]\033[0;m\n")
time.sleep(0.4)
print("Iniciando UR-PWD... \033[0;32m[\033[0;m\033[1;31m60\033[0;m%\033[0;32m]\033[0;m\n")
time.sleep(0.4)
print("Iniciando UR-PWD... \033[0;32m[\033[0;m\033[1;31m70\033[0;m%\033[0;32m]\033[0;m\n")
time.sleep(0.4)
print("Iniciando UR-PWD... \033[0;32m[\033[0;m\033[1;31m80\033[0;m%\033[0;32m]\033[0;m\n")
time.sleep(0.4)
print("Iniciando UR-PWD... \033[0;32m[\033[0;m\033[1;31m90\033[0;m%\033[0;32m]\033[0;m\n")
time.sleep(0.4)
print("Iniciando UR-PWD... \033[0;32m[\033[0;m\033[1;31m100\033[0;m%\033[0;32m]\033[0;m\n")
time.sleep(0.6)
os.system("clear")


def banner():

    print("\n")                                                  
    print(RED + Style.NORMAL+"  /$$    /$$/$$$$$$$                /$$$$$$$  /$$       /$$ /$$$$$$$  ")           
    print(RED + Style.NORMAL+"  |$$   | $$| $$__  $$             | $$__  $$| $$  /$ | $$| $$__  $$ ")
    print(RED + Style.NORMAL+"  |$$   | $$| $$  \ $$             | $$  \ $$| $$ /$$$| $$| $$  \ $$ ")
    print(RED + Style.NORMAL+"  |$$   | $$| $$$$$$$/  /$$$$$$    | $$$$$$$/| $$/$$ $$ $$| $$  | $$ ")
    print(WHITE + Style.NORMAL+"  |$$   | $$| $$__  $$  |______/   | $$____/ | $$$$_  $$$$| $$  | $$ ")
    print(WHITE + Style.NORMAL+"  |$$   | $$| $$  \ $$             | $$      | $$$/ \  $$$| $$  | $$ ")
    print(WHITE + Style.NORMAL+"  |  $$$$$$/| $$  | $$             | $$      | $$/   \  $$| $$$$$$$/ ")
    print(WHITE + Style.NORMAL+"   \______/|__/   |__/             |__/      |__/     \__/|_______/  ")
    print()
print()
mensaje ='                  Genera una contraseña segura                 '   

time.sleep(1)
for l in mensaje:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(0.1)



banner()



print()
red = input("Password para: ")

from turtle import position
from tqdm.auto import tqdm
loop = tqdm(total = 70000, position=0,leave=False)
for k in range(70000):
    loop.set_description("Generando password...".format(k))
    loop.update(1)
loop.close()



lower = 'abcdefghijklmnñopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '<>[]{}@_-#$%&=?+?'
length = 25
all = lower + upper + numbers + symbols
password = "".join(random.sample(all,length))
print('\nNew password: \'\033[1;32m{} \033[0m\n'.format(password))

print(red,password, sep=' ', end='\n', file=open("passwords.txt", 'a'), flush=False)
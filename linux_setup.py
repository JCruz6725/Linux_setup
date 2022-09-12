import os
import time

pass = str(input('pass:'))
user = 'john'
os.system("useradd -p "+pass+" " + user)
time.sleep(2)
os.system("usermod -aG admin "+user+" ; usermod -aG sudo "+user)
os.system("su j")
os.system("sudo adduser xrdp ssl-cert")
os.system(pass)
os.system("sudo systemctl restart xrdp")
os.system(pass)
os.system("sudo apt install xfce4")
os.system(pass)


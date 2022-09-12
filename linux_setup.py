import os
import time


pas = str(input('pass:'))
user = 'john'

os.system("apt-get update")
os.system("useradd -p "+pas+" " + user)
os.system("usermod -aG admin "+user+" ; usermod -aG sudo "+user)
os.system("su j")
os.system("sudo adduser xrdp ssl-cert")
os.system(pas)
os.system("sudo systemctl restart xrdp")
os.system(pas)
os.system("sudo apt install xfce4")
os.system(pas)


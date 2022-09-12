import os
import time


pas = str(input('pass:'))
user = 'john'

os.system("apt-get update")
time.sleep(2)
os.system("useradd -p "+pas+" " + user)
time.sleep(2)
os.system("usermod -aG admin "+user+" ; usermod -aG sudo "+user)
time.sleep(2)
os.system("su "+user)
time.sleep(2)
os.system("sudo apt -y install xrdp")
time.sleep(2)
os.system("sudo adduser xrdp ssl-cert")
os.system(pas)
time.sleep(2)
os.system("sudo systemctl restart xrdp")
os.system(pas)
time.sleep(2)
os.system("sudo apt install xfce4")
os.system(pas)


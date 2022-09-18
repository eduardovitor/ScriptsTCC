import subprocess  
import os
from time import sleep

temp = subprocess.run("wapiti -u https://www.anadia.al.leg.br -f csv -o ~/teste.csv", shell=True)
sleep(5)

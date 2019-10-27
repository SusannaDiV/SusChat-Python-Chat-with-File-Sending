from __future__ import print_function
from ftplib import FTP
from termcolor import colored

import os
import time
import random
from progress.bar import (FillingSquaresBar,PixelBar)
from dotenv import load_dotenv
load_dotenv(dotenv_path='settings.ini')

TEMP=colored("REMEMBER","red")
print(" (Cmptr): "+TEMP+": You can only exchange files between two users!")
global flnm
flnm=""
def sleep():
    t = 0.1
    t += t * random.uniform(-0.2, 0.2)  
    time.sleep(t)

def dwnldfile():
    ftp=FTP(os.getenv('FTP_HOST', None))
    ftp.set_pasv(True)
    ftp.login(user=os.getenv('FTP_USER', None),passwd=os.getenv('FTP_PASS', None))
    ftp.cwd(os.getenv('FTP_DIR', None))
    
    filename=input(colored(" (Cmptr): Name of the file: ","yellow"))
    time.sleep(0.3)
        
    suffix = '%(index)d/%(max)d [%(elapsed)d / %(eta)d / %(eta_td)s]'
    bar = FillingSquaresBar(" (Cmptr): Downloading your file :) ", suffix=suffix)
    for i in bar.iter(range(100)):
        sleep()

    localfile=open(filename,'wb')
    ftp.retrbinary('RETR '+filename,localfile.write,1024)
    print(" ")
    time.sleep(0.9)
    print(colored(" (Cmptr): Your file has finished downloading! :D ","yellow"))
    ftp.quit()
    localfile.close()
    
 
def uploadfile():
    ftp=FTP(os.getenv('FTP_HOST', None))
    ftp.set_pasv(True)
    ftp.login(user=os.getenv('FTP_USER', None),passwd=os.getenv('FTP_PASS', None))
    ftp.cwd(os.getenv('FTP_DIR', None))
    
    filename = input(colored(" (Cmptr): Name of the file: ","yellow"))
    flnm=filename
    time.sleep(1)
    if os.path.isfile(filename):
        print("")
        print(" (Cmptr): The dimensions of the file are: ",str(os.path.getsize(filename)))
        asw=input(colored(" (Cmptr): Are you sure you'd like to send {} (y/n): ".format(filename),"yellow"))
        if asw=='y':
            
            suffix = '%(index)d/%(max)d [%(elapsed)d / %(eta)d / %(eta_td)s]'
            bar = PixelBar(" (Cmptr): Uploading your file :) ", suffix=suffix)
            for i in bar.iter(range(100)):
                sleep()
            
            ftp.storbinary('STOR '+filename, open(filename, 'rb'))
            time.sleep(1.2)
            print("")
            print(colored(" (Cmptr): Your file has been uploaded! :D ","white"))
            ftp.quit()
            return flnm
        else:
            print(" (Cmptr): No worries, chat away! :D ")
            ftp.quit()
    else:
        print(" (Cmptr): Sorry, there is no such file as {} .".format(filename))

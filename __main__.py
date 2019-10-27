from __future__ import print_function, unicode_literals
import os
import styles 
import sys
import getpass
from PyInquirer import style_from_dict, Token, prompt
import time
import authentication
from termcolor import colored,cprint
from pyfiglet import Figlet
from pusher import Pusher
import pysher
from dotenv import load_dotenv
import json
import pychatrooms
import getpass
import random
from progress.bar import FillingCirclesBar
from progress.bar import Bar
from os import path

load_dotenv(dotenv_path='settings.ini')

class SusChat():
    pusher=None
    channel=None
    answ=None
    clientPusher=None
    user=None
    users=dict()
    temp_data=authentication.searchuser_password()
    for i in range(len(temp_data)):
        users[temp_data[i][0]]=temp_data[i][1]
    
    chatrooms=[]
    chatrooms=pychatrooms.all_rooms()
    temp_dir=os.getcwd()
    if path.isdir("SusChat_Downloads")==True:
        pass
    else:
        os.system('mkdir SusChat_Downloads')
    if path.isdir('SusChat_Uploads')==True:
        pass
    else:
        os.system('mkdir SusChat_Uploads')
    os.chdir(temp_dir)
    platforms = {'win32' : 'Windows'}
    if sys.platform not in platforms:
        plat=sys.platform
    else:
        plat=platforms[sys.platform]
    value_plat=False

    def clear(self):
        if self.value_plat==True:
            os.system('clear')
        else:
            os.system('cls')
        


    def sleep(self):
        t = 0.02
        t += t * random.uniform(-0.2, 0.2)
        time.sleep(t)
        
    def welcome(self):
        cprint("             Hello there friend!",'red',attrs=['bold'],file=sys.stderr)
        time.sleep(0.1)
        cprint(" Welcome to Secure SusChat Server!",'red',attrs=['bold'],file=sys.stderr)
        print("")
        print("")
        
    def logincred(self):
        style = style_from_dict({
        Token.QuestionMark: '#E91E63 bold',
        Token.Selected: '#00FFFF',
        Token.Instruction: '', 
        Token.Answer: '#2196f3 bold',
        Token.Question: '#7FFF00 bold',
        })
        
    
        time.sleep(0.4)
        questions=[ 
            {
                'type':'list',
                'name':'log',
                'message':'Select what do you want to do:',
                'choices': ['Login','Sign In','Exit'],
                'default':'Login'
            }
        ]

        answers=prompt(questions,style=style)

        self.clear()
        time.sleep(0.05)
        print("")
        os.system("cls")
        styles.prLightPurple("connected")
        time.sleep(0.3)
        self.clear()

        styles.prLightPurple("-+-+-+-+-+-+-+-+-+-+-+")
        styles.prLightPurple("-+       Login      +-")
        styles.prLightPurple("-+-+-+-+-+-+-+-+-+-+-+")
        print(" ")
        user1=dict()
        temp_data=authentication.searchuser_password()
        for i in range(len(temp_data)):
                user1[temp_data[i][0]]=temp_data[i][1]
        self.users=user1
        

        if answers['log']=='Login':
            username=input(" Your username is: ")
            password=getpass.getpass(" Your password is: ")
            time.sleep(0.1)
            print("")
            
            s="-"
            sys.stdout.write( ' Logging-in! :) ' )
            i=0
            while i<=10:
                sys.stdout.write( s )
                sys.stdout.flush()
                time.sleep(0.1)
                i=i+1
            
            print("")
            time.sleep(0.37)

            if username in self.users:
                if self.users[username]== password:
                    self.user=username
                    print("")
                    cprint(" You're logged-in ","green")
                    time.sleep(0.3)

                else:
                    cprint(" Your password is invalid :( )","red")
                    print(" ")
                    time.sleep(0.56)
                    self.clear()
                    self.logincred()
            else:
                cprint(" Your username is invalid ;( )","red")
                print("")
                time.sleep(0.56)
                self.clear()
                self.logincred()


        elif answers["log"]=="SignIn":
            name=input(" Your name is: ")
            username=input(" Choose an username: ")
            password=getpass.getpass(" Choose a password: ")
            uniqid=name+random.choice(["q","@","%","w","r","g","hg","crate","traitor","aligator","unknw","@@@@@","&&&&","###"])+username
            checker=authentication.register(uniqid,name,username,password)
            time.sleep(0.95)
            cprint(" You have been successfully registrated to the Secure SusChat Server, hooray!","yellow")
            time.sleep(1)
            self.logincred()
        
        elif answers['log']=='Exit':
            print("")
            print(" Closing! Bye bye")
            time.sleep(0.2)
            self.clear()
            sys.exit(1)



    def chatselector(self):
        
        chatroom=input(" Enter the SusChat chatroom name you want to join: ")
    
        if chatroom in self.chatrooms:
            print("")
        else:
            cprint(" You've succesfully created a new SusChat chatroom! Good luck!","red")
            time.sleep(1)
            pychatrooms.new_room(chatroom,0)
            print("")
            self.clear()
            


        chatrooms=pychatrooms.all_rooms()
        self.chatrooms=chatrooms

        if chatroom in self.chatrooms:
            self.chatroom=chatroom
            self.initPusher()
            self.clear()
            cprint(" Chatroom name: {}".format(self.chatroom),"green")
            print("")
        else:
            cprint(" There is no SusChat chatroom with the name you entered :( )")
            print("")
            time.sleep(0.2)
            self.clear()
            self.chatselector()    


    ''' Server Side '''
    def initPusher(self):
        self.pusher = Pusher(app_id=os.getenv('PUSHER_APP_ID', None), key=os.getenv('PUSHER_APP_KEY', None), secret=os.getenv('PUSHER_APP_SECRET', None), cluster=os.getenv('PUSHER_APP_CLUSTER', None))
        self.clientPusher = pysher.Pusher(os.getenv('PUSHER_APP_KEY', None), os.getenv('PUSHER_APP_CLUSTER', None))
        self.clientPusher.connection.bind('pusher:connection_established', self.connectHandler)
        self.clientPusher.connect()
    
    def connectHandler(self, data):
        self.channel = self.clientPusher.subscribe(self.chatroom)
        self.channel.bind('newmessage', self.pusherCallback)

    def pusherCallback(self, message):
        from playsound import playsound
        formate="["+self.user+"]: "
        message = json.loads(message)
        if message['user'] != self.user:
            print(colored("({}): {}".format(message['user'], message['message']), "yellow"))
            print(colored(formate,"red"))
    
    def getInput(self):
        
        formate="["+self.user+"]: "
        message = input(colored(formate,"red"))
        if message=="send file" or message=="sdf":
            import filestransfer
            os.chdir(os.getcwd()+'\\SusChat_Uploads')
            time.sleep(0.5)
            print("")
            os.system('dir')
            print("")
            flt=filestransfer.uploadfile()
            message=formate+"file is uploaded.[filename = {}]".format(flt)
            os.chdir(self.temp_dir)
        if message=='download file' or message=='ddf':
            os.chdir(os.getcwd()+'\\SusChat_Downloads')
            import filestransfer
            filestransfer.dwnldfile()
            os.chdir(self.temp_dir)
            message="........."
        if message=='exit':
            self.clear()
            self.main()
        if message=='open file':
            os.chdir(os.getcwd()+'\\SusChat_Downloads')
            fl=input(" (Cmptr): filename -> ")
            os.system(fl)
            os.chdir(self.temp_dir)
            message="......."
        self.pusher.trigger(self.chatroom, u'newmessage', {"user": self.user, "message": message})


    def main(self):


        style = style_from_dict({
        Token.QuestionMark: '#E91E63 bold',
        Token.Selected: '#00FFFF',
        Token.Instruction: '', 
        Token.Answer: '#2166f3 bold',
        Token.Question: '#7FFF10 bold',
        })

        self.clear()
        self.welcome()

        qus=[
            {
                'type':'list',
                'name':'choice',
                'message':'Enter :',
                'choices':['Start chatting','Quit'],
                'default':'start chat'

            }
        ]

        answer=prompt(qus,style=style)

        if answer['choice']=='Start chatting':
                
            self.logincred()
            time.sleep(1)
            self.clear()
            self.chatselector()
            
            while True:
                self.getInput()

        elif answer['choice']=='Quit':
            print("")
            print(" Closing! Bye bye! ")
            time.sleep(0.2)
            self.clear()
            sys.exit(1)

def mainload():
    SusChat().main()

if __name__=="__main__":
    SusChat().main()

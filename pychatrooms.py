from dotenv import load_dotenv
import mysql.connector
import os
load_dotenv(dotenv_path='settings.ini')

'''YOUR DATABASE DETAILS'''
chatroom_serv=mysql.connector.connect(
    host=os.getenv('SQL_HOST', None),
    user=os.getenv('SQL_USER', None),
    passwd=os.getenv('SQL_PASSWORD', None),
    database=os.getenv('SQL_DATABASE', None)
)

rooms=chatroom_serv.cursor()

def all_rooms():
    room_list=[]
    rooms.execute("SELECT server_rooms FROM chatserver")
    chat_rooms_list=rooms.fetchall()
    for i in range(len(chat_rooms_list)):
        room_list.append(chat_rooms_list[i][0])
    return room_list

def new_room(room_name,idt):
    sql= "INSERT IGNORE INTO chatserver (server_rooms,id) VALUE (%s,%s)"
    val=(room_name,idt)

    rooms.execute(sql,val)
    chatroom_serv.commit()
    
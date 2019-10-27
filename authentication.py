from dotenv import load_dotenv
import mysql.connector
import os
load_dotenv(dotenv_path='settings.ini')

user_db=mysql.connector.connect(
    host=os.getenv('SQL_HOST', None),
    user=os.getenv('SQL_USER', None),
    passwd=os.getenv('SQL_PASSWORD', None),
    database=os.getenv('SQL_DATABASE', None)
)

user_details=user_db.cursor()

def register( user_idf,name,username,passwd):

    sql="INSERT INTO user (user_id,name,username,passwod) VALUES (%s, %s, %s, %s)"
    val=(user_idf,name,username,passwd)
    
    try:
        user_details.execute(sql,val)
        user_db.commit()
        return 0
    except:
        return 1

def login(usrname,passwd):

    user_details.execute("SELECT username,passwod FROM user")
    result=user_details.fetchall()
    chk=0
    for i in range(len(result)):
        temp=[]
        temp=result[i]
        
        if temp[0]==usrname and temp[1]==passwd:
            chk=chk+1
        else:
            pass
    if chk>0:
        return 0
    else:
        return 1

def searchuser_password():

    user_details.execute("SELECT username,passwod FROM user")
    userinfo=user_details.fetchall()
    return userinfo

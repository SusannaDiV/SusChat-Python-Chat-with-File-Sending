# SusChat-Python-Chat-with-File-Sending
**CLI Python Chat program with user registration in MySQL and ability to transfer any files between 2 users**

Install all required modules (mysql-connector-python, pyfiglet, progress, wheel, PyInquirer, pusher, pysher, python-dotenv) with the command:
pip install progress python-dotenv pysher pusher termcolor mysql-connector-python wheel PyInquirer pyfiglet playsound

Pusher:
Pusher is a hosted service that makes it super-easy to add real-time data and functionality between applications, and I added it as a real-time messages layer between chatroom clients in the message transfering system.

dotenv:
Tried to make it more responsive and easier to deploy in any machine - thats the reason behind my choice of creating a single settings.ini in my project which is responsible for its tweaks, like MySQL access details, FTP credentials etc.

progress:
The progress library helped my add some fancy-looking loading bars.

FTP (ftplib):
Transmiting files directly with a TCP stream was a very messy task when it came to file extensions, so instead I used an FTP server (The File Transfer Protocol, a standard network protocol used for the transfer of computer files between a client and server on a computer network) to host files.

MySQL:
SusChat uses a SQL database to save the credentials of users and log the chatroom names.

**Project Files Description**
This project is made up of 5 main files (and a setting.ini to facilitate changes - and implementing some basic information hiding):
1. the __main__.py which is responsible to run theat chat app. Here I created a class with the name SusChat() that encapsulates all the required function like login, sign up, chatroom selection etc.
2. authentication.py which is resposible for all the authetication aspects (dealing with the registration, login sql queries and consequentially username and password searching in the database) 
3. filestransfer.py which manages the file transfer (with functions to upload and download on the FTP server)
4. pychatrooms.py which manages the chatroom selection and creation (dealing with the corresponding sql search and creations in chatserver)
5. styles.py which has functions for printing text in different colours (credit to: https://www.geeksforgeeks.org/print-colors-python-terminal/) 

**In order to successfully upload and download files to and from the FTP server, write "send file" or "sdf" and "download file" or "ddf".**

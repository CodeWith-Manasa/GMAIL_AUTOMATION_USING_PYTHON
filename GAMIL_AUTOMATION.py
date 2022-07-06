'''GMAIL AUTOMATION USING PYTHON
where we send mails by receiving user voice as an instructions.
used libraries are
    smtplib-->used for sending mail to any internet machine
    pyttsx3-->used to convert user voice instructions to text
    email.message-->used to send mails with HTML content and attachments .
    sppech_recognition--> used for ability to listen to  spoken words and identifying them.
    os--> os module include many functions to interact with the file system
    tkinter-->the python interface to TK,which is the GUI toolkit for Tcl/TK
    filedialog-->it is used for file selection
    imghdr-->determines the type of image contained in a file or byte stream

            WORKING.
                In this we are storing all the email id's in the dictionary and we are labeling their respective keys.
                then we are allowing user to say the keys for whome
                 the user want to send email.
                here we are taking user voice as an instruction and based on the key found in dictionary we are
                retrieve the mail id's then we allow user to speak the text for subject section next for the body then
                 attachement to the mail. then finally we send the email...

'''
import smtplib                          # importing smtplib
import pyttsx3                          # importing pyttsx3
from email.message import EmailMessage  # Importing email.message library
import speech_recognition as sr         # importing speech_recognition library
import os                               # importing os module
from tkinter import *                   # importing tkinter module
from tkinter import filedialog          # importing filedialog
a=Tk()                                  #it helps to display the root window and manages all the other components of tkinter application
attachments=[]                          #declaring list
listener = sr.Recognizer()              # Creates a new Recognizer instance,which represents a collection of speech recognition functionality
engine = pyttsx3.init()                 # reference for pyttsx3 constructor
email = EmailMessage()                  # it is the base class for the email object model
server = smtplib.SMTP('smtp.gmail.com', 587)  # This class manages a connection to an SMTP or ESMTP server
server.starttls()  # Puts the connection to the SMTP server into TLS mode.
def login():
    try:
        server.login('tondurmanasa@gmail.com', 'znlohnfxetyaxcnc')  # logging to the user email
    except:
        talk("invalid password or id .....try again")
        login()

def talk(text):
    engine.say(text)  # speak out the input text
    engine.runAndWait()  # Function make the speech audible in the system.


import speech_recognition as sr  # importing speech_recognition library

listener = sr.Recognizer()  # Creates a new Recognizer object, which represents a collection of speech recognition functionality


def get_info():
    try:
        with sr.Microphone() as source:  # Creates a new Microphone object, which represents a physical microphone on the computer
            print('listening....')
            voice = listener.listen(source,
                                    phrase_time_limit=15)  # listening to the spoken text for time limit of 15 sec
            info = listener.recognize_google(voice)  # using google recognizer for detecting the spoken words
            print(info)
            return info.lower()
    except:
        pass

def get_attachment():
    filename= filedialog.askopenfile(initialdir='C:/', title='select a file') #opening c drive
    if filename:
        filepath = os.path.abspath(filename.name)          #storing path of the selected file in filepath variable
        print(filepath)
    attachments.append(filepath)                       #appending filepath to list
    for filename in attachments:                         #storing filename
        filetype = filename.split('.')
        filetype = filetype[1]  # storing type of the file or image
        print(filetype)
        if filetype == "jpg" or filetype == "JPG" or filetype == "png" or filetype == "PNG" or filetype=='jpeg':
            import imghdr  # importing imghdr
            with open(filename, "rb") as f:  # opening the image
                file_data = f.read()  # reading the image
                image_type = imghdr.what(filename)  # determining type of the image
            email.add_attachment(file_data, maintype='image', subtype=image_type,
                                 filename=f.name)  # attaching photo to email
        if filetype == "pdf" or filetype == "PDF" or filetype=="txt" or filetype=="docx" or filetype=="pptx" or filetype=="zip":
            with open(filename, 'rb') as f:  # opening the file
                file_data = f.read()  # reading data from file
                file_name = f.name
            email.add_attachment(file_data, maintype='application', subtype='octet-stream',
                                 filename=file_name)  # attaching file to email
def attach_file():
    try:
        talk('Do you want to attach any photo or document')
        check = get_info()
        if 'yes' or 'ok' in check:
            Button(text='open file', width=20, command=get_attachment, bg='#8EE5EE',
                   font=('Times New Roman', 16)).pack()  # adding buttons in a python application
            Button(text='close', width=10, command=a.quit, bg='#EE0000', font=("Times New Roman", 16)).pack()
            a.mainloop()  # telling python to run the Tkinter event loop
    except:
        talk("Sorry!!! couldnt Recognize Please try again")
        attach_file()


def send_email(receiver, subject):
    email['From'] = 'tondurmanasa@gmail.com'                # from address of user
    email['To'] = receiver                                  # receiver address
    email['Subject'] = subject                              # mentioning the subject of email
    server.send_message(email)                              # sending the email


email_list = {
    "mca": "21352065@pondiuni.ac.in,21352025@pondiuni.ac.in"}  # listing the email address of receiver in a dictionary


def get_email_info():
    login()
    talk('to whom you want to send mail')                   # talking to the user
    name = get_info()                                       # calling the getinfo method
    while (name not in email_list.keys()):
        talk("NAME NOT FOUND PLEASE TRY AGAIN!!!")
        name = get_info()                                   # if keys not found in dictionary  calling the get_info
    receiver = email_list[name]                             # accessing the key of dictionary for corresponding receiver
    print(receiver)
    talk('what is the subject of your mail')
    subject = get_info()                                    # getting the subject from user
    talk('tell me the text in your email')
    message = get_info() # getting the message from user
    email.set_content(message)                              # mentioning the body of email
    attach_file()
    send_email(receiver, subject)                           # calling the send_email method


get_email_info()
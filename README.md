# GMAIL_AUTOMATION_USING_PYTHON

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

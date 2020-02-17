import pyttsx3
from googlesearch import search
import random
import webbrowser
import datetime
import time
import trail
import smtplib


#starting the engine to talk
engine = pyttsx3.init()

#slowing the speech rate
engine.setProperty("rate",140)

#acquring the current time
now = datetime.datetime.now()

name = input("Enter your name:")



cmd = list()
reply = ["hi","hello","hi there","glad to meet you","hey","hi hope you are having a good day","good to see you","hola"]
index =0
i = ""
lst = list()

def timing():
    if now.hour > 20 and now.hour <= 24:
        engine.say("Good night "+name+" , sweet dreams")
        engine.runAndWait()
        print("Good night",name)

    elif now.hour >= 12 and now.hour < 16:
        engine.say("Good afternoon "+name)
        engine.runAndWait()
        print("Good afternoon",name)

    elif now.hour >= 16 and now.hour < 20:
        engine.say("Good evening "+name)
        engine.runAndWait()
        print("Good evening",name)

    elif now.hour >= 0 and now.hour < 12:
        engine.say("Good morning "+name)
        engine.runAndWait()
        print("Good morning",name)

    else:
        engine.say("Something went wrong...")
        print("Something went wrong..")
    


timing()
while i != "bye":

    
    command = input("\nListening....\n")
    
    command = command.lower()
    
    cmd = command.split(" ")

    if command == "you there" or command == "you online":
        engine.say("Always at your service sir")
        print("Always at your service sir..")
        
    #features of chatbot
    if command == "what all things can you do" or command == "what are your features":
        engine.say("Well I can perform many tasks which include...")
        print("Well I can perform many tasks which include...")
        print("* Greeting users")
        print("* Performing simple calculations")
        print("* Making note of complaints")
        print("* Sending emails")
        print("* Calling")
        print("* Messaging...")
        engine.say("Greeting users, Performing simple calculations, making not of complaints, sending emails, calling, messaging")


    if command == "bye":
        engine.say("bye "+name+",, hope you have a good day")
        engine.runAndWait()
        
    #About creator
    if command == "who is your creator" or command == "who is your inventor":
        engine.say("My creator are, students from I S E ")
        engine.runAndWait()
    
    
    for i in cmd:

        #Complaint register
        if i == "problem" or i == "compliant" or i == "issue":
            complaint = input("Describe your complaint :")
            engine.say("Thank you! we will see to it")
            print("Thank you! we will see to it...")
            
        #User greeting
        if i == "hi" or i == "hello" or i == "hey":
            index = random.randint(0, 7)
            engine.say(reply[index])
            engine.runAndWait();
            print(reply[index])
            
        #Calculator    
        if i == "calculator" or i== "calculate":
            exp = input("Enter the expression:")
            print(eval(exp))
            engine.say("your answer is "+ str(eval(exp)))
        
        if i == "night" or i == 'morning' or i == 'evening' or i == 'afternoon':
            timing()

        #Web search    
        if i == "search":
            
            print("what r u looking for ?")
            engine.say("what r u looking for ?")
            engine.runAndWait()
            find = input()
            aa = search(
                find,
                tld = 'co.in',
                num = 1,
                start = 1,

                stop = 1,
                pause = 3.0,
                )
            cpath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(cpath))

            i = 'https://simple.wikipedia.org/wiki/'+ find
            webbrowser.get('chrome').open_new(i)
        #Reminder
        if i == 'remember':
            r = input('Listening...')
            re = r.split()
            f = open('remember.txt','a')
            f.write('\n')
            f.write('* ')
            f.write(r)

            print("Ok. I'll remember it.")
            engine.say("Ok. I'll remember it.")
            engine.runAndWait()
            
            break
        
        if i == "remind":
            f = open('remember.txt','r')
            print(f.read())

            c = input("Enter c and press enter to clear reminder:")
            if c == 'c':
                f = open("reminder.txt",'w')
                f.write('')
        #Calling        
        if i == "call":
            
            fh = open("contacts.txt")
            print("\n")
            for line in fh:
                print(line.rstrip())

            engine.say("Who do you want to call")
            engine.runAndWait()
            contact = input("\nEnter name or number:")

            fh = open("contacts.txt")
            for line in fh:
                if contact in line.split():
                    engine.say("calling "+contact)
                    print("\ncalling",contact,"...")
        #messaging
        if i == "message":

            fh = open("contacts.txt")
            print("\n")
            for line in fh:
                print(line.rstrip())

            engine.say("Who do you want to message.")
            engine.runAndWait()
            contact = input("\nEnter name or number:")
            engine.say("What is the message")
            engine.runAndWait()
            message = input("\nEnter the message:")

            fh = open("contacts.txt")
            
            for line in fh:
                if contact in line.split():
                    engine.say("message sent to "+contact)
                    print("message sent to",contact,"..")

                    msg = open("message.txt","a")
                    msg.write("\n*")
                    msg.write(message)
                    print("done")

        if i == "send_mail":

            mail = smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login(trail.sender,trail.password)

            fh = open("emails.txt")
            print("\n")
            for line in fh:
                print(line.rstrip())

            engine.say("Who do you want to email.")
            engine.runAndWait()
            recipient = input("\nEnter name or email address:")
            
            engine.say("What is the subject")
            engine.runAndWait()
            subject = input("\nEnter the subject:")

            engine.say("What is the content")
            engine.runAndWait()
            content = input("\nEnter the content:")

            fh = open("emails.txt","r")
            
            for line in fh:

                lst = line.split(":")
                if recipient in line.split():
                    header = "To :" + lst[1] + "\n" + "From :" + trail.sender + "\n" + "subject :"+ subject + "\n"
                    content = header + content
                    mail.sendmail(trail.sender,lst[1],content)
                    mail.close()

            fh = open("emails.txt")
            
            for line in fh:
                if recipient in line.split():
                    engine.say("email sent to "+ recipient)
                    print("email sent to",recipient,"..")

                    msg = open("message.txt","a")
                    msg.write("\n*")
                    msg.write(content)
                    print("done")

        engine.runAndWait()            
            
            
                
            
                
                
                
            

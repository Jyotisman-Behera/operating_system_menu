import os

import pyttsx3                                                                #To speak out the lines                                         

from datetime import datetime  						      #To get current date and time

print("\n----WELCOME TO WINDOWS ASSISTANT----",end="")                                   		
pyttsx3.speak("WELCOME TO WINDOWS ASSISTANT")

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("\t\t\t\t\t\tDate and Time :", dt_string)
pyttsx3.speak("Here is today's date and time")

print("\nHello , I am here for you ,(To turn me off please enter CTRL + C ) OR 	Enter EXIT")
pyttsx3.speak("Hello , I am here for you ,(To turn me off please enter CTRL + C ) or enter exit")

while True:                                                                    #Loop to ask the user infinite time ,till he interrupt
   
    print("\nPlease ask me what can i do for you : ",end="")
    pyttsx3.speak("Please ask me what can i do for you")
    user = input()
    todo = user.lower()                                                 
    

    if "dont" in todo or "do not " in todo :                                    #Checking whether anything mentioned not to do
        print("OK ,Tell me the next command .")
        pyttsx3.speak("OK Tell me the next command")
    

    elif "open" in todo or "launch" in todo or "run" in todo or "zoom" in todo or "want" in todo or "play" in todo or "take" in todo or "navigate" in todo or "show" in todo or "what" in todo or "date" in todo or "time" in todo:
        

        if "magnifier" in todo or "zoom" in todo or "enlarge" in todo:                   #check command for Magnifier
            print("Opening Magnifier")
            pyttsx3.speak(" Opening Magnifier ")
            os.system("magnify")

        elif "time" in todo:                                                             #Check command for time
            now1 = datetime.now()
            tonly = now1.strftime("%H:%M:%S")
            pyttsx3.speak(" Here is the time ")
            print("Time :", tonly)

        elif "date" in todo:                                                             #Check command for date
            now2 = datetime.now()
            donly = now2.strftime("%d/%m/%Y")
            pyttsx3.speak("Here is the date")
            print("Date :",donly)

        elif "camera" in todo or "shot" in todo:                                         #Check command for Camera
            print("Opening System Camera")
            pyttsx3.speak(" Opening System Camera ")
            os.system("start microsoft.windows.camera:")

        elif "powerpoint" in todo or "ppt" in todo or "presentation" in todo:            #Check command for MS-Powerpoint
            print("Opening MS Powerpoint")
            pyttsx3.speak(" Opening MS Powerpoint ")
            os.system("start powerpnt")

        elif "excel" in todo or "sheet" in todo or "work" in todo:                       #Check command for MS-Excel
            print("Opening MS Excel")
            pyttsx3.speak(" Opening MS Excel ")
            os.system("start excel")

        elif "winword" in todo or "msword" in todo:                                      #Check command for MS-Word
            print("Opening MS Word")
            pyttsx3.speak(" Opening MS Word ")
            os.system("start winword")

        elif "command" in todo or "prompt" in todo :                                     #Check command for command prompt
            print("Opening Command Prompt")
            pyttsx3.speak(" Opening command prompt ")
            os.system("start cmd")

        elif "powershell" in todo or "shell" in todo :                                   #Check command for windows powershell
            print("Opening Windows Powershell")
            pyttsx3.speak(" Opening Windows Powershell ")
            os.system("start powershell")
             
        elif "info" in todo or "detail" in todo :                                        #Check command for system details
            print("Opening System Detail Information")
            pyttsx3.speak(" Opening System Detail Information ")
            os.system("systeminfo")
        
        elif "configuration" in todo :                                                   #check command for system configuration
            print("Opening System Configuration")
            pyttsx3.speak(" Opening System Configuration")
            os.system("msconfig")
        
        elif "computer" in todo or "pc" in todo or "file" in todo:                       #Check command for files
            print("Opening This PC")
            pyttsx3.speak(" Opening This PC")
            os.system("explorer")
        
        elif "word" in todo or "wordeditor" in todo or "write" in todo:                  #Check command for wordpad
            print("Opening Wordpad")
            pyttsx3.speak(" Opening Wordpad ")
            os.system("write")
        
        elif "calculator" in todo or "calculate" in todo:                                #Check command for calculator
            print("Opening Calculator")
            pyttsx3.speak(" Opening Calculator ")
            os.system("calc")
        
        elif "facebook" in todo or "fb" in todo :                                        #Check command for facebook
            print("Lauching Facebook in Google Chrome")
            pyttsx3.speak(" Launching Facebook in Google Chrome ")
            os.system("chrome www.facebook.com")

        elif "gmail" in todo or "email" in todo :                                        #Check command for gmail 
            print("Opening Gmail in Google Chrome")
            pyttsx3.speak("Opening G mail in Google Chrome ") 
            os.system("chrome www.gmail.com")

        elif "whatsapp" in todo or "wp" in todo:                                         #Check command for Whatsapp
            print("Opening Whatsapp Web in Google Chrome")
            pyttsx3.speak("Opening Whatsapp Web in Google Chrome")
            os.system("chrome web.whatsapp.com")

        elif "youtube" in todo or "yt" in todo or "utube" in todo:                       #Check command for Youtube
            print("Opening Youtube in Google Chrome")
            pyttsx3.speak("Opening Youtube in Google Chrome")
            os.system("chrome www.youtube.com")

        elif "map" in todo or "navigate" in todo or "direction" in todo:                 #Check command for google maps 
            print("Opening Google Maps in Google Chrome")
            pyttsx3.speak("Opening google maps in Google Chrome ")
            os.system("chrome maps.google.com")

        elif "class" in todo or "academic" in todo:                                      #Check command for google classroom
            print("Taking you to Google Classroom in Google Chrome")
            pyttsx3.speak(" Taking you to Google Classroom in Google Chrome")
            os.system("chrome classroom.google.com")

        elif "meet" in todo or "Gmeet" in todo :                                         #Check command for google meet       
            print("Launching Google meet in Google Chrome ")
            pyttsx3.speak(" Launching Google meet in Google Chrome ")
            os.system("chrome meet.google.com")

        elif "call" in todo or "video" in todo or "duo" in todo :                        #Check command for duo for calling
            print("Opening Google Duo in Google Chrome")
            pyttsx3.speak(" Opening Google Duo in google chrome")
            os.system("chrome duo.google.com")

        elif "contact" in todo or "phonebook" in todo :                                  #Check command for contact list
            print("Opening contact in Google Chrome")
            pyttsx3.speak(" Opening contact in Google Chrome ") 
            os.system("chrome contacts.google.com")

        elif "news" in todo or "headline" in todo :                                      #Check command for news
            print("Showing you today's breaking news in Google Chrome")
            pyttsx3.speak("Showing you today's breaking news in Google Chrome")
            os.system("chrome news.google.co.in") 

        elif "calender" in todo :                                                        #Check command for Calender
            print("Opening Calender in Google Chrome")
            pyttsx3.speak(" Opening Calender in Google Chrome ")
            os.system("chrome calendar.google.com")       
       
        elif "note" in todo or "editor" in todo or "plain" in todo:                      #Check command for notepad
            print("Opening Notepad")
            pyttsx3.speak(" Opening Notepad ")
            os.system("notepad")
        
        elif "draw" in todo or "paint" in todo or "art" in todo :                        #Check command for MS-paint
            print("Opening MS Paint")
            pyttsx3.speak(" Opening MS Paint")
            os.system("mspaint")
       
        elif "music" in todo or "media" in todo or "video" in todo or "song" in todo:   #Check command for W M Player
            print("Opening Windows Media Player")
            pyttsx3.speak(" Opening Windows Media Player")
            os.system("wmplayer")

        elif "chrome" in todo or "browse" in todo or "google" in todo:                   #Check command for chrome
            print("Opening Chrome")
            pyttsx3.speak(" Opening Chrome ")
            os.system("chrome")

        elif "do" in todo and "for" in todo and "me" in todo:
            pyttsx3.speak(" These are the things that i can do the required action for you ")
            print("\nMagnifier\nMS-Word\nMS-Powerpoint\nMS-Excel\nCamera\nWindows Powershell\nCommand Prompt\nSystem Details\nSystem Configuration\nfiles\nWordpad\nCalculator\nfacebook\nGmail")
            print("Whatsapp\nYoutube\nGoogle map\nGoogle Classroom\nGoogle Meet\nGoogle Duo\nContact\nNews\nNotepad\nMS-Paint\nWindows Media Player\nChrome\nDate\nTime")

        elif "exit" in todo :
            pyttsx3.speak(" Turning Off Windows Assistant  ")
            pyttsx3.speak("THANK YOU FOR USING ")
            break
       
        else:
            print("Please enter something valid ")
            pyttsx3.speak(" Please enter something valid ")
    
    elif "exit" in todo:
        pyttsx3.speak("Turning Off Windows Assistant ")
        pyttsx3.speak("THANK YOU FOR USING ")
        break
    
    else:
        print("Please give me a valid command")
        pyttsx3.speak(" Please give me a valid command ")




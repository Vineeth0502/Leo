#................................................ LEO - VIRTUAL ASSISTANT ...........................................................
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import subprocess
import threading
import fitz
import pyttsx3
import datetime
import speech_recognition as sr
import os
import wikipedia
import webbrowser
import cv2
import random
from requests import get
import psutil
import pywhatkit as Kit
import smtplib
import sys
import pyjokes
import pyautogui
import requests
from pyfiglet import print_figlet
import wolframalpha
import socket
import time
from LeoUi import Ui_Leoui
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QThread
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *



api = 'TX4YPJ-3LU7GRXE63'
cleint = wolframalpha.Client(api)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #getting details of available voices
engine.setProperty('voice', voices[0].id) #setting initial voice to default
engine.say("initializing LEO.....")

def voice_change(v):
    if v.isdigit():
        x = int(v)
        if x >= 0 and x < len(voices):
            engine.setProperty('voice', voices[x].id)
            return "Voice changed successfully"
        else:
            return f"Error: voice index {x} out of range (valid range is 0 to {len(voices)-1})"
    else:
        return "Error: argument must be a valid integer"

def femalevoice():
    voice_change('0')

def malevoice():
    voice_change('1')

def speak(audio):
    LeoGui.updateMovies("speaking")
    engine.say(audio)
    LeoGui.terminalPrint(audio)
    engine.runAndWait() #Without this command, speech will not be audible to us.cls

def checktime(tt):
    hour = datetime.datetime.now().hour
    if ("morning" in tt):
        if (hour >= 6 and hour < 12):
            speak("Good morning sir")
        else:
            if (hour >= 12 and hour < 18):
                speak("it's Good afternoon sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good evening sir")
            else:
                speak("it's Goodnight sir")
    elif ("afternoon" in tt):
        if (hour >= 12 and hour < 18):
            speak("it's Good afternoon sir")
        else:
            if (hour >= 6 and hour < 12):
                speak("Good morning sir")
            elif (hour >= 18 and hour < 24):
                speak("Good evening sir")
            else:
                speak("Goodnight sir")
    else:
        speak("night sir!")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
      speak("Good Morning!")

    elif hour>=12 and hour<18:
      speak("Good Afternoon!")

    else:
      speak("Good Evening!")
    speak("I am LEO. Please tell me how may I help you")

def wifi():
    IPaddress = socket.gethostbyname(socket.gethostname())
    if IPaddress == "127.0.0.1":
        speak('no internet connection')
    else:
        LeoGui.terminalPrint("Connected, with the IP address: " + IPaddress)

def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good evening")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    smg = 'its,', 'today is ', 'it is'
    speak(random.choice(smg))
    speak(str(date))
    speak(str(month))
    speak(str(year))

def play_music(file_path):
    subprocess.Popen(['C:\\Program Files\\Windows Media Player\\wmplayer.exe', file_path])
    sys.exit(0)
    
def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=05fd3448167f47ba9b4102ae89e7f555"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        news_text = f"Today's {day[i]} news is: {head[i]}"
        LeoGui.terminalPrint(news_text)
        speak(news_text)

def online():
    print_figlet('LEO :)')
online()

def jokes():
    j = pyjokes.get_joke()
    LeoGui.terminalPrint(j)
    speak(j)

def personal():
    speak("I am LEO , a voice assistant")

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\\LEO\\screenshot.png", format='PNG')

def noint():
    IPaddress = socket.gethostbyname(socket.gethostname())
    if IPaddress == "127.0.0.1":
        speak('no internet connection')

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    LeoGui.terminalPrint('CPU usage is at ' + usage)

def battery():
    battery = psutil.sensors_battery()
    speak("Battery is at " + str(battery.percent) + " percent")
    LeoGui.terminalPrint("Battery is at: " + str(battery.percent) + " percent")

# weather condition
def weather():
    api_key = "814d994da09d63cecc52854fd7577b0e"  # generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = ('hyderabad')
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
                                                       " and " + str(weather_description))
        speak(r)
    else:
        speak(" City Not Found ")

def pdf_reader():
    # Open the PDF file
    book = fitz.open('student.pdf')
    pages = book.page_count
    speak(f"Total number of pages in this book: {pages}")
    speak("Please say the page number to read:")

    # Set up the speech recognition
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        # Convert speech to text
        pg = int(r.recognize_google(audio))
        if pg < 1 or pg > pages:
            speak(f"Invalid page number. Please say a number between 1 and {pages}.")
        else:
            # Get the specified page object
            page = book[pg-1]

            # Extract the text from the page
            text = page.get_text()

            # Convert the text to speech
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
    except ValueError:
        speak("Sorry, I didn't understand that. Please say a valid number.")
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please try again.")

    # Close the PDF file
    book.close()

class InputGetter(QObject):
    input_ready = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.recognizer = sr.Recognizer()

    def get_input(self, prompt):
        print(prompt)
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            result = self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            result = None
        self.input_ready.emit(result)

class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()
        self.alarm_thread = None
        self.input_getter = InputGetter()
        self.input_getter.input_ready.connect(self.process_input)

    def run(self):
        self.TaskExecution()
    #voice to text
    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            LeoGui.updateMovies("listening")
            LeoGui.terminalPrint("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source,timeout=5,phrase_time_limit=8)
        try:
            LeoGui.updateMovies("loading")
            LeoGui.terminalPrint("Recognizing...")    
            self.query = r.recognize_google(audio, language='en-in')
            LeoGui.terminalPrint(f"User said: {self.query}")
        except Exception as e :
            #LeoGui.terminalPrint(e)   
            LeoGui.terminalPrint("Say that again please...")  
            return "None"
        return self.query

    def input_time(self):
        """
            Function to parse user input and return a datetime object
        """
        speak("What time should I set the alarm for?")
        while True:
            time = self.takeCommand().upper().replace('.','')

            try:
                alarm_time = datetime.datetime.strptime(time, '%I:%M %p')
                return alarm_time
            except ValueError:
                speak("Sorry, I didn't understand that. Please tell me the time in HH:MM AM/PM format.")
                continue

    def set_alarm(self, alarm_time, music_file):
        while True:
            now = datetime.datetime.now()
            if now.hour == alarm_time.hour and now.minute == alarm_time.minute:
                play_music(music_file)
                break
            else:
                time.sleep(10) # Sleep for 10 seconds before checking the time again

    def process_input(self, name):
         
        # Look up the phone number for the given name
        phone_numbers = {
            "Ramya": "+919390465058",
            "vineet": "+919876543210",
            "ketham": "+919999888777"
        }
        phone_num = phone_numbers.get(name.lower())
        if phone_num is None:
            print(f"No phone number found for {name}")
        else:
            # Set the phone number and ask the user for the message
            self.phone_num = phone_num
            message = "What message do you want to send?"
            speak(message)
            # The result will be passed to self.send_message
            self.message = self.input_getter.get_input("")


    def send_message(self, message):
        # Call the sendwhatmsg() function with the phone number and message parameters, and default time_hour and time_min values
        Kit.sendwhatmsg(self.phone_num, message, time_hour=datetime.datetime.now().hour, time_min=datetime.datetime.now().minute + 1)

    def TaskExecution(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainer/trainer.yml')
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath)

        font = cv2.FONT_HERSHEY_SIMPLEX

        id = 2
        names = ['', 'vineeth']

        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cam.set(3, 640)
        cam.set(4, 480)

        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)

        face_detected = False  # Flag to keep track of whether a face has been detected
        start_time = time.time()  # Get the current time

        while not face_detected and time.time() - start_time < 10:  # Exit loop if face is detected or 10 seconds have passed
           
            ret, img = cam.read()

            converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                converted_image,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH)),
            )

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

                id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])

                if (accuracy < 100):
                    id = names[id]
                    accuracy = "  {0}%".format(round(100 - accuracy))
                else:
                    id = "unknown"
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    sys.exit()
                cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
                cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

                face_detected = True  # Set flag to True once a face has been detected

            cv2.imshow('camera', img)
            cv2.waitKey(1)

        # Release the webcam resources
        cam.release()
        cv2.destroyAllWindows()
        LeoGui.updateMovies("speaking")
        speak("verification successful")
        speak("hello sir i am your virtual assistant")
        speak("welcome back vineeth sir")
        noint()
        wishMe() 
        while True:  
        #if 1:
            self.query = self.takeCommand().lower()

            if "open notepad" in self.query:
                npath = "C:\\Windows\\notepad.exe"
                os.startfile(npath)

            elif "open visual studio code" in self.query:
                vpath = "C:\\Users\\VINEETH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(vpath)

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "read pdf " in self.query or "read pdf file" in self.query:
                pdf_reader()

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('camera', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                pyautogui.hotkey('escape')
                cap.release()
                cv2.destroyAllWindows()

            elif "turn off camera" in self.query or "close camera" in self.query:
                pyautogui.hotkey('escape')

            elif "play music" in self.query:
                music_dir = "D:\\songs"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP adress is {ip}")

            elif 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")            
                #LeoGui.terminalPrint(results)
                speak(results)

            elif "today date" in self.query or "today's date" in self.query:
                date()
            
            elif 'open facebook' in self.query:
                webbrowser.open("facebook.com")

            elif 'open instagram' in self.query:
                webbrowser.open("instagram.com")

            elif 'open snapchat' in self.query:
                webbrowser.open("web.snapchat.com")

            elif 'open google' in self.query:
                speak("sir, what should i search on google")
                cm = self.takeCommand().lower()
                webbrowser.open(f"{cm}")

            elif 'open stackoverflow' in self.query:
                webbrowser.open("stackoverflow.com")

            elif "send message" in self.query or "send message to " in self.query:
               self.input_getter.get_input(speak("Who do you want to send a message to?"))

            elif "play song on youtube" in self.query:
                Kit.playonyt("see you again")

            elif "send email" in self.query:

                speak("what should i send? text or file")
                self.query = self.takeCommand().lower()
                if "file" in self.query or "attach" in self.query or "attached file" in self.query:
                    email = "vineethketham@gmail.com"
                    password = "xgtwvaagzrclwdbn"
                    send_to_email ="kethamvineeth@gmail.com"
                    speak("okay sir, what is the subject for this email")
                    self.query = self.takeCommand().lower()
                    subject = self.query
                    speak("and sir, what is the message for this email")
                    query2 = self.takeCommand().lower()
                    message = query2
                    speak("sir please enter the correct path of the file into the shell")
                    file_location = input("enter the path:")

                    speak("please wait, i am sending email now")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    #setup the attachment
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application','octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition',"attachment; filename= %s" %filename)

                    #attach the attachment to the MIMEMultipart object
                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("email has been sent to vineeth")

                else:
                    email = "vineethketham@gmail.com"
                    password = "xgtwvaagzrclwdbn"
                    send_to_email ="kethamvineeth@gmail.com"
                    message = self.query

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    server.sendmail(email, send_to_email, message)
                    server.quit()
                    speak("email has been sent to vineeth")

            elif "sleep" in self.query:
                speak("thanks for using me sir, have a good day")
                sys.exit()

            elif "close notepad" in self.query:
                speak("okay sir,closing notepad")
                os.system("taskkill /f /im notepad.exe")

            # set alarm
            elif "set alarm" in self.query:
                if self.alarm_thread is not None and self.alarm_thread.is_alive():
                    speak("Sorry, an alarm is already set. Please wait for it to go off or say 'stop alarm' to stop it.")
                else:
                    alarm_time = self.input_time()
                    speak("Alarm set for " + alarm_time.strftime('%I:%M %p'))
                    music_file = "D:\\songs\\alarm.mp3"
                    self.alarm_thread = threading.Thread(target=self.set_alarm, args=(alarm_time, music_file))
                    self.alarm_thread.start() # Start the thread to check for the alarm time and play the music

            elif "play music" in self.query:
                music_file = "D:\\songs\\alarm.mp3"
                play_music(music_file)

            elif "stop" in self.query:
                    stop_music()

            elif "stop alarm" in self.query:
                if self.alarm_thread is not None and self.alarm_thread.is_alive():
                    stop_alarm()

            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shutdown the system" in self.query:
                os.system("shutdown /s /t 5")
            
            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif "switch window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.press("right")
                pyautogui.keyUp("alt")
                speak('window switched')

            elif "news" in self.query:
                speak("please wait sir, fetching the latest news")
                news()

            elif "time" in self.query:
                    strTime = datetime.datetime.now().strftime("%I:%M:%S")
                    timemsg = (f', {strTime}'), (f'it is , {strTime}'), (f'the current time is, {strTime}'), (
                        f'its , {strTime}')
                    speak(random.choice(timemsg))

            elif 'i am sad' in self.query:
                smg = ['here is something for you ' + jokes(), 'i hate that one', 'i, really dont like it']
                speak(' '.join(random.choice(smg)))
        
            elif 'i love you' in self.query:
                reply = ['i also like you', 'i like it', "i don't hate you", 'i also love you as a friend']
                speak(' '.join(random.choices(reply)))

            elif "volume up" in self.query or "increase the volume" in self.query or "increase volume" in self.query:
                pyautogui.press("volumeup")

            elif "volume down" in self.query or "decrease the volume" in self.query or "decrease volume" in self.query:
                pyautogui.press("volumedown")

            elif "mute" in self.query or "mute the volume" in self.query or "mute volume" in self.query:
                pyautogui.press("volumemute")
           
            elif ("tell me about yourself" in self.query):
                personal()

            elif ("about you" in self.query):
                personal()

            elif ("who are you" in self.query):
                personal()

            elif ("yourself" in self.query):
                personal()

            elif 'tell me the weather in' in self.query or "tell me today's weather " in self.query or "weather in" in self.query:
                    self.query = self.query.replace("weather", "")
                    self.query = self.query.replace("of", "")
                    self.query = self.query.replace("at", "")
                    self.query = self.query.replace("the", "")
                    self.query = self.query.replace("in", "")
                    self.query = self.query.replace("city", "")
                    self.query = self.query.replace("tell", "")
                    self.query = self.query.replace("me", "")
                    self.query = self.query.replace("can", "")
                    self.query = self.query.replace("you", "")
                    self.query = self.query.replace("today's", "")
                    self.query = self.query.replace("in", "")

                    api_key = "814d994da09d63cecc52854fd7577b0e"
                    base_url = "http://api.openweathermap.org/data/2.5/weather?"
                    city_name = self.query
                    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                    response = requests.get(complete_url)
                    x = response.json()
                    if x["cod"] != "404":
                        y = x["main"]
                        current_temperature = y["temp"]
                        current_pressure = y["pressure"]
                        current_humidiy = y["humidity"]
                        z = x["weather"]
                        weather_description = z[0]["description"]
                        r = ("in " + city_name + " Temperature is " +
                            str(int(current_temperature - 273.15)) + " degree celsius " +
                            ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
                            ", humidity is " + str(current_humidiy) + " percent"
                                                                    " and " + str(weather_description))
                        speak(r)

                    else:
                        speak(" City Not Found ")

            elif 'tell me the weather' in self.query:
                weather()

            elif 'youtube search' in self.query:
                self.query = self.query.replace("youtube", "")
                self.query = self.query.replace("search", "")
                self.query = self.query.replace("on", "")
                self.query = self.query.replace("youtube", "")
                site = 'https://www.youtube.com//results?search_query=m' + self.query
                webbrowser.open(site)
            
            elif 'tell me the temperature' in self.query:
                weather()

            elif "tell me today's temperature" in self.query:
                weather()
                
            elif "open website" in self.query:
                    speak("Tell me the name of the website")
                    search = self.takeCommand().lower()
                    speak('Opening' + search)
                    url = 'www.' + search + '.com'
                    webbrowser.open(url)

            elif  'clear reminders' in self.query or 'clear all reminder' in self.query:
                    replyt = 'ok clearing all the reminders ' , 'cleared' , 'cleared all the reminders' 
                    speak(random.choice(replyt))
                    f = open("D:\\data.txt", "r+")  
                    f.seek(0)    
                    f.truncate() 

            elif 'full form of friday' in self.query:
                speak('Female Replacement Intelligent Digital Assistant Youth')

            elif 'face' in self.query:
                    speak('opening face recognition')
                    path = 'D:\\LEO\\Face Recognition.py'
                    os.startfile(path)

            elif ("do you know anything" in self.query or "remember" in self.query):
                    reminder_file = open("D:\\LEO\\data.txt", 'r')
                    speak("You said me to remember that: " + reminder_file.read())

            elif ("powers" in self.query or "help" in self.query or "features" in self.query or 'what can you do' in self.query):
                    features = ''' i can help to do lot many things like..
                        i can tell you the current time and date,
                        i can tell you the current weather,
                        i can tell you battery and cpu usage,
                        i can create the reminder list,
                        i can shut down or logout or hibernate your system,
                        i can tell you non funny jokes,
                        i can open any website,
                        i can repeat what you  you told me,
                        i can search the thing on wikipedia,
                        i can change my voice from male to female and vice-versa
                        i have  a search engine make by my sir if you want to know something just say open search and ask the question
                        i have a wake word detection i will be online if you say hey leo
                        And yes one more thing, My sir is working on this system to add more features...,
                        tell me what can i do for you??
                        '''
                    speak(features)

            elif ("voice" in self.query):
                    if 'female' in self.query:
                        femalevoice()

                    else:
                        malevoice()

            elif ('i am done' in self.query or 'bye bye LEO' in self.query or 'no work' in self.query or 'go offline LEO' in self.query or 'bye' in self.query or'nothing' in self.query ):
                    speak("thanks for using me sir, have a good day")
                    sys.exit()

            elif ("how's your day going" in self.query or 'how is your day going' in self.query or 'you day' in self.query):
                    speak('Wonderfull , thanks for asking me sir, how can i help you ')

            elif ('change my name' in self.query or 'change name' in self.query or 'change I name' in self.query):
                # Open "name.txt" file in read and write mode, and set the file pointer to the beginning
                with open("D:\\LEO\\name.txt", "r+") as f:
                    f.seek(0)
                    # Truncate the file contents
                    f.truncate()
                    # Prompt the user to say their name and store the response in sname variable
                    speak('Tell me your name')
                    sname = self.takeCommand()

                    # Check if the user's name contains the string "vineeth"
                    if 'vineeth' in sname.lower():
                         # Open the "name.txt" file in write mode, write the user's name to the file, and close the file
                        with open("D:\\LEO\\name.txt", "w") as file1:
                            file1.write(sname)

                        # Read the contents of the file and speak a welcome message with the user's name
                        with open("D:\\LEO\\name.txt", "r") as file2:
                            file_contents = file2.read()
                            speak('From now on, I will call you Sir ' + file_contents)

                    else:
                        # Open the "name.txt" file in write mode, write the user's name to the file, and close the file
                        with open("D:\\LEO\\name.txt", "w") as file1:
                            file1.write(sname)

                        # Speak a welcome message with the user's name
                        speak('Welcome, Sir ' + sname)

            elif 'change birthday' in self.query:
                    f = open("D:\\LEO\\birthday.txt", "r+")
                    f.seek(0)
                    f.truncate()
                    speak('tell me the birthday date')
                    sname = self.takeCommand()
                    file1 = open("D:\\LEO\\birthday.txt", "w")
                    file1.write(sname)
                    file1.close()
                    file2 = open("D:\\LEO\\birthday.txt", "r")
                    file_contents = file2.read()
                    file2.close()
                    speak('so your birthday is at ' + file_contents)

            elif 'my birthday date' in self.query or "my birthday" in self.query:
                f = open('D:\\LEO\\birthday.txt', 'r')
                file_contents = f.read()
                speak(file_contents)

            elif 'are you there' in self.query:
                speak('hello there')

            elif 'tell me my name' in self.query or "my name" in self.query:

                f = open('D:\\LEO\\name.txt', 'r')
                file_contents = f.read()
                speak(file_contents)

            elif 'hey' in self.query:
                speak('hey')
            
            elif 'screenshot' in self.query:
                speak('ok sir')
                screenshot()

            elif 'cpu' in self.query:
                cpu()
            
            elif 'battery' in self.query:
                battery()

            elif 'open location' in self.query:
                speak('tell me the location you are looking for')
                location = self.takeCommand()
                url2 = 'https://google.nl/maps/place/' + location +'/&amp;'
                webbrowser.open(url2)
                speak('location on your screen sir')

            elif 'close browser' in self.query:
                try:
                    speak('as you wish')

                except Exception as e:
                    speak("i cant do that right now")

            elif 'close all' in self.query:
                try:
                    speak('as you wish')
                    os.system('TASKKILL /F /IM *')

                except Exception as e:
                    speak("i cant do that right now")
           
            elif 'close file' in self.query:
                try:
                    speak('as you wish')
                    os.system('TASKKILL /F /IM Explorer.exe')
                except Exception as e:
                    speak("i cant do that right now")     
            
            elif 'my location' in self.query:
                speak('opening your home location on browser')
                loc = 'https://www.google.co.in/maps/@26.1317482,91.8018681,18.5z'
                webbrowser.open(loc)

            elif 'close' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("F4")
                pyautogui.keyUp()
                speak('application killed')
                
            elif 'what is your name' in self.query:
                speak('MY NAME is LEO')     

            elif 'folder' in self.query:
                speak('tell me the name of the folder')
                path= 'C:\\Users\\VINEETH\\OneDrive\\Desktop'
                os.chdir(path)
                Newfolder=self.takeCommand()
                os.makedirs(Newfolder)
                speak('i have  made a folder named' +Newfolder+'in you dekstop directry')
                
            elif 'hello leo' in self.query or 'lo leo' in self.query:
                speak("hello sir how's going")
               
            elif 'hey  LEO' in self.query:
                speak('hey sir what can i do for you')

            elif 'red or blue' in self.query:
                speak('BLue sir')
                
            elif 'your favorite colour' in self.query or 'tell me your favourite colour' in self.query:
                speak('blue')
                
            elif 'change colour' in self.query:
                os.system('color 03')

            elif 'how are you' in self.query:
                speak('I am fine sir ')

            elif 'hello' in self.query:
                speak('hello sir')   

            if 'wake up' in self.query:
                speak('Online and ready sir')
            
            if "you can't do anything" in self.query or 'you are nothing' in self.query or  'you are dumb' in self.query or 'you dont have brain' in self.query or 'you are mad' in self.query:
                speak("Sorry sir")

            elif 'question' in self.query:
                speak('tell me the question you want to get')
                question = self.takeCommand()
                speak('getting information sir')
                try:
                    try:
                        results = wikipedia.summary(question, sentences=2)
                        speak(results)
                    except:
                        client = wolframalpha.Client('TX4YPJ-3LU7GRXE63')
                        res = client.voice_data(question)
                        results = next(res.results).text
                        speak(results)
                except:
                    speak("Sorry sir i didn't get it")

            elif "thank you " in self.query:
                speak("it's my pleasure sir")
            
            speak("sir, do you have any other work")
      
startExecution = MainThread()
    
class Main(QtWidgets.QMainWindow, Ui_Leoui):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Leoui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_3.clicked.connect(self.manualCodeFromTerminal)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("G.U.I Material/B.G/Background.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("G.U.I Material/B.G/Iron_Template_1.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("G.U.I Material/ExtraGui/initial.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("G.U.I Material/ExtraGui/B.G_Template_1.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("G.U.I Material/B.G/techcircle.gif")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("G.U.I Material/B.G/tech loading-cropped.gif")
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("G.U.I Material/B.G/speaking.gif")
        self.ui.label_10.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("G.U.I Material/B.G/listening.gif")
        self.ui.label_11.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("G.U.I Material/VoiceReg/sleepmode.gif")
        self.ui.label_12.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

    def updateMovies(self, state):
        if state == "listening":
            self.ui.label_11.raise_()
            self.ui.label_10.hide()
            self.ui.label_12.hide()
            self.ui.label_9.hide()
            self.ui.label_11.show()
        elif state == "speaking":
            self.ui.label_10.raise_()
            self.ui.label_11.hide()
            self.ui.label_12.hide()
            self.ui.label_9.hide()
            self.ui.label_10.show()
        elif   state == "loading":
            self.ui.label_9.raise_()
            self.ui.label_10.hide()
            self.ui.label_12.hide()
            self.ui.label_11.hide()
            self.ui.label_9.show()
        elif   state == "sleeping":
            self.ui.label_12.raise_()
            self.ui.label_10.hide()
            self.ui.label_9.hide()
            self.ui.label_11.hide()
            self.ui.label_12.show()

    def terminalPrint(self, text):
        self.ui.terminalOutputBox.appendPlainText(text)

    def manualCodeFromTerminal(self):
        cmd = self.ui.lineEdit.text()
        if cmd:
            self.ui.lineEdit.clear()
            self.ui.terminalOutputBox.appendPlainText(f"You Just typed>> {cmd}")

            if cmd == 'exit':
                LeoGui.close()
            elif cmd == 'help':
                self.terminalPrint("I can perform various tasks which is programmed inside me by my sir")

            else:
                pass
        else:
            pass

if __name__ == "__main__":

    app = QApplication(sys.argv)
    LeoGui = Main()
    LeoGui.show()
    exit(app.exec_())


from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import subprocess
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
import pywhatkit as Kit
import smtplib
import sys
import pyjokes
import pyautogui
import requests
from pyfiglet import  print_figlet
import wolframalpha
import socket
import time
import psutil
import threading

api = 'TX4YPJ-3LU7GRXE63'
cleint = wolframalpha.Client(api)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #getting details of available voices
engine.setProperty('voice', voices[0].id) #setting initial voice to default
engine.say("initializing LEO.....")
engine.say("hello sir i am your virtual assistant")

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
    engine.say(audio)
    print(audio)
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
        print("Connected, with the IP address: " + IPaddress)

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
    speak(date)
    speak(month)
    speak(year)

def play_music(file_path):
    subprocess.Popen(['C:\\Program Files\\Windows Media Player\\wmplayer.exe', file_path])
    sys.exit(0)

def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=05fd3448167f47ba9b4102ae89e7f555"
    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day = ["first","second","third","fourth","fifth"]#["sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        #print(f"today's {day[i]} news is:", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

def online():
    print_figlet('LEO :)')
online()

def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)

def personal():
    speak(
        "I am LEO , a voice assistant")

def screenshot():
    img = pyautogui.screenshot()
    img.save(
        "D:\\LEO"
    )

def noint():
    IPaddress = socket.gethostbyname(socket.gethostname())
    if IPaddress == "127.0.0.1":
        speak('no internet connection')

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)

def battery():
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))

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

def input_time():
    
    """
     Function to parse user input and return a datetime object
    """
    speak("What time should I set the alarm for?")
    while True:
        time = takeCommand().upper().replace('.','')

        try:
            alarm_time = datetime.datetime.strptime(time, '%I:%M %p')
            return alarm_time
        except ValueError:
            speak("Sorry, I didn't understand that. Please tell me the time in HH:MM AM/PM format.")
            continue

def set_alarm(alarm_time, music_file):
    while True:
        now = datetime.datetime.now()
        if now.hour == alarm_time.hour and now.minute == alarm_time.minute:
            play_music(music_file)
            break
        else:
            time.sleep(10) # Sleep for 10 seconds before checking the time again

#voice to text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=10,phrase_time_limit=8)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e :
        #print(e)    
        print("Say that again please...")  
        return "None"
    return query

def TaskExecution():
  cam.release()
  cv2.destroyAllWindows()
  speak("verification successful")
  speak("welcome back vineeth sir")
  noint()
  wishMe() 
  alarm_thread = None
  while True:  
  #if 1:
    
    query = takeCommand().lower()

    if "open notepad" in query:
        npath = "C:\\Windows\\notepad.exe"
        os.startfile(npath)

    elif "open visual studio code" in query:
        vpath = "C:\\Users\\VINEETH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(vpath)

    elif "open command prompt" in query:
        os.system("start cmd")

    elif("read pdf " in query or "read pdf file" in query):
        pdf_reader()

    elif "open camera" in query:
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

    elif "turn off camera" in query or "close camera" in query:
       pyautogui.hotkey('escape')

    elif "play music" in query:
        music_dir = "D:\\songs"
        songs = os.listdir(music_dir)
        rd = random.choice(songs)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[0]))

    elif "ip address" in query:
        ip = get('https://api.ipify.org').text
        speak(f"your IP adress is {ip}")

    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")            
        #print(results)
        speak(results)

    elif "date" in query:
        date()
    
    elif 'open facebook' in query:
        webbrowser.open("facebook.com")

    elif 'open instagram' in query:
        webbrowser.open("instagram.com")

    elif 'open snapchat' in query:
        webbrowser.open("web.snapchat.com")

    elif 'open google' in query:
        speak("sir, what should i search on google")
        cm = takeCommand().lower()
        webbrowser.open(f"{cm}")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif "send message" in query:
        Kit.sendwhatmsg("+919390465058","this is testing protocol",19,59)

    elif "volume up" in query or "increase the volume" in query or "increase volume" in query:
        pyautogui.press("volumeup")

    elif "volume down" in query or "decrease the volume" in query or "decrease volume" in query:
        pyautogui.press("volumedown")

    elif "mute" in query or "mute the volume" in query or "mute volume" in query:
        pyautogui.press("volumemute")

    elif "play song on youtube" in query:
        Kit.playonyt("see you again")

    elif "send email" in query:

        speak("what should i send? text or file")
        query = takeCommand().lower()
        if "file" in query or "attach" in query or "attached file" in query:
            email = "vineethketham@gmail.com"
            password = "xgtwvaagzrclwdbn"
            send_to_email ="kethamvineeth@gmail.com"
            speak("okay sir, what is the subject for this email")
            query = takeCommand().lower()
            subject = query
            speak("and sir, what is the message for this email")
            query2 = takeCommand().lower()
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
            message = query

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, send_to_email, message)
            server.quit()
            speak("email has been sent to vineeth")

    elif "sleep" in query:
        speak("thanks for using me sir, have a good day")
        sys.exit()

    elif "close notepad" in query:
        speak("okay sir,closing notepad")
        os.system("taskkill /f /im notepad.exe")
        alarm = int(datetime.datetime.now().hour)
        if alarm==22:
            music_dir = "D:\\songs"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

    elif "set alarm" in query:
        if alarm_thread is not None and alarm_thread.is_alive():
            speak("Sorry, an alarm is already set. Please wait for it to go off or say 'stop alarm' to stop it.")
        else:
            alarm_time = input_time()
            speak("Alarm set for " + alarm_time.strftime('%I:%M %p'))
            music_file = "D:\\songs\\alarm.mp3"
            alarm_thread = threading.Thread(target=set_alarm, args=(alarm_time, music_file))
            alarm_thread.start() # Start the thread to check for the alarm time and play the music

    elif "play music" in query:
        music_file = "D:\\songs\\alarm.mp3"
        play_music(music_file)

    elif "stop" in query:
        stop_music()

    elif "stop alarm" in query:
        if alarm_thread is not None and alarm_thread.is_alive():
            stop_alarm()
        else:
            speak("Sorry, there is no alarm set to stop.")

    elif "tell me a joke" in query:
        joke = pyjokes.get_joke()
        speak(joke)

    elif "shutdown the system" in query:
        os.system("shutdown /s /t 5")
    
    elif "restart the system" in query:
        os.system("shutdown /r /t 5")

    elif "sleep the system" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif "switch window" in query:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        pyautogui.press("right")
        pyautogui.keyUp("alt")
        speak('window switched')

    elif "news" in query:
        speak("please wait sir, fetching the latest news")
        news()

    elif "time" in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            timemsg = (f', {strTime}'), (f'it is , {strTime}'), (f'the current time is, {strTime}'), (
                f'its , {strTime}')
            speak(random.choice(timemsg))

    elif 'i am sad' in query:
        joke = jokes()
        if joke is not None:
            smg = 'Here is something to cheer you up: ' + joke
        else:
            smg = "Sorry, I couldn't think of a joke right now."
        speak(smg)

    elif 'i love you' in query:
            reply = 'i also like you', 'i like it', "i don't hate you", 'i also love you as a friend'
            speak(random.choices(reply))

    elif ("tell me about yourself" in query):
        personal()

    elif ("about you" in query):
        personal()

    elif ("who are you" in query):
        personal()

    elif ("yourself" in query):
        personal()

    elif 'tell me the weather in' in query or "tell me today's weather " in query:
            query = query.replace("weather", "")
            query = query.replace("of", "")
            query = query.replace("at", "")
            query = query.replace("the", "")
            query = query.replace("in", "")
            query = query.replace("city", "")
            query = query.replace("tell", "")
            query = query.replace("me", "")
            query = query.replace("can", "")
            query = query.replace("you", "")
            query = query.replace("today's", "")
            query = query.replace("in", "")

            api_key = "814d994da09d63cecc52854fd7577b0e"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = query
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

    elif 'tell me the weather' in query:
        weather()

    elif 'youtube search' in query:
        query = query.replace("youtube", "")
        query = query.replace("search", "")
        query = query.replace("on", "")
        query = query.replace("youtube", "")
        site = 'https://www.youtube.com//results?search_query=m' + query
        webbrowser.open(site)
    
    elif 'tell me the temperature' in query:
        weather()

    elif "tell me today's temperature" in query:
        weather()
        
    elif "open website" in query:
            speak("Tell me the name of the website")
            search = takeCommand().lower()
            speak('Opening' + search)
            url = 'www.' + search + '.com'
            webbrowser.open(url)

    elif ('clear reminders' in query or 'clear all reminder' in query):
            replyt = 'ok clearing all the reminders ' , 'cleared' , 'cleared all the reminders' 
            speak(random.choice(replyt))
            f = open("D:\\LEO\\data.txt", "r+")  
            f.seek(0)    
            f.truncate() 

    elif 'full form of friday' in query:
        speak('Female Replacement Intelligent Digital Assistant Youth')

    elif ('face' in query or 'detect' in query):
            speak('opening face recognition')
            path = 'D:\\LEO\\Face recognition.py'
            os.startfile(path)

    elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("D:\\LEO\\data.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())

    elif ("powers" in query or "help" in query or "features" in query or 'what can you do' in query):
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

    elif ("voice" in query):
            if 'female' in query:
                femalevoice()

            else:
                malevoice()

    elif ('i am done' in query or 'bye bye LEO' in query or 'no work' in query or 'go offline LEO' in query or 'bye' in query or'nothing' in query ):
            speak("thanks for using me sir, have a good day")
            sys.exit()

    elif ("how's your day going" in query or 'how is your day going' in query or 'you day' in query):
        speak('Wonderfull , thanks for asking me sir, how can i help you ')

    elif ("what's my name" in query or "what is my name" in query):
        with open('name.txt', 'r') as file:
          text = file.read()
        speak(text)

    elif ('change my name' in query or 'change name' in query or 'change I name' in query):
        # Open "name.txt" file in read and write mode, and set the file pointer to the beginning
        with open("D:\\LEO\\name.txt", "r+") as f:
            f.seek(0)
            # Truncate the file contents
            f.truncate()
            # Prompt the user to say their name and store the response in sname variable
            speak('Tell me your name')
            sname = takeCommand()

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

    elif 'change birthday' in query:
            
            f = open("D:\\LEO\\birthday.txt", "r+")
            f.seek(0)
            f.truncate()
            speak('tell me the birthday date')
            sname = takeCommand()
            file1 = open("D:\\LEO\\birthday.txt", "w")
            file1.write(sname)
            file1.close()
            file2 = open("D:\\LEO\\birthday.txt", "r")
            file_contents = file2.read()
            file2.close()
            speak('so your birthday is at ' + file_contents)

    else:
        # Handle other commands here
        pass
   
    speak("sir, do you have any other work")

if __name__ == "__main__":
   
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
                TaskExecution()
            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

            face_detected = True  # Set flag to True once a face has been detected

        cv2.imshow('camera', img)
        cv2.waitKey(1)

    # Release the webcam resources
    cam.release()
    cv2.destroyAllWindows()


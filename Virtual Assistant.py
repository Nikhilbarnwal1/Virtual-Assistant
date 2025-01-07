import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import subprocess
import pyjokes
import calendar
import AppOpener
import pyautogui
import pywhatkit
import qrcode
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 150)
print(type(engine))
print(engine)

def speak(audio): #to speak. Text to Speech
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    minute= int(datetime.datetime.now().minute)
    if (hour>=0 and hour<12):
        print("Good Morning sir!")
        speak("Good Morning sir!")     #Text to Speech
    elif(hour>=12 and hour<18):
        print("Good afternoon sir!")
        speak("Good afternoon sir!")
    else:
        print("Good Evening sir")
        speak("Good Evening sir")
    print("I am your voice assistant, How may I help you?")
    speak("I am your voice assistant, How may I help you?")
def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

    def generate_qr_code(text):
        qr = qrcode.QRCode()
        qr.add_data(text)
        qr.make()
        qr.save("qr-code.png")

def takeCommand(): #it takes microphone input from the user and return the string output
     r=sr.Recognizer()    #recogniser class helps in recognising the audio
     with sr.Microphone() as source:
         print("please tell me your query")
         speak("please tell me your query")
         print("Listening...")
         r.pause_threshold = 0.5 #it refers to the amount of time gap after which the audio is supposed to be complete
         r.energy_threshold =300
         audio=r.listen(source)#digitaldata of whatsoever hs been spoken will be stored in audio
     try:
      print("Recognising...")
      query=r.recognize_google(audio,language="en-in")
      print("User Said:",query)
     except Exception as e:
      print("Say that again please!")
      return "None"
     return query
wishMe()
#while True:
if 1:
    query = takeCommand().lower()
    if 'on wikipedia' in query:
        speak("Searching on  Wikipedia please wait")
        print("Searching on  Wikipedia please wait")
        query=query.replace("on wikipedia", "")
        results=wikipedia.summary(query, sentences=5)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'on youtube' in query:
        speak("searching on youtube please wait")
        print("searching on youtube please wait")
        query=query.replace("on youtube","")
        query=query.replace("search","")
        webbrowser.open("https://youtube.com/search?q=%s" % query)
    elif 'open my web development website' in query:
        webbrowser.open("https://nassoftech.lapmates.com/")
    elif 'open my shopping website' in query:
        webbrowser.open("sskp-online-shopping.free.nf")
    elif 'on google' in query:
        speak("opening in google please wait")
        print("opening in google please wait")
        query=query.replace("on google","")
        query=query.replace("search","")
        webbrowser.open("https://google.com/search?q=%s" % query)
    elif 'open youtube' in query:
        speak("opening youtube please wait")
        print("opening youtube please wait")
        webbrowser.open("youtube.com")
    elif 'open facebook' in query:
        speak("opening facebook please wait")
        print("opening facebook please wait")
        webbrowser.open("fb.com")
    elif 'open instagram' in query:
        speak("opening instagram please wait")
        print("opening instagram please wait")
        webbrowser.open("instagram.com")
    elif 'open whatsapp' in query:
        speak("opening whatsapp please wait")
        print("opening whatsapp please wait")
        webbrowser.open("https://web.whatsapp.com/")
    elif 'open email' in query:
        speak("opening email please wait")
        print("opening email please wait")
        webbrowser.open("mail.google.com/")
    elif 'tell me the time' in query:
        time=datetime.datetime.now().strftime("%H:%M")
        speak("sir, the time is")
        speak(time)
    elif 'hello' in query:
        speak("Hii How can i help you")
    elif 'whose laptop is this' in query:
        speak("this is nikhil laptop")
        print("this is nikhil laptop")
    elif 'weather report' in query:
        speak("searching please wait")
        print("searching please wait")
        webbrowser.open("https://mausam.imd.gov.in/")
    elif 'book movie ticket' in query:
        speak("after opening website please search your favourite movie")
        print("after opening website please search your favourite movie")
        webbrowser.open("https://in.bookmyshow.com/explore/movies-national-capital-region-ncr")
    #https://in.bookmyshow.com/expl ore/movies
    elif 'book hotel' in query:
        speak("opening please wait")
        print("opening please wait")
        webbrowser.open("https://www.booking.com/")
    elif 'book flight ticket' in query:
        speak("opening please wait")
        print("opening please wait")
        webbrowser.open("https://www.makemytrip.com/flights/")
    elif 'book train ticket' in query:
        speak("silent please some time")
        webbrowser.open("https://www.irctc.co.in/nget/train-search")
    elif'train enquiry' in query:
        speak("Opening please wait")
        print("Opening please wait")
        webbrowser.open("https://enquiry.indianrail.gov.in/mntes/")
    elif ' group members name' in query:
        print("Nikhil")
        print("Piyush")
        print("Abhishek")
        speak("Nikhil")
        speak("Piyush")
        speak("Abhishek")
    elif 'food' in query:
        speak("did you want to eat something")
        print("did you want to eat something")
        query = takeCommand().lower()
        if 'yes' in query:
            speak("ok sir wait a second")
            print("ok sir wait a second")
            speak("from which company you want to order swiggy or zomato")
            print("from which company you want to order swiggy or zomato")
            query = takeCommand().lower()
            if 'zomato' in query:
                speak("ok sir please wait a second")
                print("ok sir please wait a second")
                webbrowser.open("https://www.zomato.com/")
            elif 'swiggy' in query:
                speak("ok sir please wait a second")
                print("ok sir please wait a second")
                webbrowser.open("https://www.swiggy.com/")
            else:speak("please select anyone.")
        # elif 'no' in query:
        #     speak("ok sir no problem")
        else:speak(" sir please tell me yes or no and restart the program")
    elif 'open map' in query:
        speak("opening map please wait")
        print("opening map please wait")
        webbrowser.open("https://google.com/maps/")
    elif 'online shopping' in query:
        print("ok sir wait a second")
        speak("ok sir wait a second")
        print("what type of items you want to purchase")
        speak("what type of items you want to purchase")
        query = takeCommand().lower()
        if 'dress' in query:
            webbrowser.open("https://www.myntra.com/")
        elif 'shoes' in query:
            webbrowser.open("https://www.flipkart.com/q/shoes")
        elif 'phone' in query:
            webbrowser.open("https://www.amazon.in/mobile-phones/b?ie=UTF8&node=1389401031")
        elif 'all items' in query:
            webbrowser.open("https://www.flipkart.com/")
    elif 'shut down my laptop' in query:
        speak("are you sure want to shut down your laptop")
        query = takeCommand().lower()
        if 'yes' in query:
            speak("Please wait shutting down your laptop")
            os.system("shutdown /s")
        else:speak("i am not shutting down sir thank you")
    elif 'sleep my laptop' in query:
        speak("are you sure want to sleep")
        query = takeCommand().lower()
        if 'yes' in query:
            speak(" ok sir i am sleeping Thank you")
            os.system("shutdown /l")
        else:speak("i am not sleeping sir thank you")
        exit()
    elif 'jokes' in query:
        print(pyjokes.get_joke())
        speak(pyjokes.get_joke())
    elif 'calendar' in query:
        speak(calendar.show_calendar)
    elif "today is which day" in query:
        tellDay()
    elif 'news about goverment jobs' in query:
        webbrowser.open("https://www.sarkariresult.com/")
    elif 'latest news' in query:
        webbrowser.open("https://www.hindustantimes.com/")
    elif 'play online songs' in query:
        speak("ok wait a second")
        print("ok wait a second")
        webbrowser.open("https://open.spotify.com/search")
    elif "open vs code" in query:
        speak("opening vs code please wait")
        print("opening vs code please wait")
        codePath="C:\\Users\\asd\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
        os.startfile(codePath)
    elif "open chrome" in query:
        speak("opening chrome please wait")
        print("opening chrome please wait.")
        codePath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(codePath)
    elif 'azad polytechnic on map' in query:
        webbrowser.open("https://www.google.com/maps/place/Azad+Polytechnic+Bharthipur/@25.7683939,83.1250097,17.71z/data=!4m6!3m5!1s0x3991b70fffffffff:0x72bc8cf8321df647!8m2!3d25.768653!4d83.126558!16s%2Fg%2F11btx0w2vg?entry=ttu")
    elif 'open xamp' in query:
        codePath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\XAMPP"
        os.startfile(codePath)
    elif 'create qr code' in query:
        img = qrcode.make(input("Enter your data:"))
        img.save("my.png")
    elif 'send message to piyush' in query:
        pywhatkit.sendwhatmsg("+918931034828",input("Enter your  :"),23,9)
    elif 'help' in query:
        print("Opening please wait")
        speak("Opening please wait")
        webbrowser.open("https://www.india.gov.in/help")
    exit()

"+918931034828"
                                                                                                                                                                                                                                                                                                                                                                                                        
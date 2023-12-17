# add feature   calculate ko function meh padla baka check for + - * signs and then direct it to function cus calculate 
import pyttsx3 #pip install pyttsx3==2.71
import speech_recognition as sr #pip install speechrecognition
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import docx
from docx import Document   #pip install python-docx
import random as r 
import time 
import requests 
import random
import pafy	#pip install youtube-dl  #pip install pafy
import pywhatkit  #pip install pywhatkit
import wolframalpha #pip install wolframalpha
import requests
from time import sleep
import sys
import subprocess
#pip install pipwin  #pipwin install pyaudio         #https://youtu.be/dj5oOPaeIqI for pip install problems
import pyjokes  #pip install pyjokes 
engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

#links for google serches
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
url = 'http://google.com/'
url1 = 'http://youtube.com/'
url2 = 'https://netflix.com'
url3 = 'https://twitter.com/'
url4 = 'https://pinterest.com/'
url5 = 'https://instagram.com/'
url7 = 'https://flipkart.com/'
url8 = 'https://amazon.com/'
mic=1
def speak(audio): 
    
    engine.say(audio)#what ever audio system will say
    engine.runAndWait()
def greeting():
    hour=datetime.datetime.now()
    hour1=int(hour.strftime("%H"))#module date time 0-24 hour of the day is obtained here
    if hour1>=0 and hour1<12:
        speak("Good Morning!")#speaks this

    elif hour1>=12 and hour1<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    print("ANA: I am Ana, Please tell me how may I help you?")
    speak("I am Ana, Please tell me how may I help you?")  
def uservoice():
    #It takes microphone input from the user and returns string output with which it works

    r = sr.Recognizer()#this is a class which helps in recognising voice
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1.5# seconds of non-speaking audio before a phrase is considered complete(built in)
        
        audio = r.listen(source)#all from speech recognition module

    try:#mayerror possibility
        print("......")    
        command = r.recognize_google(audio, language='en-in')#google speech recognition and language set
        
        
        
        print("You:",command)

    except Exception as exp:#if the google API couldnt recognise
          print("Say that again please...") 
          return "None"#none string is returned if nothing
    return command
def News(): 
      
    
    main_url =  "http://newsapi.org/v2/top-headlines?country=in&apiKey=fc5b69bf6b704344b926ebeaf63b8e25"
    open_page= requests.get(main_url).json() 
    article = open_page["articles"] 
    results = [] 
    for ar in article: 
        results.append(ar["title"]) 
    news_number=int(input("enter the number of hedlines u need"))
    for i in range(news_number): 
        print(i + 1, results[i]) 
        speak(results[i]) 
        time.sleep(2)                
print("user guide:\n hey yoo.... Ana the virtual assistant can do various simple stuff for u\n\
    1: it replies to simple what/who type of questions...say \"who is virat kohli\"\n\
    2: Do some math calulations including some calculus...say \"calculate 10 plus 10\"\n\
    3: Does some simple convertions...say \"convert 5 km to m\"\n\
    4: Gets u the latest news...say \"news\"\n\
    5: plays songs for u...say \"play perfect\"\n\
    6: stopwatch..say \"start stopwatch\"\n\
    7: standard date n time... say \"what is the time \"\n\
    8: opens word documents...say \"open word\"\n\
    9: open websites\n\
    10: wikipedia searches...say\"ronaldo wikipedia\"\n\
    11: say \"tell me a joke\" ")

greeting()
while True:#infinite loop
    mainvar=input("press enter for ana to listen to you:")
    command = uservoice().lower()
    

        #how its gonna excecute
    if 'wikipedia' in command:#if the user tells stn with wikipedia in it
            print('ANA: Searching Wikipedia please wait...')
            speak('Searching Wikipedia please wait...')
            command = command.replace("wikipedia", "")
            try:
                info = wikipedia.summary(command,sentences=2)#2 sentence from wiki argument1= title to serch argument2=number of sentences to get
                print("ANA: According to Wikipedia")
                speak("According to Wikipedia")
                print(info)
                speak(info)
            except:
                print(" Please be specific with your search, For example: Instead of Virat Kohli say Virat Kohli cricketer wikipedia")
                speak("Please be specific with your search, For example: Instead of Virat Kohli say Virat Kohli cricketer wikipedia")
    elif "convert" in command:
        try:
            com_list=command.split()
            for i in com_list:
                try:
                    
                    ele_e= int(i)
                    ele_f=com_list.index(i)
                    
                except:
                    pass
            index1=ele_f + 1
            index2= ele_f+ 3
            operand1=com_list[index1]
            operand2=com_list[index2]
        except:
            print("ANA : Please repeat sir it didnt make sense")
            speak("ANA : Please repeat sir it didnt make sense")
        if "metre" in command:
            
            #km to others
            if operand1== "km" or operand1=="kilometre" and operand2=="metre" or operand2=="m" or operand2=="metres":
                res_main= ele_e*1000.0
                print("Ana:",ele_e,"kilometres is equal to",res_main,"metres")
                speak("{} kilometres is equal to {} metres".format(ele_e,res_main))
            elif operand1=="km" or operand1=="kilometre" and operand2=="centimetre" or operand2=="cm":
                res_main= ele_e*100000.0
                print("Ana:",ele_e,"kilometres is equal to",res_main,"centimetres")
                speak("{} kilometres is equal to {} centimetres".format(ele_e,res_main))
            elif operand1=="km" or operand1=="kilometre" and operand2=="milimetre" or operand2=="mm":
                res_main= ele_e*10000000.0
                print("Ana:",ele_e,"kilometres is equal to",res_main,"milimetres")
                speak("{} kilometres is equal to {} milimetres".format(ele_e,res_main))
            elif operand1=="km" or operand1=="kilometre" and operand2=="miles":
                res_main= ele_e*0.6214
                res_main="{:3f}".format(res_main)
                print("Ana:",ele_e,"kilometres is equal to",res_main,"miles")
                speak("{} kilometres is equal to {} miles".format(ele_e,res_main))
            
            #metres to others
            elif operand1=="m" or operand1=="metre" or operand1=="metres" and operand2=="kilometres" or operand2=="km" or operand2=="kilometre":
                res_main= ele_e/1000
                print("Ana:",ele_e,"metres is equal to",res_main,"kilometeres")
                speak("{} kilometres is equal to {} kilometres".format(ele_e,res_main))
            elif operand1=="m" or operand1=="metre" or operand1=="metres" and operand2=="centimetres" or operand2=="cm":
                res_main= ele_e*100
                print("Ana:",ele_e,"metres is equal to",res_main,"centimeteres")
                speak("{} kilometres is equal to {} centimeteres".format(ele_e,res_main))
            elif operand1=="m" or operand1=="metre" or operand1=="metres" and operand2=="milimetres" or operand2=="mm":
                res_main= ele_e*1000
                print("Ana:",ele_e,"metres is equal to",res_main,"miliimeteres")
                speak("{} kilometres is equal to {} miliimeteres".format(ele_e,res_main))
            elif operand1=="m" or operand1=="metre" or operand1=="metres" and operand2=="miles":
                res_main= ele_e*0.000621371
                res_main="{:3f}".format(res_main)
                print("Ana:",ele_e,"metres is equal to",res_main,"centimeteres")
                speak("{} kilometres is equal to {} centimeteres".format(ele_e,res_main))
            
            #centimetres or others
            elif operand1=="cm" or operand1=="centimetre" and operand2=="kilometres" and operand2=="km":
                res_main= ele_e/10000
                res_main="{:3f}".format(res_main)
                print("Ana:",ele_e,"centimetre is equal to",res_main,"kilometeres")
                speak("{} centimetres is equal to {} kilometeres".format(ele_e,res_main))
            elif operand1=="cm" or operand1=="centimetre"  and operand2=="metre" or operand2=="m":
                res_main= ele_e/100
                print("Ana:",ele_e,"centimetres is equal to",res_main,"meteres")
                speak("{} centimetres is equal to {} meteres".format(ele_e,res_main))
            elif operand1=="cm" or operand1=="centimetre" and operand2=="milimetres" or operand2=="mm":
                res_main= ele_e*10
                print("Ana:",ele_e,"centimetres is equal to",res_main,"miliimeteres")
                speak("{} centimetres is equal to {} miliimeteres".format(ele_e,res_main))
            
            #miles to others
            elif operand1=="miles" and operand2=="kilometres" and operand2=="km":
                res_main= ele_e*1.60934
                res_main="{:3f}".format(res_main)
                print("Ana:",ele_e,"miles is equal to",res_main,"kilometeres")
                speak("{} miles is equal to {} kilometeres".format(ele_e,res_main))
            elif operand1=="miles" and operand2=="centimeters" or operand2=="cm":
                res_main= ele_e*160934
                print("Ana:",ele_e,"miles is equal to",res_main,"centimeteres")
                speak("{} miles is equal to {} centimeteres".format(ele_e,res_main))
            
    elif "pika" in command:
        print("ANA: Pikachu is a pokemon that can generate powerful electricity have cheek sacs that are extra soft and super stretchy")
        speak("ANA: Pikachu is a pokemon that can generate powerful electricity have cheek sacs that are extra soft and super stretchy")
        print("Do you waant me to fetch u more info")
        speak("Do you waant me to fetch u more info")
        command = uservoice().lower()
        if "yes" in command:
            webbrowser.get(chrome_path).open_new_tab('https://www.pokemon.com/us/pokedex/pikachu')
        else:
            pass


            
    elif "good morning" in command or "morning" in command or "good afternoon" in command or "afternoon" in command or "evening" in command or "good evening" in command :
        pass
    
    
            
    elif "stopwatch" in command:
        
        speak(" okay,starting stopwatch")
        speak(" press enter to start stopwatch")
        start=input("ANA: press enter to start")
        begin=time.time()
        speak(" started stopwatch, to stop it, press enter")
        endtimer=input("ANA: press enter to stop")
        end=time.time()
        timet=end-begin
        timet=int(timet)
        if timet<60:
            timet=str(timet)
            timet=timet+ " seconds"
        elif timet>60:
            time11=int(timet%60)
            time2=int(timet//60)
            timet=str(timet)
            timet=time2,"minutes",time11,"seconds"
        
        speak("the time elapsed was {}".format(timet))
    


    elif 'time' in command:
        timeof=datetime.datetime.now()
        time1=timeof.strftime("%H  %M %p")
        print("ANA: The time is {}".format(time1))
        speak("The time is {}".format(time1))

    elif "day" in command or "week day" in command or 'date' in command or "what is the date" in command:
        date=datetime.datetime.now()
        date2=date.strftime("%A %d %B %Y")
        print("ANA: its {} ".format(date2))
        speak("its {} ".format(date2))
    
    
        
    
        
    elif 'open word' in command or  'open ms word' in command or 'ms word' in command:
        
        speak("ANA: what do you want the file name to be")
        command=uservoice().lower()
        speak("ANA: opening word")
        document=Document()
        document.save('{}.docx'.format(command))
        document1 = Document('{}.docx'.format(command))
        document.save('{}.docx'.format(command))
        os.system('start {}.docx'.format(command))

    elif 'calculate' in command or "calculator" in command:
        if "integra" in command or "differen" in command:
            try:
            
                last=command
                app_id = "H9GULL-EAT8R8U4TA" 
                client = wolframalpha.Client(app_id) 
  
                indx = last.split().index('calculate') 
                query = last.split()[indx + 1:] 
                res = client.query(' '.join(query)) 
                answer1 = next(res.results).text 
                print("ANA: the answer of {}".format(answer1))
                speak("The answer of  " + answer1)
            except:
                pass
        
        command=command.replace("calculate","")
        
        one=command.count("one")
        for i in range(one):
            command=command.replace("one","1")
        command=command.replace("plus","+")
        if  "+" in command:
            
            try:
                result=eval(command)
                speak("the sum is {}".format(result))
                print("ANA: the sum is {}".format(result))
            except:
                pass
        elif "-" in command:
            
            try:
                result=eval(command)
                speak("the difference is {}".format(result))
                print("ANA: the difference is {}".format(result))
            except:
                pass
        elif "into" in command:
            number=command.count("into")
            for i in range(number):
                add=command.replace('into', '*')
                    
            try:
                result=eval(add)
                speak("the product is {}".format(result))
                print("ANA: the product is {}".format(result))
            except:
                pass
        elif "by" in command or "/" in command:
            command=command.replace("divided","")
            command=command.replace("by","/")
            try:
                result=eval(command)
                speak("the quotient is {}".format(result))
                print("ANA: the quotient is {}".format(result))
            except:
                pass
            
        elif " x " in command:
            try:
                number=command.count(" x ")
                for i in range(number):
                    add=command.replace(" x "," * ")
                    result=eval(add)
                    speak("the product is {}".format(result))
                    print("ANA: the product is {}".format(result))
            except:
                pass
        else:
            speak("please repeat")
            print("ANA: please repeat")
    elif "video" in command or "youtube" in command:
        try:  
            command=command.replace("open","")
            command=command.replace("video","")
            command=command.replace("youtube","")
            command=command.replace("play","")
            if command=="":
                break
            else:
                pywhatkit.playonyt(command) 
                print("ANA: Playing...")
                speak("playing")
                time.sleep(10) 
        except:
            pass
    elif "hey" in command or "hi" in command or "hai" in command or "hay" in command or "hello" in command or ("who" in command and "are" in command) :
        print("ANA: Helloo!! So, if you are talking to me for the first time, then let me quickly introduce myself !I am Ana, a 21st century, minor virtual assistant,designed by Pratham Shetty  I can help you with a few minor everyday tasks of yours.")
        speak("Helloo!! So, if you are talking to me for the first time, then let me quickly introduce myself !I am Ana, a 21st century, minor virtual assistant,designed by Pratham Shetty. I can help you with a few minor everyday tasks of yours.")
    elif 'who' in command or "what" in command or "where" in command or "when" in command:
            print("ANA: just a second")
            speak('just a second')
            
            try:
                print("ANA: ")
                info = wikipedia.summary(command,sentences=2)#2 sentence from wiki argument1= title to serch argument2=number of sentences to get
                print(info)
                speak(info)
            except:
                print("ANA: Failed to get you good information shall i play a video on {}".format(command))
                speak("Failed to get you good information shall i play a video on {}".format(command))
                yorn=input("YES or NO?")
                yorn.lower
                if yorn=="yes":
                    print("ANA: playing a video on {}".format(command))
                    speak("playing a video on {}".format(command))
                    url=(pywhatkit.playonyt(command))
                    video = pafy.new(url)
                    time.sleep(10)
                else:
                    continue
    elif "joke" in command:
        joke=pyjokes.get_joke()
        print("ANA:",joke)
        speak(joke)        

    elif "music" in command or "song" in command:
        speak(" Any specific song u want me to play?")
        command=uservoice().lower()
        if "no" in command or "nope" in command:
            speak(" okay playing music")
            music_dir="D:\pratham baabu\song"
            songs=list(os.listdir(music_dir))
            random.shuffle(songs)
            for i in range(len(songs)):
                os.startfile(os.path.join(music_dir, songs[i]))

        else:
            if "yes" in command:
                speak("which song then")
                command=uservoice().lower()
                query=command.replace("play","")
                url=(pywhatkit.playonyt(query))
                video = pafy.new(url)
                print("ANA: okay playing{}".format(query))
                speak("okay playing{}".format(query))
                time.sleep(10)
            else:
                query=command.replace("play","")
                url=(pywhatkit.playonyt(query))
                video = pafy.new(url)
                speak("okay playing{}".format(query))
                time.sleep(10)
    elif "play" in command:
        query=command.replace("play","")
        url=(pywhatkit.playonyt(query))
        video = pafy.new(url)
        speak("ANA: okay playing{}".format(query))
        time.sleep(10)
        
    elif "news" in command or "hedlines" in command or "headlines" in command:
        print("ANA: Fetching news")
        speak("fetching news")
        speak("enter the number of headlines u need")
        
        News()

    elif "notepad" in command and "open" in command:
        print("ANA: opening notepad")
        speak("okay opening notepad")
        os.system('notepad.exe')

    elif "open google" in command:
        speak("opening google")
        webbrowser.get(chrome_path).open_new_tab(url)
    elif "open" in command and "my files" in command or "file exlorer" in command or "my file"in command:
        print("ANA: opening...")
        speak("opening..")
        fname="C:\\Windows\\explorer"
        os.system(fname)
    elif "how" in command and "to" in command:
        print("ANA: playing a video on {}".format(command))
        speak("playing a video on {}".format(command))
        url=(pywhatkit.playonyt(command))
        video = pafy.new(url)
        time.sleep(10)
    elif "open"in command and  "youtube" in command:
        webbrowser.get(chrome_path).open_new_tab(url1)
    elif "open netflix" in command:
        webbrowser.get(chrome_path).openew_tab(url2)
    elif "open twitter" in command:
        webbrowser.get(chrome_path).open_new_tab(url3)
    elif "open pinterest" in command:
        webbrowser.get(chrome_path).open_new_tab(url4)
    
    elif "open instagram" in command:
        webbrowser.get(chrome_path).open_new_tab(url5)
    elif "open flipkart" in command:
        webbrowser.get(chrome_path).open_new_tab(url7)
    elif "open amazon" in command:
        webbrowser.get(chrome_path).open_new_tab(url8)
    elif "hey" in command or "hi" in command or "hai" in command or "hay" in command or "hello" in command or ("who" in command and "are" in command) :
        print("ANA: Helloo!! So, if you are talking to me for the first time, then let me quickly introduce myself !I am Ana, a 21st century, minor virtual assistant,designed by Annapurna Shenoy ,Pratham Shetty and Prathik N.K. I can help you with a few minor everyday tasks of yours.")
        speak("Helloo!! So, if you are talking to me for the first time, then let me quickly introduce myself !I am Ana, a 21st century, minor virtual assistant,designed by Annapurna Shenoy ,Pratham Shetty and Prathik N.K. I can help you with a few minor everyday tasks of yours.")
    elif 'quit' in command or 'exit' in command or 'close' in command  or "bye" in command:
        print("ANA: okay have a good day")
        speak("okay, Have a good day!!!!")
        exit()
    
    elif "are" in command and "you" in command and "human" in command: 
        print("Ana : Ummm,not a human, i am a virtual assistant")
        speak(" Ummm,not a human, i am a virtual assistant")
    elif "your" in command and "age" in command or "how old" in command and "are" in command and "you" in command :
        print("Ana : Shhhh ! dont ask, i would prefer keeping it a secret ")
        speak("Shhhh ! dont ask, i would prefer keeping it a secret ")
    elif 'quit' in command or 'exit' in command or 'close' in command  or "bye" in command:
        print("ANA: okay have a good day")
        speak("okay, Have a good day!!!!")
        exit()
    
    
    elif "how are you" in command or "how are u doing" in command:
        speak("i am doing great")
    
    else:
        print("ANA:i dont know what your speaking about")
        speak("i dont know what your speaking about")





        

    
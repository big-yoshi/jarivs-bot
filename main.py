#! encoding=UTF-8
import pyttsx3
import time
import speech_recognition as sr
import os
import random
from weather import *


import wikipedia as wk

if os.name == 'posix':

	import gi
	gi.require_version('Notify', '0.7')
	from gi.repository import Notify as nt
	from gi.repository import GdkPixbuf as img
	def notify(text,urg=1):
	    nt.init("jarvis A.I")
	    nt.set_app_name("Jarvis")
	    image = img.Pixbuf.new_from_file("unnamed.png")
	    nots = nt.Notification.new(text)
	    nots.set_icon_from_pixbuf(image)
	    nots.set_image_from_pixbuf(image)
	    nots.set_urgency(urg)
	    nots.show()
	    speak(text)
	    time.sleep(1)
	    nots.close()
################################################################
hi_words = ['hi', 'yo', 'what\'s up', 'hey', 'hello']
Q_words = ['where', 'when', 'who', 'what']
w_words = ['was', 'were']
d_words = ['do', 'does', 'did']
p_words = ['is','am','are']
h_words = ['have', 'has', 'had']
sub_words = ['i', 'i am', 'we', 'our', 'they', 'them', 'you', 'your', 'it']
sub_with_s_words = ['yours', 'mine', 'theirs', 'ours', 'its']
names = ['jarvis']
init_words = ['lunch','start','initiate']
###################################################################
all_lists = [hi_words,Q_words,w_words,d_words,p_words,h_words,sub_words,sub_with_s_words,names,init_words,names]
###################################################################
#RESPONSE LIST
r_hi_words = ['hello sir','glad to see you back','welcome back sir']
####################################################################
wBrain = open("brain/learn.txt",'w')
rBrain = open("brain/learn.txt",'r')
####################################################################
def speak(word,sp=140):
    NUM = 1
    word = str(word)
    engine = pyttsx3.init()
    rate = engine.getProperty("rate") - 200
    engine.setProperty('voice', 'english-us')
    engine.setProperty('rate', rate + sp)
    for _ in range(1):
            engine.say(word)
            engine.runAndWait()
###################################################################
def check_weather(loc):
    weather = Weather(unit=Unit.CELSIUS)
    lookup = weather.lookup_by_location(loc)
    cond = lookup.condition
    print("Condition: "+str(cond.text))
    print("Temp:      "+str(cond.temp))
    print("Date:      "+str(cond.date))

    speak("Condition: "+str(cond.text))
    speak("Temperature:      "+str(cond.temp)+" degrees")
###################################################################

###################################################################
def search_info(cont):
    listed = wk.search(cont)
    for stuff in listed:
        print("{}".format(stuff))
        speak(stuff,180)
    speak("your order sir")
    order = wk.summary(input("\norder:\t"))
    print(order)
###################################################################
def listen_for_cmd():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("[*] Listening ")
        audio = r.listen(source ,timeout=8,phrase_time_limit=7)
        print("[*] Getting Data")

    text = r.recognize_google(audio)
    print(text)
    conditions(text)
###################################################################
def conditions(text):
    string = str(text).split(' ')
    for word in string:
        if word in hi_words:
            if 'jarvis' in string:
                ch = random.choice(r_hi_words)
                speak(ch)

        if word in Q_words:
            for p_ in p_words:
                try:
                        x = string.index(p_)
                        break
                        return x
                except:
                        pass
            name = string[x+1:]
            print(name)
            speak(name)


    if 'search' in string and 'for' in string:
        text = str(text)
        num = text.rfind("for")
        person = text[num+4:]
        #person = str(person).split(" ")
        #person = person[0]
        speak("searching for "+str(person))
        search_info(person)
        notify("all the info on the web about "+person)

    if 'weather' in string and 'for' in string:
        text = str(text)
        num = text.rfind("for")
        city = text[num+4:]
        city = str(city).split(" ")
        city = city[0]
        speak("checking weather for "+city)
        check_weather(city)
###################################################################


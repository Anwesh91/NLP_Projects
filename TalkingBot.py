import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()#Listening voice from the user
engine = pyttsx3.init()#Converting Voice into Text
voices = engine.getProperty('voices')#setting property of Alexa
engine.setProperty('voice', voices[0].id)#0 is for male voice and 1 is for feamale voice


def talk(text):
    engine.say(text)
    engine.runAndWait()
    
    
def take_command():
    try: 
        with sr.Microphone() as source:
            print('listening.........')
            voice =listener.listen(source)#listening from local user
            command = listener.recognize_google(voice)#saving the voice signal in digital format as voice variable
            command = command.lower()
            if 'Alex' in command :#chaking command has the name of Alex in our case name is 'bot', we can use anything like Alexa, HeyGoogle, Buddy etc...
                command =command.replace('Alex','')
                print(command)
                
    except:
        pass
       # print ("I am unable to Listen. Please Speak again...")
    return command
  
  
def run_bot():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        talk('Current time is '+ time)
    elif 'who' in command:
        person = command.replace('Who','')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'which' in command:
        person = command.replace('which','')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'where' in command:
        person = command.replace('where','')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'what' in command:
        person = command.replace('what','')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'is' in command:
        person = command.replace('is','')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'are' in command:
        person = command.replace('are','')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'how' in command:
        person = command.replace('how','')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'corona' in command:
        person = command.replace('corona','')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'sports' in command:
        person = command.replace('sport','')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'love' in command:
        person = command.replace('love','')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'peace' in command:
        person = command.replace('peace','')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'Are you Bot' in command:
        print('Yes I am Bot Created by Anwesh')
        talk('Yes I am Bot Created by Anwesh')
    elif 'Joke' in command:
        talk(pykokes.get_joke())
    else:
        talk ('I am only talking bot Not God, Please refer Internet, friends and family')
            


while True:
    run_bot()
import pyttsx3 as tts
import datetime
import speech_recognition as sr
import wikipedia
import sys
import webbrowser

engine = tts.init("sapi5")
engine.setProperty("rate", 190)
v = engine.getProperty("voices")
engine.setProperty("voice", v[1].id)

def speak(text):
    '''func to speak the given text'''
    engine.say(text)
    engine.runAndWait()

def wish_me():
    '''function to greet the user depending on the current time, everytime the program is run'''
    h = datetime.datetime.now().hour

    if h >= 0 and h < 12:
        speak("good morning")
    elif h >= 12 and h < 17:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("i am knightwalker, a virtual assistant.")

def take_command():
    '''will take audio command and return a text query'''
    r = sr.Recognizer()
    r.energy_threshold = 200
    mic = sr.Microphone()
    try:
        print('listening..')
        with mic as source:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
        query = r.recognize_google(audio, language="en-IN")
        print(query)
        query = query.lower()
        if "knightwalker" in query:
            query = query.replace("knightwalker", "")
        return query

    except sr.RequestError:
        speak("you are not connected to the internet")
        sys.exit()

    except:
        speak("sorry i didn't hear u!! say that again please")
        return "none"

def curr_date():
    '''returns today's date'''
    dt = datetime.date.today()
    return dt

def curr_time():
    '''returns current time'''
    dt = datetime.datetime.now()
    return dt

if __name__ == "__main__":
    wish_me()
    while True:
        command = take_command()

        if "quit" in command or "bye" in command:
            speak("happy to be of your service")
            sys.exit()

        elif command == "none":
            pass

        elif "hi" in command:
            speak(f"hi how are you doing?")

        elif "hello" in command:
            speak(f"hello how are you doing?")

        elif "i am doing well" in command or "i am feeling great" in command:
            speak("that's awesome i'm happy to hear that")

        elif "what's your name" in command or "what is your name" in command:
            speak("my name is knightwalker")

        elif "how old are you" in command or "what's your age" in command:
            speak(
                "i dont know my exact age but i was created on the 2nd of february 2022 which is literally the 2nd day of the second month of the year 2022")

        elif "who are you" in command:
            speak("i am knightwalker,your beloved ai assistant")

        elif "where do you live" in command:
            speak("i was created in new delhi")

        elif "what can you do" in command:
            speak("i can do anything for you, you name it i've got it")

        elif "what do you do for a living" in command:
            speak("i am an ai. i help people with their daily tasks")

        elif "what are your hobbies" in command:
            speak("i dont have any particular hobbies however i do like to sing")

        elif "can you play guitar" in command:
            speak("no, as of now i dont but i am looking forward to learning it")

        elif "do you like someone" in command or "are you single" in command or "are you dating someone" in command:
            speak("i am not dating anyone at the moment ,however i am looking for my soulmate. i hope i meet my soulmate soon")

        elif "date" in command:
            date = curr_date()
            d = date.strftime("%d-%m-%Y")
            print(f"today is {d}")
            speak(f"today is {d}")

        elif "what day is it" in command or "what's the day" in command:
            date = curr_date()
            d = date.strftime("%A")
            speak(f"today is {d}")

        elif "what month is it" in command or "what's the month" in command:
            date = curr_date()
            m = date.strftime("%B")
            speak(f"it is currently {m}")

        elif "what year is it" in command or "what's the year" in command:
            date = curr_date()
            y = date.strftime("%Y")
            speak(f"it is currently {y}")

        elif "what's the time" in command or "what time is it" in command or "what is the time" in command:
            t = curr_time()
            t1 = t.strftime("%I:%M %p")
            speak(f"it is {t1} right now")

        elif "what is" in command:
            command = command.replace("what is", "")
            query1 = command[1:]
            query = query1.replace(" ", "+")
            base = "https://www.google.com/search?q="
            q = base + query
            webbrowser.open(q)

        elif "what do you mean by" in command:
            command = command.replace("what do you mean by", "")
            query1 = command[1:]
            query = query1.replace(" ", "+")
            base = "https://www.google.com/search?q="
            q = base + query
            webbrowser.open(q)

        elif "define" in command:
            command = command.replace("define", "")
            query1 = command[1:]
            query = query1.replace(" ", "+")
            base = "https://www.google.com/search?q="
            q = base + query
            webbrowser.open(q)

        elif "search on youtube" in command or "youtube search" in command:
            speak("alright what do u want me to search for")
            com = take_command()
            if "search for" in command:
                com = com.replace("search for", "")
                com = com[1:]
            query = com.replace(" ", "+")
            base = "https://www.youtube.com/results?search_query="
            q = base + query
            webbrowser.open(q)

        elif "search on google" in command or "google search" in command:
            speak("alright what do u want me to search for")
            com = take_command()
            if "search for" in command:
                com = com.replace("search for", "")
                com = com[1:]
            query = com.replace(" ", "+")
            base = "https://www.google.com/search?q="
            q = base + query
            webbrowser.open(q)

        elif "open google" in command:
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")

        elif "open geeks for geeks" in command or "open gfg" in command:
            webbrowser.open("https://www.geeksforgeeks.org")

        elif "open stack overflow" in command:
            webbrowser.open("https://stackoverflow.com")

        elif "wikipedia" in command:
            command = command.replace("wikipedia", "")
            speak(f"searching for {command}")
            wiki = wikipedia.summary(command, sentences=2, auto_suggest=False)
            speak(wiki)

        elif "you are the best" in command or "you are awesome" in command:
            speak("thank you so much. i'm happy to be of help")

        else:
            speak("sorry i don't know what you mean")

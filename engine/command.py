import pyttsx3
import speech_recognition as sr
import eel
import time


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Set to the first voice (usually the default voice)
    engine.setProperty('rate', 180)  # Set the speaking rate
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()
@eel.expose
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, 10, 7)
        try:
            print("Recognizing...")
            eel.DisplayMessage("Recognizing...")
            query = r.recognize_google(audio, language='en-pk')
            print(f"User said: {query}\n")
            eel.DisplayMessage(query)
            time.sleep(2)
           
    
        except Exception as e:
            print("Sorry, I could not understand your voice.")
            query = ""
        return query.lower()
    # all commands
@eel.expose
def allcommands(message=1):
    if message == 1:
        query = takecommand()
        print( query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:
     

     if 'open' in query:
        from engine.features import Opencommand
        Opencommand(query)
     elif 'on YouTube' in query:
       from engine.features import playYouTube
       playYouTube(query)

     elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp, makeCall,sendMessage
            contact_no, name = findContact(query)
            if(contact_no != 0):
                speak("Which mode you want to use whatsapp or mobile")
                preferance = takecommand()
                print(preferance)

                if "mobile" in preferance:
                    if "send message" in query or "send sms" in query: 
                        speak("what message to send")
                        message = takecommand()
                        sendMessage(message, contact_no, name)
                    elif "phone call" in query:
                        makeCall(name, contact_no)
                    else:
                        speak("please try again")
                elif "whatsapp" in preferance:
                    message = ""
                    if "send message" in query:
                        message = 'message'
                        speak("what message to send")
                        query = takecommand()
                                        
                    elif "phone call" in query:
                        message = 'call'
                    else:
                        message = 'video call'
                                        
                    whatsApp(contact_no, query, message, name)
     else:
       from engine.features import chatBot
       chatBot(query)
    except:
       print("Error ")    
       
    eel.ShowHood()        



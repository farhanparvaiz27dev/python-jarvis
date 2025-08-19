import os
import re
from shlex import quote
import struct
import subprocess
import time
import webbrowser
import hugchat
from playsound import playsound
import eel
import pvporcupine
import pyaudio
import pyautogui
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
from engine.db import cursor
from engine.helper import extract_yt_term, remove_words



# Function to play the assistant sound
@eel.expose
def  playAssistantSound():
     music_dir = "www\\assets\\audio\\start_sound.mp3"
     playsound(music_dir)


def Opencommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower()

    app_name = query.strip()

    if app_name != "":
     try:
        # Check if the app is in the sys_commands table
        cursor.execute("SELECT path FROM sys_commands WHERE name IN (?)", (app_name,))
        results = cursor.fetchall()

        if len (results)!= 0:
            speak("Opening " + app_name)
            os.startfile(results[0][0])

        elif len(results) == 0:
            # Check in web_commands table
            cursor.execute("SELECT url FROM web_commands WHERE name IN (?)", (app_name,))
            results = cursor.fetchall()

            if len (results) != 0:
                speak("Opening " + query)
                webbrowser.open(results[0][0])  # Assumes URL works with os.startfile

            else:
                speak("Opening " + query)
                try:
                    os.system('start ' + query)
                except Exception:
                    speak(" not found ")
     except Exception as e:
        speak("Something went wrong")
        print("Error:", e)


def playYouTube(query):
    search_term = extract_yt_term(query)
    speak("playing" + search_term + "on YouTube")
    kit.playonyt(search_term)



def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()



#### 8. Create find contacts number Function in features.py
def findContact(query):
    
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+92'):
            mobile_number_str = '+92' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0

# whatsApp function to send message, call or video call

def whatsApp(mobile_no, message, flag, name):
    

    if flag == 'message':
        target_tab = 20
        jarvis_message = "message send successfully to "+name

    elif flag == 'phone call':
        target_tab = 14
        message = ''
        jarvis_message = "calling to "+name

    else:
        target_tab = 13
        message = ''
        jarvis_message = "staring video call with "+name


    # Encode the message for URL
    encoded_message = quote(message)
    print(encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range( target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(jarvis_message)


from groq import Groq

client = Groq(api_key="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")

# Store conversation history outside the function so it persists
messages = [{"role": "system", "content": "You are a helpful AI assistant."}]

def chatBot(query):
    user_input = query.lower()

    # Add user message to conversation
    messages.append({"role": "user", "content": user_input})

    # Get model response
    response = client.chat.completions.create(
        model="llama3-8b-8192",  # Free model
        messages=messages
    )

    answer = response.choices[0].message.content

    # Add assistant reply to conversation
    messages.append({"role": "assistant", "content": answer})

    # Output
    print(answer)
    speak(answer)  # Your existing voice output function
    return answer

# android automation

def makeCall(name, mobileNo):
    mobileNo =mobileNo.replace(" ", "")
    speak("Calling "+name)
    command = 'adb shell am start -a android.intent.action.CALL -d tel:'+mobileNo
    os.system(command)

    
# to send message
def sendMessage(message, mobileNo, name):
    from engine.helper import replace_spaces_with_percent_s, goback, keyEvent, tapEvents, adbInput
    message = replace_spaces_with_percent_s(message)
    mobileNo = replace_spaces_with_percent_s(mobileNo)
    speak("sending message")
    goback(4)
    time.sleep(1)
    keyEvent(3)
    # open sms app
    tapEvents(263, 1366)
    #start chat
    tapEvents(557, 1407)
    # search mobile no
    adbInput(mobileNo)
    #tap on name
    tapEvents(601, 574)
    # tap on input
    tapEvents(390, 2270)
    #message
    adbInput(message)
    #send
    tapEvents(657, 935)
    speak("message send successfully to "+name)



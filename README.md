🤖 Jarvis – Your Personal AI Assistant

Jarvis is a voice-activated personal assistant built using Python, combining speech recognition, text-to-speech, face authentication, chat AI integration, and a frontend UI with HTML, CSS, and JavaScript animations.

It supports hotword detection, chatbot responses via API, and real-time command execution like opening apps, playing YouTube videos, sending WhatsApp messages, and more.

🚀 Features

🎙 Speech to Text & Text to Speech – Converts your speech into text and responds back with natural voice.

🧠 AI Chat Integration – Uses API keys (Groq LLaMA model) for intelligent responses with chat history.

👤 Face Recognition Authentication – Secures access by verifying the user’s face before starting.

🔑 Hotword Detection – Wake Jarvis using keywords like "Jarvis" or "Alexa".

📂 Custom Commands – Open apps, search the web, play YouTube videos, and more.

📱 WhatsApp Integration – Send messages, make calls, and even start video calls.

📡 Android Automation (ADB) – Place calls or send SMS via connected Android devices.

💻 Frontend UI – Built with HTML, CSS, JavaScript and animated with Eel for seamless desktop integration.

🎨 Chat History & Animations – Displays interactive responses with animations in the frontend.

🛠️ Tech Stack

Backend: Python 3, Eel

Frontend: HTML, CSS, JavaScript

Voice & AI: SpeechRecognition, pyttsx3, pvporcupine (Hotword), Groq API

Face Recognition: OpenCV (LBPH model)

Automation: PyAutoGUI, PyWhatKit, ADB tools

Database: SQLite (commands & contacts)

📂 Project Structure
Jarvis/
│── run.py              # Entry point – runs main Jarvis & hotword processes
│── main.py             # Starts frontend + face authentication
│── features.py         # Core assistant features (chat, hotword, YouTube, WhatsApp, etc.)
│── engine/             # Authentication, commands, configs, database
│── www/                # Frontend (HTML, CSS, JS, animations)
│── envjarvis/          # Virtual environment

⚡ Installation

Clone the repository:

git clone🤖 Jarvis – Your Personal AI Assistant

Jarvis is a voice-activated personal assistant built using Python, combining speech recognition, text-to-speech, face authentication, chat AI integration, and a frontend UI with HTML, CSS, and JavaScript animations.

It supports hotword detection, chatbot responses via API, and real-time command execution like opening apps, playing YouTube videos, sending WhatsApp messages, and more.

🚀 Features

🎙 Speech to Text & Text to Speech – Converts your speech into text and responds back with natural voice.

🧠 AI Chat Integration – Uses API keys (Groq LLaMA model) for intelligent responses with chat history.

👤 Face Recognition Authentication – Secures access by verifying the user’s face before starting.

🔑 Hotword Detection – Wake Jarvis using keywords like "Jarvis" or "Alexa".

📂 Custom Commands – Open apps, search the web, play YouTube videos, and more.

📱 WhatsApp Integration – Send messages, make calls, and even start video calls.

📡 Android Automation (ADB) – Place calls or send SMS via connected Android devices.

💻 Frontend UI – Built with HTML, CSS, JavaScript and animated with Eel for seamless desktop integration.

🎨 Chat History & Animations – Displays interactive responses with animations in the frontend.

🛠️ Tech Stack

Backend: Python 3, Eel

Frontend: HTML, CSS, JavaScript

Voice & AI: SpeechRecognition, pyttsx3, pvporcupine (Hotword), Groq API

Face Recognition: OpenCV (LBPH model)

Automation: PyAutoGUI, PyWhatKit, ADB tools

Database: SQLite (commands & contacts)

📂 Project Structure
Jarvis/
│── run.py              # Entry point – runs main Jarvis & hotword processes
│── main.py             # Starts frontend + face authentication
│── features.py         # Core assistant features (chat, hotword, YouTube, WhatsApp, etc.)
│── engine/             # Authentication, commands, configs, database
│── www/                # Frontend (HTML, CSS, JS, animations)
│── envjarvis/          # Virtual environment

⚡ Installation

Clone the repository:

git clone(https://github.com/farhanparvaiz27dev/python-jarvis)
cd jarvis


Create a virtual environment:

python -m venv envjarvis
source envjarvis/Scripts/activate   # On Windows
source envjarvis/bin/activate       # On Linux/Mac


Install dependencies:

pip install -r requirements.txt


Add your API key (Groq or other LLM provider) in:

features.py → client = Groq(api_key="your_api_key_here")


Start Jarvis:

python run.py

🖥️ Usage

Say "Jarvis" or "Alexa" to wake the assistant.

Authenticate via Face Recognition.

Give commands like:

"Open Chrome"

"Play music on YouTube"

"Send WhatsApp message to Ali"

"Tell me a joke"

Interact with Jarvis through the frontend UI.

📸 Screenshots / Demo

(Add your screenshots or demo video here)

🔑 Hotkeys

Wake word: "Jarvis" / "Alexa"

Shortcut: Win + J (auto-pressed when hotword detected).

📜 License

This project is open-source and available under the MIT License.
cd jarvis


Create a virtual environment:

python -m venv envjarvis
source envjarvis/Scripts/activate   # On Windows
source envjarvis/bin/activate       # On Linux/Mac
Install dependencies:
pip install -r requirements.txt
Add your API key (Groq or other LLM provider) in:
features.py → client = Groq(api_key="your_api_key_here")
Start Jarvis:
python run.py
🖥️ Usage
Say "Jarvis" or "Alexa" to wake the assistant.
Authenticate via Face Recognition.

Give commands like:
"Open Chrome"
"Play music on YouTube"
"Send WhatsApp message to Ali"
"Tell me a joke"
Interact with Jarvis through the frontend UI.

🔑 Hotkeys
Wake word: "Jarvis" / "Alexa"
Shortcut: Win + J (auto-pressed when hotword detected).

📜 License
This project is open-source and available under the MIT License.

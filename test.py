from datetime import datetime
import pyttsx3

engine = pyttsx3.init()

current_dateTime = datetime.now()

engine.say(f'Today is {current_dateTime: %B %d, %Y}')
engine.runAndWait()
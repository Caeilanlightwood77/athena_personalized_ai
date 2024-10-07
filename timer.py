from time import sleep
import pyttsx3

engine = pyttsx3.init()

def timer():
    engine.say("Enter the time in minutes")
    engine.runAndWait()
    user = float(input("Enter the time in minutes: "))
    minute = user * 60
    incorrect = "Incorrect syntax inputted!"
    correct = "Countdown starting in..."
    time_is_up = "Time is up."
    goodluck = "Good luck!!!"
    checker = isinstance(user, float)

    if(checker == False):
        engine.say(incorrect)
        engine.runAndWait()
        return timer()
    else:
        engine.say(correct)
        engine.runAndWait()

        for i in range(3,0,-1):
            engine.say(i)
            engine.runAndWait()

        engine.say(goodluck)
        engine.runAndWait()
        sleep(minute)
        
    engine.say(time_is_up)
    engine.runAndWait()


if __name__ == "__main__":
    timer()







    

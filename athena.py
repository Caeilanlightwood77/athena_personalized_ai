from time import sleep
import stdiomask
import getpass
from timetable import timetable
from timer import timer
from random import randint
from number_generator import random_number
import pyttsx3

engine = pyttsx3.init()

# Loop program if user does not want to end
def loop():
    try:
        # Local variables for manipulation
        no_response = ["nothing", "exit", "end program","no"]
        timetable_response = ["timetable", "open timetable", "execute timetable"]
        timer_response = ["timer", "open timer", "execute timer"]
        random_number_response = ["random number", "open random number", "execute random number",
                                  "generate a random number", "execute random number generator"]
        user_question = ["How else can I help you, Sir? ", "Is there anything else that I can help you with? ",
                         "Would like me to do something else, Sir? "]
        
        x = randint(0, len(user_question) - 1)
        engine.say(user_question[x])
        engine.runAndWait()
        user = input(f'\n{user_question[x]}').lower()

        if user in no_response:
            return 1
        elif user in timetable_response:
            timetable()
            return loop()
        elif user in timer_response:
            timer()
            return loop()
        elif user in random_number_response:
            random_number()
            return loop()
        else:
            return 0
    except Exception as e:
        engine.say("An error occurred. Ending the program.")
        engine.runAndWait()
        print(f"Error: {e}")
        return 0


def login():
    try:
        username = "HelloWorld"
        password = "H3ll0W0rld"

        no_response = ["nothing", "exit", "end program"]
        yes_answer = ["yes", "y"]
        no_answer = ["no", "n"]
        timetable_response = ["timetable", "open timetable", "execute timetable"]
        timer_response = ["timer", "open timer", "execute timer"]
        random_number_response = ["random number", "open random number", "execute random number",
                                  "generate a random number", "execute random number generator"]

        engine.say("Hello Sir. How can I help you today?")
        engine.runAndWait()
        user = input("Hello Sir. How can I help you today? ").lower()

        if user in no_response:
            engine.say("Ending the program in...")
            engine.runAndWait()
            for i in range(3, 0, -1):
                engine.say(i)
                engine.runAndWait()
            engine.say("Have a nice day, Sir.")
            engine.runAndWait()
        else:
            counter = 0
            while counter != 1:
                engine.say("Please provide your username and password, Sir.")
                engine.runAndWait()
                
                try:
                    user_username = stdiomask.getpass(prompt="Username: ")
                    user_password = getpass.getpass()
                except Exception as e:
                    print(f"Error: {e}")
                    continue

                if user_password == password and user_username == username:
                    inner_counter = 0
                    while inner_counter != 1:
                        try:
                            if user in timetable_response:
                                engine.say("Executing the timetable program.")
                                engine.runAndWait()
                                timetable()
                            elif user in timer_response:
                                engine.say("Executing the timer program.")
                                engine.runAndWait()
                                timer()
                            elif user in random_number_response:
                                engine.say("Executing the random number program.")
                                engine.runAndWait()
                                random_number()
                            else:
                                engine.say("Error 404. Ending the program.")
                                engine.runAndWait()
                                inner_counter += 1
                                break

                            engine.say("Would you like me to end the program?")
                            engine.runAndWait()
                            exit_program = input("\nWould you like to end the program? (Yes/No) ").lower()

                            if exit_program in yes_answer:
                                engine.say("Ending the program in...")
                                engine.runAndWait()
                                for i in range(3, 0, -1):
                                    engine.say(i)
                                    engine.runAndWait()
                                engine.say("Have a nice day, Sir.")
                                engine.runAndWait()
                                inner_counter += 1
                                break
                            elif exit_program in no_answer:
                                looping = loop()
                                if looping == 1:
                                    engine.say("Ending the program in...")
                                    engine.runAndWait()
                                    for i in range(3, 0, -1):
                                        engine.say(i)
                                        engine.runAndWait()
                                    engine.say("Have a nice day, Sir.")
                                    engine.runAndWait()
                                    inner_counter += 1
                                    break
                                elif looping == 0:
                                    engine.say("Error 404. Ending the program in...")
                                    engine.runAndWait()
                                    for i in range(3, 0, -1):
                                        engine.say(i)
                                        engine.runAndWait()
                                    engine.say("Have a nice day, Sir.")
                                    engine.runAndWait()
                                    inner_counter += 1
                                    break
                        except Exception as e:
                            engine.say("An error occurred. Ending the program.")
                            engine.runAndWait()
                            print(f"Error: {e}")
                            inner_counter += 1
                else:
                    engine.say("Username and password do not match.")
                    engine.runAndWait()
                    exit_program = input("\nWould you like to end the program? (Yes/No) ").lower()

                    if exit_program in yes_answer:
                        engine.say("Ending the program in...")
                        engine.runAndWait()
                        for i in range(3, 0, -1):
                            engine.say(i)
                            engine.runAndWait()
                        engine.say("Have a nice day, Sir.")
                        engine.runAndWait()
                        counter += 1
                    elif exit_program in no_answer:
                        counter = 0
        exit()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        engine.say("An unexpected error occurred. Ending the program.")
        engine.runAndWait()


if __name__ == "__main__":
    login()

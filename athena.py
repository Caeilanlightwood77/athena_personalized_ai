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
    # Local variables for manipulation
    # Possible user answers
    no_response = ["nothing", "exit", "end program","no"]
    timetable_response = ["timetable", "open timetable", "execute timetable"]
    timer_response = ["timer", "open timer", "execute timer"]
    random_number_response = ["random number", "open random number", "execute random number",
                              "generate a random number", "execute random number generator"]
    user_question = ["How else can I help you, Sir? ", "Is there anything else that I can help you with? ",
                     "Would like me to do something else, Sir? "]
    text = ""

    # Indicate the end of the program
    exit_number = 0

    # Get answer from user
    x = randint(0, len(user_question) - 1)
    engine.say(user_question[x])
    engine.runAndWait()
    user = input(f'\n{user_question[x]}').lower()

    if user in no_response:
        exit_number = 1
        return exit_number
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
        exit_number = 0
        return exit_number


def login():
    # Saved username and password
    username = "HelloWorld"
    password = "H3ll0W0rld"

    # Local variable for manipulation
    text = ""

    # Possible user answers
    no_response = ["nothing", "exit", "end program"]
    yes_answer = ["yes", "y"]
    no_answer = ["no", "n"]
    timetable_response = ["timetable", "open timetable", "execute timetable"]
    timer_response = ["timer", "open timer", "execute timer"]
    random_number_response = ["random number", "open random number", "execute random number",
                              "generate a random number", "execute random number generator"]

    # Get answer from user
    engine.say(" Hello Sir. How can I help you today? ")
    engine.runAndWait()
    user = input("Hello Sir. How can I help you today? ").lower()

    if user in no_response:
        text = " Ending the program in..."
        engine.say(text)
        engine.runAndWait()
        for i in range(3, 0, -1):
            engine.say(i)
            engine.runAndWait()
        text = " Have a nice day, Sir."
        engine.say(text)
        engine.runAndWait()
    else:
        counter = 0
        while counter != 1:
            text = " Please provide your username and password, Sir."
            engine.say(text)
            engine.runAndWait()
            # Ask user for username and password. Username and password are hidden while typed
            user_username = stdiomask.getpass(prompt="Username: ")
            user_password = getpass.getpass()

            # If values match with the saved username and password
            if user_password == password and user_username == username:
                inner_counter = 0
                # While loop to repeat programs
                while inner_counter != 1:
                    if user in timetable_response:
                        text = " Executing the timetable program."
                        engine.say(text)
                        engine.runAndWait()
                        timetable()
                    elif user in timer_response:
                        text = " Executing the timer program."
                        engine.say(text)
                        engine.runAndWait()
                        timer()
                    elif user in random_number_response:
                        text = " Executing the random number program."
                        engine.say(text)
                        engine.runAndWait()
                        random_number()
                    else:
                        text = " Error 404. Ending the program."
                        engine.say(text)
                        engine.runAndWait()
                        inner_counter += 1
                        break

                    # Ask user if he/she wants to end the program
                    engine.say(" Would you like me to end the program?")
                    engine.runAndWait()
                    exit_program = input("\nWould you like to end the program?(Yes/No) ").lower()

                    if exit_program in yes_answer:
                        text = " Ending the program in..."
                        engine.say(text)
                        engine.runAndWait()
                        for i in range(3, 0, -1):
                            engine.say(i)
                            engine.runAndWait()
                        text = " Have a nice day, Sir."
                        engine.say(text)
                        engine.runAndWait()
                        # Break the inner_counter while loop
                        inner_counter += 1
                        break
                    elif exit_program in no_answer:
                        # Call loop function
                        looping = loop()
                        # If there's no error from the function looping
                        if looping == 1:
                            text = " Ending the program in..."
                            engine.say(text)
                            engine.runAndWait()
                            for i in range(3, 0, -1):
                                engine.say(i)
                                engine.runAndWait()
                            text = " Have a nice day, Sir."
                            engine.say(text)
                            engine.runAndWait()
                            # Break the inner_counter while loop
                            inner_counter += 1
                            break
                        # If there's an error from the function looping
                        elif looping == 0:
                            text = " Error 404. Ending the program in..."
                            engine.say(text)
                            engine.runAndWait()
                            for i in range(3, 0, -1):
                                engine.say(i)
                                engine.runAndWait()
                            text = " Have a nice day, Sir."
                            engine.say(text)
                            engine.runAndWait()
                            # Break the inner_counter while loop
                            inner_counter += 1
                            break
                    else:
                        text = " Error 404. Ending the program in..."
                        engine.say(text)
                        engine.runAndWait()
                        for i in range(3, 0, -1):
                            engine.say(i)
                            engine.runAndWait()
                        text = " Have a nice day, Sir."
                        engine.say(text)
                        engine.runAndWait()
                        # Break the inner_counter while loop
                        inner_counter += 1
                        break
                # Break the counter while loop
                counter += 1
            # Give chance to user if password and username does not match
            else:
                text = " Username and password does not match."
                engine.say(text)
                engine.runAndWait()
                # Ask user if he/she wants to end the program
                engine.say(" Would you like me to end the program? ")
                engine.runAndWait()
                exit_program = input("\nWould you like to end the program? (Yes/No) ").lower()

                if exit_program in yes_answer:
                    text = " Ending the program in..."
                    engine.say(text)
                    engine.runAndWait()
                    for i in range(0, 3, -1):
                        engine.say(i)
                        engine.runAndWait()
                    text = " Have a nice day, Sir."
                    engine.say(text)
                    engine.runAndWait()
                    counter += 1
                elif exit_program in no_answer:
                    counter = 0
        exit()


if __name__ == "__main__":
    login()

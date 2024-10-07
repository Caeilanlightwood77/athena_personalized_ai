from random import randint, random
from time import sleep
import pyttsx3
# Generate a number between the criteria provide by the user

engine = pyttsx3.init()

def float_number():

    engine.say("Enter start number")
    engine.runAndWait()
    start_number = float(input("Enter start number: "))

    engine.say("Enter end number")
    engine.runAndWait()
    end_number = float(input("Enter end number: "))

    yes_answer = ["yes", "end program","y"]
    no_answer = ["no", "continue","n"]

    exit_number = 0
    
    while(exit_number != 1):
        fl_number = (random() * end_number) + start_number
        engine.say(f'Random number: {fl_number:.2f}')
        engine.runAndWait()
        print(f'Random number: {fl_number:.2f}\n')
        
        engine.say("Would you like me to generate another float number?")
        engine.runAndWait()
        exit_program = input("Would you like me to generate another float number? ")

        if(exit_program in yes_answer):
            exit_number = 0
        elif(exit_program in no_answer):
            exit_number += 1
        else:
            engine.say("Error 404. Random generation of float number has ended.")
            engine.runAndWait()
            exit_number += 1

    engine.say("Ending random generation of float number.")
    engine.runAndWait()

def int_number():
    
    engine.say("Enter start number")
    engine.runAndWait()
    start_number = int(input("Enter start number: "))

    engine.say("Enter end number")
    engine.runAndWait()
    end_number = int(input("Enter end number: "))

    yes_answer = ["yes", "end program","y"]
    no_answer = ["no", "continue","n"]

    exit_number = 0

    while(exit_number != 1):
        integer_number = randint(start_number, end_number)
        engine.say(f'Random number: {integer_number}')
        engine.runAndWait()
        print(f'Random number: {integer_number}\n')

        engine.say("Would you like me to generate another integer number?")
        engine.runAndWait()

        exit_program = input("Would you like me to generate another integer number? ")

        if(exit_program in yes_answer):
            exit_number = 0
        elif(exit_program in no_answer):
            exit_number += 1
        else:
            engine.say("Error 404. Random generation of integer number has ended.")
            engine.runAndWait()
            exit_number += 1

    engine.say("Ending random generation of integer number.")
    engine.runAndWait()

def random_number():
    engine.say("Would you like me to create a float number or integer number?")
    engine.runAndWait()
    user = input("Would you like me to create a float number or integer number? ").lower()

    float_numbers = ["generate a float number", "float number","float"]
    int_numbers = ["generate an integer number", "integer number","integer"]

    if(user in float_numbers):
        float_number()
    elif(user in int_numbers):
        int_number()
    else:
        engine.say("Error 404. Random number generator has ended.")
        engine.runAndWait()

if __name__ == "__main__":
    random_number()

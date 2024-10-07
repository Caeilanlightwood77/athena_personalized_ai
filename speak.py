"""
import pyttsx3

engine = pyttsx3.init()

user = input("Which calculation would you like me to do? ").lower()

match user:
    case "addition":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

        addition = x + y

        engine.say(f'{x} + {y} = {addition}')
        engine.runAndWait()

        print(f'{x} + {y} = {addition}')

    case "subtraction":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

        subtraction = x - y

        engine.say(f'{x} minus {y} = {subtraction}')
        engine.runAndWait()

        print(f'{x} - {y} = {subtraction}')
    
    case "division":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

        division = x / y

        engine.say(f'{x} divided by {y} = {division}')
        engine.runAndWait()

        print(f'{x} / {y} = {division}')


    case "multiplication":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

        multiplication = x * y

        engine.say(f'{x} times {y} = {multiplication}')
        engine.runAndWait()

        print(f'{x} x {y} = {multiplication}')

    case _:
        
        engine.say("Invalid Input")
        engine.runAndWait()
        print("Invalid Input")
"""

import pyttsx3

engine = pyttsx3.init()

user = input("What kind of calculation would you like me to do?").lower()

match user:
    case "addition":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

        addition = x + y

        engine.say(f'{x} + {y} = {addition}')
        engine.runAndWait()

        print(f'{x} + {y} = {addition}')

    case "subtraction":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

        subtraction = x - y

        engine.say(f'{x} minus {y} = {subtraction}')
        engine.runAndWait()

        print(f'{x} - {y} = {subtraction}')
    
    case "division":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

        division = x / y

        engine.say(f'{x} divided by {y} = {division}')
        engine.runAndWait()

        print(f'{x} / {y} = {division}')


    case "multiplication":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

        multiplication = x * y

        engine.say(f'{x} times {y} = {multiplication}')
        engine.runAndWait()

        print(f'{x} x {y} = {multiplication}')

    case _:
        
        engine.say("Invalid Input")
        engine.runAndWait()
        print("Invalid Input")
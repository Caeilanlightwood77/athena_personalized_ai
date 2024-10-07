from time import sleep
import pyttsx3
# Arrange numbers on the criteria given by the user

engine = pyttsx3.init()

# Arrange numbers in ascending order
def arrange_ascending():
    number_list = []
    engine.say("How many numbers are there? ")
    engine.runAndWait()
    quantity = int(input("How many numbers are there? "))

    for i in range(1,quantity + 1,1):
        engine.say(f'What is number {i}?')
        engine.runAndWait()
        number = float(input(f'What is number {i}? '))
        number_list.append(number)
    
    number_list.sort()

    print(f'Ascending list: {number_list}')


# Arrange numbers in descending order
def arrange_descending():
    number_list = []
    engine.say("How many numbers are there?")
    engine.runAndWait()
    quantity = int(input("How many numbers are there? "))

    for i in range(1,quantity + 1,1):
        engine.say(f'What is number {i}?')
        engine.runAndWait()
        number = float(input(f'What is number {i}? '))
        number_list.append(number)
    
    number_list.sort(reverse = True)

    print(f'Descending list: {number_list}')
    

def arrange_number():
    engine.say("Which order would you like me to arrage the numbers?")
    engine.runAndWait()
    order = input("Which order would you like me to arrange the numbers? ").lower()
    text = ""
    if(order == "ascending order"):
        arrange_ascending()
    elif(order == "descending order"):
        arrange_descending()
    else:
        text = "Error 404. Ending the program in..."
        engine.say(text)
        engine.runAndWait()
        for i in range(3,0,-1):
            engine.say(i)
            engine.runAndWait()
        text = "End of program"

if __name__ == "__main__":
    arrange_number()
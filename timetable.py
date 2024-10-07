import datetime
from time import sleep
import pyttsx3

engine = pyttsx3.init()

def timetable_list():
    subjects = {
        "monday": ["PE 1","PE 1","PE 1","PE 1","ITE 10","ITE 10","No Class","STS","STS","STS",\
        "No class","No class","No class","SE 101","SE 101","SE 101","PC","PC","PC","CSC","CSC","CSC"],

        "tuesday": ["No class","No class","No class","No class","ITE 11","ITE 11","ITE 11",\
        "No class","No class","No class","No class","No class","No class","No class","No class",\
        "No class","ITE 15","ITE 15","ITE 15","No class","No class","No class"],

        "wednesday": ["No class","ITE 10","ITE 10","ITE 10","ITE 10","ITE 10","ITE 10","ITE 11",\
        "ITE 11","ITE 11","ITE 11","ITE 11","ITE 11","CSC","CSC","CSC","CSC","CSC","CSC","CSC","CSC","CSC"],

        "thursday": ["No class","No class","No class","No class","ITE 10","ITE 10","No class","STS","STS",\
        "STS","No class","No class","No class","No class","No class","No class","PC","PC","PC","CSC","CSC","No class"],

        "friday": ["No class","No class","No class","No class","ITE 11","ITE 11","ITE 11","No class","No class",\
        "No class","No class","No class","No class","No class","No class","No class","ITE 15","ITE 15","ITE 15",\
        "No class","No class","No class"],

        "saturday": ["No class","No class","No class","No class","NSTP 1","NSTP 1","NSTP 1","NSTP 1","NSTP 1","NSTP 1",\
        "NSTP 1","NSTP 1","No class","No class","No class","No class","No class","No class","No class","No class",\
        "No class","No class"]
    }

    return subjects

def time():
    hours = ["07:00 - 07:30","07:30 - 08:00","08:00 - 08:30","08:30 - 09:00","09:00 - 09:30",\
    "09:30 - 10:00","10:00 - 10:30","10:30 - 11:00","11:00 - 11:30","11:30 - 12:00","12:00 - 12:30", \
    "12:30 - 13:00","13:00 - 13:30","13:30 - 14:00","14:00 - 14:30","14:30 - 15:00","15:00 - 15:30", \
    "15:30 - 16:00","16:00 - 16:30","16:30 - 17:00","17:00 - 17:30","17:30 - 18:00"]

    return hours

def timetable():
    # Local variables for manipulation. This checks the current day of the week
    x = datetime.datetime.now()
    day = x.strftime("%A")
    subjects = timetable_list()
    hours = time()

    # List for every day
    monday = subjects["monday"]
    tuesday = subjects["tuesday"]
    wednesday = subjects["wednesday"]
    thursday = subjects["thursday"]
    friday = subjects["friday"]

    # Title names
    timetable_name = "Timetable"
    subjects_name = "Subjects"
    hours_name = "    Time     "

    title = f'{timetable_name}'
    heading = f'| {hours_name} {" " * ((len(hours[0]) -1) - len(hours[0]))} | {subjects_name} {" " * ((len(hours[0]) - 1) - len(hours[0]))}|'

    # User's possible answers
    yes_answer = ["yes","y"]
    no_answer = ["no","n"]
    days_answer = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

    # Question for the user
    engine.say("Would you like to see today's timetable?")
    engine.runAndWait()
    user = input("Would you like to see today's timetable? (Yes/No) ").lower()

    if(user in yes_answer):
        if(day == "Monday"):
            print("\nMonday\n")
            print(title + "\n\n" + heading)
            for i in range(len(hours)):
                row = f'| {hours[i]} {" " * ((len(hours[i]) - 1) - len(hours[i]))} | {monday[i]} {" " * ((len(subjects_name) - 1) - len(monday[i]))} |'
                print(row)
        elif(day == "Tuesday"):
            print("\nTuesday\n")
            print(title + "\n\n" + heading)
            for i in range(len(hours)):
                row = f'| {hours[i]} {" " * ((len(hours[i]) - 1) - len(hours[i]))} | {tuesday[i]} {" " * ((len(subjects_name) - 1) - len(tuesday[i]))} |'
                print(row)
        elif(day == "Wednesday"):
            print("\nWednesday\n")
            print(title + "\n\n" + heading)
            for i in range(len(hours)):
                row = f'| {hours[i]} {" " * ((len(hours[i]) - 1) - len(hours[i]))} | {wednesday[i]} {" " * ((len(subjects_name) - 1) - len(wednesday[i]))} |'
                print(row)
        elif(day == "Thursday"):
            print("\nThursday\n")
            print(title + "\n\n" + heading)
            for i in range(len(hours)):
                row = f'| {hours[i]} {" " * ((len(hours[i]) - 1) - len(hours[i]))} | {thursday[i]} {" " * ((len(subjects_name) - 1) - len(thursday[i]))} |'
                print(row)
        elif(day == "Friday"):
            print("\nFriday\n")
            print(title + "\n\n" + heading)
            for i in range(len(hours)):
                row = f'| {hours[i]} {" " * ((len(hours[i]) - 1) - len(hours[i]))} | {friday[i]} {" " * ((len(subjects_name) - 1) - len(friday[i]))} |'
                print(row)
        elif(day == "Saturday"):
            engine.say("Today is Saturday. You don't have anything on saturdays")
            engine.runAndWait()
        else:
            engine.say("Today is Sunday. You don't have anything on sundays")
            engine.runAndWait()
    elif(user in no_answer):
        engine.say("Which day would you like to see your timetable on?")
        engine.runAndWait()
        user = input("Which day would you like to see your timetable on? ").lower()

        if(user in days_answer):
            if(user == "monday"):
                print("Monday\n")
                print(title + "\n\n" + heading)
                for i in range(len(hours)):
                    row = f'| {hours[i]} {" " * ((len(hours[i]) - 1) - len(hours[i]))} | {monday[i]} {" " * ((len(subjects_name) - 1) - len(monday[i]))} |'
                    print(row)
            elif(user == "tuesday"):
                print("Tuesday\n")
                print(title + "\n\n" + heading)
                for i in range(len(hours)):
                    row = f'| {hours[i]} {" " * ((len(hours[i]) - 1) - len(hours[i]))} | {tuesday[i]} {" " * ((len(subjects_name) - 1) - len(tuesday[i]))} |'
                    print(row)
            elif(user == "wednesday"):
                print("Wednesday\n")
                print(title + "\n\n" + heading)
                for i in range(len(hours)):
                    row = f'| {hours[i]} {" " * ((len(hours[i]) - 1) - len(hours[i]))} | {wednesday[i]} {" " * ((len(subjects_name) - 1) - len(wednesday[i]))} |'
                    print(row)
            elif(user == "thursday"):
                print("Thursday\n")
                print(title + "\n\n" + heading)
                for i in range(len(hours)):
                    row = f'| {hours[i]} {" " * ((len(hours[i]) - 1) - len(hours[i]))} | {thursday[i]} {" " * ((len(subjects_name) - 1) - len(thursday[i]))} |'
                    print(row)
            elif(user == "friday"):
                print("Friday\n")
                print(title + "\n\n" + heading)
                for i in range(len(hours)):
                    row = f'| {hours[i]} {" " * ((len(hours[i]) - 1) - len(hours[i]))} | {friday[i]} {" " * ((len(subjects_name) - 1) - len(friday[i]))} |'
                    print(row)
            elif(user == "saturday"):
                engine.say("You don't have anything on saturdays")
                engine.runAndWait()
            else:
                engine.say("You don't have anything on sundays")
                engine.runAndWait()
        else:
            engine.say("Error 404. Ending the program...")
            engine.runAndWait()
            for timer in range(3,0,-1):
                engine.say(timer)
                engine.runAndWait()

            exit()
    else:
        engine.say("Error 404. Ending the program...")
        engine.runAndWait()
        for timer in range(3,0,-1):
            engine.say(timer)
            engine.runAndWait()
        exit()
   


if __name__ == "__main__":
    timetable()





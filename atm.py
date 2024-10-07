from random import randint

"""
Automated Teller Machine

Available Money Bills
1000,500,100,50,20,10,5

"""

# Functions
# Generate a value divisible by 5
def withdrawn_amount():
    amount_withdrawn = round(randint(1,2000))

    if(amount_withdrawn % 5 == 0):
        return amount_withdrawn
    else:
        return withdrawn_amount()


# Check the nature of the value
def check_money(money):
    text = ""

    if(money >= 1000):
            text += "thousand"
    elif(money >= 500 and money < 1000):
        text += "five hundred"
    elif(money >= 100 and money < 500):
        text += "one hundred"
    elif(money >= 50 and money < 100):
        text += "fifty"
    elif(money >= 20 and money < 50):
        text += "twenty"
    elif(money >= 10 and money < 20):
        text += "ten"
    elif(money >= 5 and money < 10):
        text += "five"

    return text

# The actor for the function atm()
def helper(money):
    multiplier = 0
    remainder = 0
    checker = check_money(money)

    if(checker == "thousand"):
        remainder = money % 1000
        money -= remainder
        multiplier = money / 1000
        money = remainder
    elif(checker == "five hundred"):
        remainder = money % 500
        money -= remainder
        multiplier = money / 500
        money = remainder
    elif(checker == "one hundred"):
        remainder = money % 100
        money -= remainder
        multiplier = money / 100
        money = remainder
    elif(checker == "fifty"):
        remainder = money % 50
        money -= remainder
        multiplier = money / 50
        money = remainder
    elif(checker == "twenty"):
        remainder = money % 20
        money -= remainder
        multiplier = money / 20
        money = remainder
    elif(checker == "ten"):
        remainder = money % 10
        money -= remainder
        multiplier = money / 10
        money = remainder
    elif(checker == "five"):
        remainder = money % 5
        money -= remainder
        multiplier = money / 5
        money = remainder

    return multiplier

# ATM function
def atm(money, money_list):
    checker = check_money(money)

    if(money != 0):
        multiplier = helper(money)
        if(checker == "thousand"):
            money_list[0] = multiplier
            return atm(money, money_list)
        elif(checker == "five hundred"):
            money_list[1] = multiplier
            return atm(money, money_list)
        elif(checker == "one hundred"):
            money_list[2] = multiplier
            return atm(money, money_list)
        elif(checker == "fifty"):
            money_list[3] = multiplier
            return atm(money, money_list)
        elif(checker == "twenty"):
            money_list[4] = multiplier
            return atm(money, money_list)
        elif(checker == "ten"):
            money_list[5] = multiplier
            return atm(money, money_list)
        elif(checker == "five"):
            money_list[6] = multiplier
            return atm(money, money_list)


# Global variable for manipulation
money = withdrawn_amount()
money_list = [0,0,0,0,0,0,0]
automatedMoney = atm(money, money_list)
print("Requested amout: ", money, "\nMoney List: ", money_list)

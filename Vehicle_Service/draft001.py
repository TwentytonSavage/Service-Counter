import time

name = input("Hello, can I have your name?: ")
info = input(f"Alright, {name}, can I have the make and model of you car please?: ")
mileage = input(f"Whats the mileage on your, {info}?: ")
issue = input(f"What seems to be the problem, {name}, with your, {info}?: ")

if issue == ("Oil Change"):
    print(f"Alright, {name}, we will get that oil changed for you on your, {info}.")
    time.sleep(2)
    print("That will be $79.99 or 112.99 for synthetic oil.")
    time.sleep(2)
    print("That's 115.53 Canadian")
    time.sleep(2)
    pay = input("Thank you for choosing Woonsocket Career Center auto garage, how would you like to pay?:")

    if pay == ("Cash"):
        print("Thank you for your payment, have a great day!")
    elif pay == ("Credit"):
        print("Alright just swipe your card here.")
        time.sleep(2)
        print("Thank you for your payment, have a great day!")
    elif pay == ("Debit"):
        print("Alright just swipe your card here.")
        time.sleep(2)
        print("Thank you for your payment, have a great day!")
    else:
        print("Sorry, we only accept cash, credit, or debit.")

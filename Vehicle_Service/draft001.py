import time

name = input("Hello, can I have your name?: ")
info = input(f"Alright, {name}, can I have the make and model of you car please?: ")
mileage = input(f"Whats the mileage on your, {info}?: ")
issue = input(f"What do you need done, {name}, with your {info}?: ")

if issue.lower() == "oil change":
    print(f"Alright, {name}, we will get that oil changed for you on your {info}.")
    time.sleep(2)
    print("That will be $79.99 or $112.99 for synthetic oil.")
    time.sleep(2)
    print("That's 115.53 Canadian.")
    time.sleep(2)
    pay = input("Thank you for choosing Woonsocket Career Center auto garage, how would you like to pay?: ")


    if pay == ("Cash"):
        print(f"Thank you for your payment, {name}, have a great day!")
    elif pay == ("Credit"):
        print("Alright just swipe your card here.")
        time.sleep(2)
        print("Prossesing...")
        time.sleep(2)
        print(f"Thank you for your payment, {name}, have a great day!")
    elif pay == ("Debit"):
        print("Alright just swipe your card here.")
        time.sleep(2)
        print("Prossesing...")
        time.sleep(2)
        print(f"Thank you for your payment, {name}, have a great day!")
    else:
        print("Sorry, we only accept cash, credit, or debit.")
    

elif issue.lower() == "tire rotation":
    tire = input(f"Alright, {name}, what kind of tires do you have on your {info}?: ")
    if tire.lower() == "standard":
        print(f"Alright, {name}, that will be $30.00 for that type of tire rotation.")
        time.sleep(2)
        print("That's 43.33 Canadian.")
        time.sleep(2)
    elif tire.lower() == "truck":
        print(f"Alright, {name}, that will be $45.00 for that type of tire rotation.")
        time.sleep(2)
        print("That's 64.99 Canadian.")
        time.sleep(2)
        pay = input("Thank you for choosing Woonsocket Career Center auto garage, how would you like to pay?:")
    if pay == ("Cash"):
        print(f"Thank you for your payment, {name}, have a great day!")
    elif pay == ("Credit"):
        print("Alright just swipe your card here.")
        time.sleep(2)
        print("Prossesing...")
        time.sleep(2)
        print(f"Thank you for your payment, {name}, have a great day!")
    elif pay == ("Debit"):
        print("Alright just swipe your card here.")
        time.sleep(2)
        print("Prossesing...")
        time.sleep(2)
        print(f"Thank you for your payment, {name}, have a great day!")
    else:
        print("Sorry, we only accept cash, credit, or debit.")
    

elif issue.lower() == "brake pad replacment and front end alignment":
    
    pads = input(f"Alright, {name}, would you like the standard or the package that does both of them for cheaper?: ")
    
    if pads.lower() == "standard":
        print(f"Alright, {name}, that will be $150.00 for the brake pad replacment.")
        time.sleep(2)
        print("That's 216.66 Canadian.")
        time.sleep(2)
    
    elif pads.lower() == "package":
        print(f"Alright, {name}, that will be $120.00 for the package.")
        time.sleep(2)
        print("That's 173.33 Canadian.")
        time.sleep(2)
    
    pay = input("Thank you for choosing Woonsocket Career Center auto garage, how would you like to pay?:")
    
    if pay == ("Cash"):
        print(f"Thank you for your payment, {name}, have a great day!")
    
    elif pay == ("Credit"):
        print("Alright just swipe your card here.")
        time.sleep(2)
        print("Prossesing...")
        time.sleep(2)
        print(f"Thank you for your payment, {name}, have a great day!")
   
    elif pay == ("Debit"):
        print("Alright just swipe your card here.")
        time.sleep(2)
        print("Prossesing...")
        time.sleep(2)
        print(f"Thank you for your payment, {name}, have a great day!")
   
    else:
        print("Sorry, we only accept cash, credit, or debit.")

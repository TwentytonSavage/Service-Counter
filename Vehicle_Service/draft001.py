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
else:
    print("Sorry, we only offer oil changes, tire rotations, brake pad replacments, and broken glass repair.")
    print("Thank you for choosing Woonsocket Career Center auto garage, have a great day!")
    pay = None
    
if pay:
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

if issue.lower() == "tire rotation":
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
else:
    print("Sorry, we only offer oil changes, tire rotations, brake pad replacments, and broken glass repair.")
    print("Thank you for choosing Woonsocket Career Center auto garage, have a great day!")
    
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
    

if issue.lower() == "brake pad replacment":
    pads = input(f"Alright, {name}, would you like the standard which only does the brake pads or the package that does both brake pad replacemnet and front end alignment?: ")
    
    if pads.lower() == "standard":
        print(f"Alright, {name}, that will be $100.00 for the brake pad replacment.")
        time.sleep(2)
        print("That's 144.43 Canadian.")
        time.sleep(2)
    
    elif pads.lower() == "package":
        print(f"Alright, {name}, that will be $120.00 for the package.")
        time.sleep(2)
        print("That's 173.33 Canadian.")
        time.sleep(2)
    else:
        print("Sorry, we only offer oil changes, tire rotations, brake pad replacments, and broken glass repair.")
        print("Thank you for choosing Woonsocket Career Center auto garage, have a great day!")
    
    
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

elif issue.lower() == "broken glass repair":
    glass = input(f"Alright, {name}, is it a large or a small window that needs to be repaired on your {info}?: ")
    if glass.lower() == "front":
        print(f"Alright, {name}, that will be $69.99 for the large window.")
        time.sleep(2)
        print("That's 101.08 Canadian.")
        time.sleep(2)
    elif glass.lower() == "back":
        print(f"Alright, {name}, that will be $39.99 for the small window.")
        time.sleep(2)
        print("That's 57.76 Canadian.")
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
else:
    print("Sorry, we only offer oil changes, tire rotations, brake pad replacments, and broken glass repair.")
    print("Thank you for choosing Woonsocket Career Center auto garage, have a great day!")
    
    

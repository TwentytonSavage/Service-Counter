import time

name = input("Hello, can I have your name?: ")
info = input(f"Alright, {name}, can I have the make and model of your car please?: ")
mileage = input(f"What's the mileage on your {info}?: ")
issue = input(f"What do you need done, {name}, with your {info}?: ")

if issue.lower() == "oil change":
    print(f"Alright, {name}, we will get that oil changed for you on your {info}.")
    time.sleep(2)
    print("That will be $79.99 or $112.99 for synthetic oil.")
    time.sleep(2)
    print("That's 115.53 Canadian.")
    time.sleep(2)
    pay = input("Thank you for choosing Woonsocket Career Center auto garage, how would you like to pay?: ")

elif issue.lower() == "tire rotation":
    tire = input(f"Alright, {name}, what kind of tires do you have on your {info} (standard or truck)?: ")
    if tire.lower() == "standard":
        print(f"Alright, {name}, that will be $30.00 for that type of tire rotation.")
        time.sleep(2)
        print("That's 43.33 Canadian.")
    elif tire.lower() == "truck":
        print(f"Alright, {name}, that will be $45.00 for that type of tire rotation.")
        time.sleep(2)
        print("That's 64.99 Canadian.")
    else:
        print("Sorry, we only handle standard and truck tires.")
        exit()
    pay = input("Thank you for choosing Woonsocket Career Center auto garage, how would you like to pay?: ")

elif issue.lower() == "brake pad replacement":
    pads = input(f"Alright, {name}, would you like the 'standard' (brake pads only) or the 'package' (brake pads and front-end alignment)?: ")
    if pads.lower() == "standard":
        print(f"Alright, {name}, that will be $100.00 for the brake pad replacement.")
        time.sleep(2)
        print("That's 144.43 Canadian.")
    elif pads.lower() == "package":
        print(f"Alright, {name}, that will be $120.00 for the package.")
        time.sleep(2)
        print("That's 173.33 Canadian.")
    else:
        print("Sorry, we only offer the standard or package options for brake pad replacement.")
        exit()
    pay = input("Thank you for choosing Woonsocket Career Center auto garage, how would you like to pay?: ")

elif issue.lower() == "broken glass repair":
    glass = input(f"Alright, {name}, is it a 'front' or 'back' window that needs to be repaired on your {info}?: ")
    if glass.lower() == "front":
        print(f"Alright, {name}, that will be $69.99 for the large window.")
        time.sleep(2)
        print("That's 101.08 Canadian.")
    elif glass.lower() == "back":
        print(f"Alright, {name}, that will be $39.99 for the small window.")
        time.sleep(2)
        print("That's 57.76 Canadian.")
    else:
        print("Sorry, we only repair front or back windows.")
        exit()
    pay = input("Thank you for choosing Woonsocket Career Center auto garage, how would you like to pay?: ")

elif issue.lower() == "dent removal":
    dent_size = input(f"Alright, {name}, is it a 'big' or 'small' dent on your {info}?: ")
    if dent_size.lower() == "big":
        print(f"Alright, {name}, that will be $10.00 for the big dent removal.")
        time.sleep(2)
        print("That's 14.39 Canadian.")
    elif dent_size.lower() == "small":
        print(f"Alright, {name}, that will be $5.00 for the small dent removal.")
        time.sleep(2)
        print("That's 7.20 Canadian.")
    else:
        print("Sorry, we only handle big or small dents.")
        exit()
    pay = input("Thank you for choosing Woonsocket Career Center auto garage, how would you like to pay?: ")

else:
    print("Sorry, we only offer oil changes, tire rotations, brake pad replacements, broken glass repair, and dent removal.")
    print("Thank you for choosing Woonsocket Career Center auto garage, have a great day!")
    exit()

# Payment processing
if pay.lower() == "cash":
    print(f"Thank you for your payment, {name}, have a great day!")
elif pay.lower() == "credit":
    print("Alright, just swipe your card here.")
    time.sleep(2)
    print("Processing...")
    time.sleep(2)
    print(f"Thank you for your payment, {name}, have a great day!")
elif pay.lower() == "debit":
    print("Alright, just swipe your card here.")
    time.sleep(2)
    print("Processing...")
    time.sleep(2)
    print(f"Thank you for your payment, {name}, have a great day!")
else:
    print("Sorry, we only accept cash, credit, or debit.")

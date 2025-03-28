import time

name = input("Hello, can I have your name?: ")
info = input(f"Alright, {name}, can I have the make and model of your car please?: ")
mileage = input(f"What's the mileage on your {info}?: ")
issue = input(f"What do you need done, {name}, with your {info}?: ")

def process_payment(name):
    pay = input("Thank you for choosing Woonsocket Career Center auto garage, how would you like to pay?: ")
    if pay.lower() in ["credit", "debit"]:
        print(f"Alright just swipe your card here.")
        time.sleep(2)
        print("Processing...")
        time.sleep(2)
        print(f"Thank you for your payment, {name}, have a great day!")
    else:
        print("Sorry, we only accept credit or debit.")
    return pay

def handle_service(service_name, price_usd, price_cad):
    print(f"Alright, {name}, that will be ${price_usd:.2f} for {service_name}.")
    time.sleep(2)
    print(f"That's {price_cad:.2f} Canadian.")
    time.sleep(2)
    process_payment(name)

if issue.lower() == "oil change":
    handle_service("an oil change", 79.99, 115.53)

elif issue.lower() == "tire rotation":
    tire = input(f"Alright, {name}, what kind of tires do you have on your {info}?: ")
    if tire.lower() == "standard":
        handle_service("a standard tire rotation", 30.00, 43.33)
    elif tire.lower() == "truck":
        handle_service("a truck tire rotation", 45.00, 64.99)

elif issue.lower() == "brake pad replacement":
    pads = input(f"Alright, {name}, would you like the standard brake pad replacement or the package that includes front end alignment?: ")
    if pads.lower() == "standard":
        handle_service("a standard brake pad replacement", 100.00, 144.43)
    elif pads.lower() == "package":
        handle_service("brake pad replacement with front end alignment", 120.00, 173.33)

elif issue.lower() == "broken glass repair":
    glass = input(f"Alright, {name}, is it a large or a small window that needs to be repaired on your {info}?: ")
    if glass.lower() == "large":
        handle_service("a large window repair", 69.99, 101.08)
    elif glass.lower() == "small":
        handle_service("a small window repair", 39.99, 57.76)

else:
    print("Sorry, we only offer oil changes, tire rotations, brake pad replacements, and broken glass repair.")
    print("Thank you for choosing Woonsocket Career Center auto garage, have a great day!")
    
    

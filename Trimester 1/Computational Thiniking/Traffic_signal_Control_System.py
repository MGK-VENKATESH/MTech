traffic = int(input("Enter the number of Vehicles"))
emergency = input("Is there any emergency vehicle in Traffic or not?")

if emergency.lower() == "yes":
    print("Green Signal Immediatly")
else:
    if traffic > 50:
        print("Green for 90 seconds")
    elif traffic < 20:
        print("Green for 50 seconds")
    else:
        print("Green for 30 seconds")

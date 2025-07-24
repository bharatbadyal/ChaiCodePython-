cup_size = input("Enter your cup size prefrence (small,medium or large): ").lower()

if cup_size == "medium":
    print("The price of your Medium Cup is 10 rupees")
elif cup_size == "small":
    print("The price of your Small Cup is 5 rupees")
elif cup_size == "large":
    print("The price of your Large Cup is 15 rupees")
else:
    print("Unknown Cup size!!")
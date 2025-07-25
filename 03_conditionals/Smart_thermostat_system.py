from ast import Pass
device_status = input("Enter the device status (active or Off): ").lower()
temperature = int(input("Enter the temperature in Celcius: "))

# if device_status == "active" and temperature > 35:
#     print("Warning: High Temperature!!!!!")
# else:
#     print("Temperature is Normal")

if device_status == "active":
    if temperature >= 35:
        print("Warning: High Temperature!!!!!")
    else:
        print("Temeprature is Normal")
else:
    print("Device is offline")
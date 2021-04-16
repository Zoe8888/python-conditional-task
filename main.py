# Determining driver demerits
drivers_speed = int(input("Enter your speed in kilometers: "))
speed_limit = int(input("Enter speed limit in kilometers: "))
if speed_limit >= drivers_speed:
    print("OK")
elif drivers_speed > speed_limit:
    demerits = (drivers_speed - speed_limit) / 5
    print("Number of demerits: ", demerits)
    if demerits > 12:
        print("Go to jail")

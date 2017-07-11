def water_state(temp):
    if temp<0:
        print "ice"
    elif temp>100:
        print "steam"
    else:
        print "liquid"

print "enter the temperature reading in degrees centigrade"
temp = input("Temperature (C): ")

water_state(temp)

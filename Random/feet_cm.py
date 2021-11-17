def turn(num):
    num_2 = round(num * 100) / 100
    return num_2


enter = input("Enter in cm or feet?")
if enter == "cm":
    a = input("Height in cm: ")
    res = int(a) / 30.48
    b = turn(res)
    print(str(a) + " cm are: " + str(b) + " feet")
elif enter == "feet":
    a = input("Enter in feet: ")
    res = round(float(a) * 30.48)
    print(str(a) + " feet are: " + str(res) + " cm")
elif enter == "q" or enter == "Q":
    pass

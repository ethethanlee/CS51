problem = True
while problem:
    canausa = input("How do you want it converted? 1. F to C; 2. C to F\n")
    if canausa.isdigit():
        canausa = int(canausa)
        if 0 < canausa < 2:
            number = input("Temperature between 1 and 100 in Fahrenheit please: \n")
            if number.isdigit() and -1 < int(number) < 101:
                number = int(number)
                food = (number-32)*.555555555556
                food = "{:.3f}".format(food)
                food = str(food)
                print ("That is " + food + " C")
                problem = False
            else:
                print("Your input needs to be a valid positive integer between 1 and 100.")
        elif 1 < canausa < 3:
            numberr = input("Temperature between 1 and 100 in Celsius please: \n")
            if numberr.isdigit() and -1 < int(numberr) < 101:
                numberr = int(numberr)
                numberr = 1.8*numberr + 32
                numberr = "{:.3f}".format(numberr)
                numberr = str(numberr)
                print ("That is " + numberr + " F")
                problem = False
            else:
                print("Your input needs to be a valid positive integer between 1 and 100.")
        else:
            print("Your input needs to be 1 or 2. \n")
    else:
        print("Your input needs to be 1 or 2. \n")
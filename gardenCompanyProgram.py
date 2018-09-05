layingLawnPrice=15.50 #per m2
layingLawnTime=20 #mins per m2
Layingaconcretepatio £20.99 per m2
20 mins per m2
Laying a wooden deck £15.75 per m2
30 mins per m2
Digging and filling a rectangular pond £25.00 per m2
45 mins per m2
Installing a water feature (e.g. a fountain) £150.00 each 60 mins each
Installing garden lights £5.00 each 10 mins each


def startMenu():
    menuOption = input("""Press 1: Create Garden
Press 2: Reviews
Press 3: documents
Press 4: Exit
>>""")

    if menuOption == "1":
        name()
    elif menuOption == "2":
        reviews()
    elif menuOption == "3":
        documents()
    elif menuOption == "4":
        exit()
    else:
        print("invalid option")
        startMenu()


def writeToDocumnents():
    garden = open("garden.txt", "a")
    garden.write(
        name + ":\nLawn:\n" + theLawn +
        "\nConcrete patio:\n" + theConcretePatio +
        "\nWooden Deck:\n" + theWoodDeck \
        + "\nPond:\n" + thePond + "\nthe water feature:\n" + theWater + "\nGarden lights:\n" + theLawn + "\nTotal cost for materials:\n" \
        + totalCostForMats + "\nTotal cost for labour:\n" + totalCostForLabour + "\nTotal cost :\n" + totalCost)
    startMenu()


def name():
    global name
    name = input("What is your name:\n>>")
    wantLawn()


def wantLawn():
    global theLawn, totalPriceOfLawn, totalTimeOfLawn
    wantLawnAnswer = input("Do you want a lawn: y/n\n>>").lower()
    if wantLawnAnswer == "y":
        lengthOfLawn = float(input("Enter length of lawn:\n>> "))
        widthOfLawn = float(input("Enter width of lawn:\n>> "))
        totalSizeOfLawn = lengthOfLawn * widthOfLawn
        totalPriceOfLawn = totalSizeOfLawn * layingLawnPrice
        totalTimeOfLawn = totalSizeOfLawn * 20
        print("Price: £", totalPriceOfLawn, "m^2, Time to Take:", totalTimeOfLawn, "minutes")
        theLawn = "£" + str(totalPriceOfLawn) + "" + str(totalTimeOfLawn) + " minutes " \
                  + str(totalSizeOfLawn) + "m^2 (" + str(lengthOfLawn) + "m" + str(widthOfLawn) + "m)"
    elif wantLawnAnswer == "n":
        print("No lawn for you")
    else:
        print("Invalid Option, try again.")
        wantLawn()
    wantConcretePatio()


def wantConcretePatio():
    global theConcretePatio, totalPriceOfConcretePatio, totalTimeOfConcretePatio
    wantConcretePatioAnswer = input("Do you want a Concrete Patio: y/n\n>>").lower()
    if wantConcretePatioAnswer == "y":
        lengthOfConcretePatio = float(input("Enter length of Concrete Patio:\n>> "))
        widthOfConcretePatio = float(input("Enter width of Concrete Patio:\n>> "))
        totalSizeOfConcretePatio = lengthOfConcretePatio * widthOfConcretePatio
        totalPriceOfConcretePatio = totalSizeOfConcretePatio * 20.99
        totalTimeOfConcretePatio = totalSizeOfConcretePatio * 20
        print("Price: £", totalPriceOfConcretePatio, "m^2, Time to Take:", totalTimeOfConcretePatio, "minutes")
        theConcretePatio = "£" + str(totalPriceOfConcretePatio) + "" + str(
            totalTimeOfConcretePatio) + " minutes " + str(totalSizeOfConcretePatio) + \
                           "m^2 (" + str(lengthOfConcretePatio) + "m" + str(widthOfConcretePatio) + "m)"
    elif wantConcretePatioAnswer == "n":
        print("No Concrete Patio for you")
    else:
        print("Invalid Option, try again.")
        wantConcretePatio()
    wantWoodenDeck()


def wantWoodenDeck():
    global theWoodDeck, totalPriceOfWoodenDeck, totalTimeOfWoodenDeck
    wantWoodenDeckAnswer = input("Do you want a woodendeck: y/n\n>>").lower()
    if wantWoodenDeckAnswer == "y":
        lengthOfWoodenDeck = float(input("Enter length of WoodenDeck:\n>> "))
        widthOfWoodenDeck = float(input("Enter width of Wooden Deck:\n>> "))
        totalSizeOfWoodenDeck = lengthOfWoodenDeck * widthOfWoodenDeck
        totalPriceOfWoodenDeck = totalSizeOfWoodenDeck * 15.75
        totalTimeOfWoodenDeck = totalSizeOfWoodenDeck * 30
        print("Price: £", totalPriceOfWoodenDeck, "m^2, Time to Take:", totalTimeOfWoodenDeck, "minutes")
        theWoodDeck = "£" + str(totalPriceOfWoodenDeck) + "" + str(totalTimeOfWoodenDeck) + " minutes " + str(
            totalSizeOfWoodenDeck) + \
                      "m^2 (" + str(lengthOfWoodenDeck) + "m" + str(widthOfWoodenDeck) + "m)"
    elif wantWoodenDeckAnswer == "n":
        print("No WoodenDeck for you")
    else:
        print("Invalid Option, try again.")
        wantWoodenDeck()
    wantPond()


def wantPond():
    global thePond, totalPriceOfPond, totalTimeOfPond
    wantPondAnswer = input("Do you want a Pond: y/n\n>>").lower()
    if wantPondAnswer == "y":
        lengthOfPond = float(input("Enter length of WoodenDeck:\n>> "))
        widthOfPond = float(input("Enter width of Wooden Deck:\n>> "))
        totalSizeOfPond = lengthOfPond * widthOfPond
        totalPriceOfPond = totalSizeOfPond * 25
        totalTimeOfPond = totalSizeOfPond * 45
        print("Price: £", totalPriceOfPond, "m^2, Time to Take:", totalTimeOfPond, "minutes")
        thePond = "£" + str(totalPriceOfPond) + "" + str(totalTimeOfPond) + " minutes " + str(totalSizeOfPond) + \
                  "m^2 (" + str(lengthOfPond) + "m" + str(widthOfPond) + "m)"
    elif wantPondAnswer == "n":
        print("No Pond for you")
    else:
        print("Invalid Option, try again.")
        wantPond()
    wantWaterFeature()


def wantWaterFeature():
    global theWater, priceOfWaterFeature, timeToTakeForWaterFeature
    wantWaterFeatureAnswer = input("Want a water feature y/n:\n>>").lower()
    if wantWaterFeatureAnswer == "y":
        howManyWaterFeatures = float(input("How many water featres do you want:\n>>"))
        priceOfWaterFeature = howManyWaterFeatures * 150
        timeToTakeForWaterFeature = howManyWaterFeatures * 60
        print("Price: £", priceOfWaterFeature, "m^2, Time to Take:", timeToTakeForWaterFeature, "minutes")
        theWater = "£" + str(priceOfWaterFeature) + "" + str(timeToTakeForWaterFeature) + " minutes " + str(
            howManyWaterFeatures) + "water features"
    elif wantWaterFeatureAnswer == "n":
        print("No water feature for you:")
    else:
        print("Invalid Option, try again.")
        wantWaterFeature()
    wantLamp()


def wantLamp():
    global theLamp, priceOflamp, timeToTakeForlamp
    wantlampAnswer = input("Want a water feature y/n:\n>>").lower()
    if wantlampAnswer == "y":
        howManylamp = float(input("How many water featres do you want:\n>>"))
        priceOflamp = howManylamp * 5
        timeToTakeForlamp = howManylamp * 10
        print("Price: £", priceOflamp, "m^2, Time to Take:", timeToTakeForlamp, "minutes")
        thelamp = "£" + str(priceOflamp) + "" + str(timeToTakeForlamp) + " minutes " + str(howManylamp) + "lamps"
    elif wantlampAnswer == "n":
        print("No lamp for you:")
    else:
        print("Invalid Option, try again.")
        wantLamp()

    writeToDocumnents()


def totalCosts():
    global totalCostForLabour, totalCostForMats, totalCost
    totalCostForMats = totalPriceOfLawn + totalPriceOfConcretePatio + totalPriceOfWoodenDeck + totalPriceOfPond + priceOfWaterFeature + priceOflamp
    totalLabourTime = totalTimeOfLawn + totalTimeOfConcretePatio + totalTimeOfWoodenDeck + totalTimeOfPond + timeToTakeForWaterFeature + timeToTakeForlamp
    hourlyCharge = 1649
    totalCostForLabour = hourlyCharge * (totalLabourTime / 60)


def documents():
    pass


def reviews():
    pass


startMenu()

def startMenu():
    menuOption = input("""Press 1: Create Garden
Press 2: Reviews
Press 3: Old documents
Press 4: Exit
>>""")

    if menuOption == "1":
        createGarden()
    elif menuOption == "2":
        reviews()
    elif menuOption == "3":
        oldDocumnents()
    elif menuOption == "4":
        exit()

def createGarden():
    wantLawn = input("Do you want a lawn: y/n\n>>").lower()
    if wantLawn == "y":
        lengthOfLawn = float(input("Enter length of lawn:\n>> "))
        widthOfLawn = float(input("Enter width of lawn:\n>> "))
        totalSizeOfLawn = lengthOfLawn*widthOfLawn
        totalPriceOfLawn = totalSizeOfLawn * 15.50
        totalTimeOfLawn = totalSizeOfLawn * 20
        print("Price: £",totalPriceOfLawn,"m^2, Time to Take:",totalTimeOfLawn,"minutes")
    elif wantLawn == "n":
        print("No lawn for you")
    wantConcretePatio = input("Do you want a Concrete Patio: y/n\n>>").lower()
    if wantConcretePatio == "y":
        lengthOfConcretePatio = float(input("Enter length of Concrete Patio:\n>> "))
        widthOfConcretePatio = float(input("Enter width of Concrete Patio:\n>> "))
        totalSizeOfConcretePatio = lengthOfConcretePatio * widthOfConcretePatio
        totalPriceOfConcretePatio = totalSizeOfConcretePatio * 20.99
        totalTimeOfConcretePatio = totalSizeOfConcretePatio * 20
        print("Price: £", totalPriceOfConcretePatio, "m^2, Time to Take:", totalTimeOfConcretePatio, "minutes")
    elif wantConcretePatio == "n":
        print("No Concrete Patio for you")
    wantWoodenDeck = input("Do you want a lawn: y/n\n>>").lower()
    if wantWoodenDeck == "y":
        lengthOfWoodenDeck = float(input("Enter length of WoodenDeck:\\n>> "))
        widthOfWoodenDeck = float(input("Enter width of Wooden Deck:\n>> "))
        totalSizeOfWoodenDeck = lengthOfWoodenDeck * widthOfWoodenDeck
        totalPriceOfWoodenDeck = totalSizeOfWoodenDeck * 15.75
        totalTimeOfWoodenDeck = totalSizeOfWoodenDeck * 30
        print("Price: £", totalPriceOfWoodenDeck, "m^2, Time to Take:", totalTimeOfWoodenDeck, "minutes")
    elif wantWoodenDeck== "n":
        print("No WoodenDeck for you")
    if wantPond == "y":
        lengthOfPond = float(input("Enter length of WoodenDeck:\\n>> "))
        widthOfPond = float(input("Enter width of Wooden Deck:\n>> "))
        totalSizeOfPond = lengthOfPond * widthOfPond
        totalPriceOfPond = totalSizeOfPond * 15.75
        totalTimeOfPond = totalSizeOfPond * 30
        print("Price: £", totalPriceOfPond, "m^2, Time to Take:", totalTimeOfPond, "minutes")
    elif wantPond== "n":
        print("No Pond for you")
def reviews():
    pass

def oldDocumnents():
    pass

startMenu()

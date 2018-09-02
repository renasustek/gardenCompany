def startMenu():
    menuOption = input("""Press 1: Create Garden"
Press 2: Reviews
Press 3: Old documents
Press 4: Exit""")

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
        print("Price:",totalPriceOfLawn+"m^2, Time Taken:",totalTimeOfLawn)
    elif wantLawn == "n":
        pass
def reviews():
    pass

def oldDocumnents():
    pass

startMenu()

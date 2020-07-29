import pickle 
import os 
masterList = []

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def menuPrint():
    print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print("#               ~ T H E   M E N U ~                       #")
    print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print(" \n MENU: select a choice below \n A) Create New List \n B) My Lists \n C) Menu \n Q) Quit")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Going to be export. Dont mess with me. 
def saveToFile(choice, aList):
    validFlag = 0 
    while(validFlag == 0):
        print("Enter a valid directory to save your file...")
        savePath = input()
        if (os.path.isdir(savePath)):
            fileName = aList[0] + ".txt"
            savePath = savePath + '/' + fileName 
            validFlag = 1

    myFile = open(savePath,'w')
    myFile.write("********************************************** \n")
    myFile.write("             ~ " + choice + " ~                \n")
    myFile.write("********************************************** \n")

    for i in aList:
        listElement = str(i)
        elementNoBrackets = ""
        for x in listElement:
            if (x!='[' and x != ']' and x != "'" and x!= ','):
                elementNoBrackets = elementNoBrackets + x 
        if(elementNoBrackets != choice):
            myFile.write("* ")
            myFile.write(elementNoBrackets + "\n ")
        myFile.write("\n")
    myFile.close()
    print("l i s t   s a v e d !")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def printList(choice, aList):
    choice = str(choice)
    if(len(aList)!=0):

        print("**********************************************")
        print("          ~ " + choice + " ~                  ")
        print("**********************************************")

        for i in aList:
            listElement = str(i)
            temp = ""
            for x in listElement:
                if (x!='[' and x != ']' and x != "'" and x!= ','):
                    temp = temp + x

            if(temp != choice):
                print("*", end='')
                print(temp)
        print("**********************************************")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#  mod for choice A in the main menu "Generate List"    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def createList():
    global masterList
    print("Enter a list name:")
    duplicate = False
    newList = []
    addMe = input()
    addMe = addMe.strip()
    for i in masterList:
        if (addMe == i[0]):
            duplicate = True
    
    if(duplicate == False):
        newList.append(addMe)
        masterList.append(newList)
        print("Your new list "  + addMe + " was Created ")
    elif(duplicate == True):
        print(str(addMe) + " already exists as a list")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def showMyLists():
    global masterList 

    if not masterList:
        print("You don't have any lists. Return to the main menu and create a list to get started!")

    print("**********************************************")
    print("           ~ Y O U R   L I S T S ~            ")
    print("**********************************************")

    for i in masterList:
        print("*" + i[0])
    
    print("**********************************************")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def sortList(choice, aList):

    #Not a caseless matching 
    #aList.sort()
    #printList(choice, aList)
    aList.remove(choice)
    aList = sorted(aList, key=str.casefold)
    aList.insert(0,choice)
    printList(choice, aList)
    return aList
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def clearList(choice, aList):
    aList.remove(choice)
    aList.clear()
    aList.append(choice)
    return aList
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def myLists():

    global masterList

    userInput = " "
    showMyLists()
    found = 0 
    isEmpty = False

    if(not masterList):
        isEmpty = True

    while(found == 0 and isEmpty == False):
        print("")
        print("Pick a list to get started. Enter M to go back to menu: \n")
        listChoice = input()
        listChoice = listChoice.strip()
        if(listChoice.upper() == "M"):
            mainProg()
            break

    # Just use the index module. What I did was the loooong way :(
        for i in masterList:
            if(listChoice in i):
                index = masterList.index(i)
                found = 1 
                break
        if(found == 0):
            print("Uh oh, couldn't find " + listChoice + " enter an existing list name")

    # Now we know we are working on masterList[index]. Broke from enter valid list menu. 
    while(userInput != "9" and isEmpty == False):
        print("What do you want to do with '" + listChoice + "' ? Select a choice: \n 1) Add item to list \n 2) Remove item from list \n 3) Search for an item in the list \n 4) Display the list \n 5) Sort the list alphabetically \n 6) Save the list to a file \n 7) Clear the list \n 8) Delete the list \n 9) Go back to My Lists")
        userInput = input()
        userInput = userInput.strip()
        if(userInput == "1"):
            print("Enter an item:")
            addMe = input()
            addMe = addMe.strip()
            if (addMe not in masterList[index]):
                masterList[index].append(addMe)
                if (addMe != masterList[index][0]):
                    print(addMe + " was added to the list :D ")
                else:
                    print("Try something that's not the same title of the list....")
            else:
                print(str(addMe) + " is already in the list. Try something new.")
        elif(userInput == "2"):
            print("Enter an item to remove:")
            removeMe = input()
            removeMe = removeMe.strip()
            if(removeMe == listChoice):
                print("you can't remove the title of the list")
            if(removeMe in masterList[index]):
                masterList[index].remove(removeMe)
                print(removeMe + " was removed from the list :D ")
            else:
                print("We couldn't find " + removeMe + " in the " + listChoice + " list")
        elif(userInput== "3"):
            print("watcha lookin for?")
            findMe = input()
            findMe = addMe.strip()
            if(findMe in masterList[index]):
                print(findMe + " was found!")
            else:
                print("We couldn't find " + findMe + " in the " + listChoice + " list")
        elif(userInput == "4"):
            printList(listChoice, masterList[index])
        elif(userInput == "5"):
            masterList[index] = sortList(listChoice, masterList[index])
        elif(userInput == "6"):
            saveToFile(listChoice, masterList[index])
        elif(userInput == "7"):
            print("Are you sure you want to clear '" + listChoice + "' ? Y/N")
            userChoice = input()
            flag = 0
            while(flag == 0):
                if(userChoice.upper().strip() == "Y"):
                    #masterList[index].clear()
                    clearList(listChoice, masterList[index])
                    print(listChoice + " has been cleared")
                    flag = 1
                elif(userChoice.upper().strip()== "N"):
                    print("Clear list aborted")
                    flag = 1 
            continue
        elif(userInput == "8"):
            
            flag = 0
            while(flag == 0):
                print("Are you sure you want to delete '" + listChoice + "' ? Y/N")
                userChoice = input()
                if(userChoice.upper().strip() == "Y"):
                    masterList.remove(masterList[index])
                    print(listChoice + " has been delete")
                    flag = 1
                    userInput = "9"
                    myLists()
                elif(userChoice.upper().strip()== "N"):
                    print("delete aborted")
                    flag = 1 
            continue
        elif(userInput == "9"):
            myLists()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def startUp():
    global masterList
    if(os.path.isfile("C:/Users/austb/OneDrive/Documents/JUSTCODE/myCodeProjects/Python/pythonDays/outfile")):
        with open('outfile', 'rb') as fp:
            masterList = pickle.load(fp)
    else:
        print("Didn't find ya a file to load")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def shutDown():
    global masterList
    print()
    print("Would you like to save changes. Y/N")
    decide = input()
    decide = decide.upper()
    if(decide == "Y"):
        with open('outfile', 'wb') as fp:
            pickle.dump(masterList, fp) 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def mainProg():
    userChoice = ""
    while(userChoice != "Q"):
        menuPrint()
        userChoice = input()
        userChoice = userChoice.strip().upper()
        if(userChoice == "A"):
            createList()
        elif(userChoice == "B"):
            myLists()
        elif(userChoice=="C"):
            menuPrint()
        elif(userChoice=="Q"):
            print("Goodbye, random user")
            shutDown()
            exit()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#            ~ T H E   P R O G    E N T R Y ~             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# call start up to get data. 
startUp()

#initiate 
mainProg()



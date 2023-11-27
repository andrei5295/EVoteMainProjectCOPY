from Admin import Admin
from Candidate import Candidate
captainList = []
councilorList = []
candidateList = []
userSet = set()

# Call this function to login as admin
def loginAsAdmin(adminList):
    print("\nEnter Your Credentials")
    name = input("Username: ")
    password = input("Password: ")
    isLoggedIn = False

    for admin in adminList:
        if name == admin.user and password == admin.pw:
            isLoggedIn = True

    return isLoggedIn

# Register new administrator
def registerAdmin(adminList):
    print("Administrator Registration")
    print("--------------------------")
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        newAdmin = Admin(username,password)
        adminList.append(newAdmin)
        print("Registration Successful!")
        yesNo = input("Register? [Y/N]")
        if yesNo != "Y":
            break

# Register new candidate
def registerCandidate(candidateList):
    while True:
        print("Candidate Registration")
        print("----------------------")
        name = input("Name: ")
        position = input("Position: ").lower()

        newCandidate = Candidate(name , position)
        candidateList.append(newCandidate)

        if position == "captain":
            captainList.append(newCandidate)
        elif position == "councilor":
            councilorList.append(newCandidate)
        print("Registration Successful!")
        yesNo = input("Register? [Y/N]")
        if yesNo != "Y" or "y":
            break

def loginVoter():
    print("")
    ageInput = int(input("Age: "))
    idInput = input("Voter's ID [Y/N]: ").lower()
    isLoggedIn = False
    if ageInput >= 18 and idInput == "y":
        print("You Are Qualified To Vote!")
        print("")
        isLoggedIn = True
    else:
        print("Sorry You Are Not Qualified To Vote.")
        print("")
    return isLoggedIn

def voteForCaptains():
    count = 0
    print("Captains:")
    for captains in captainList:
        count += 1
        print(f"\t{count}.",captains.name)
    userInput = int(input("Select Captain Number: "))
    print("")
    captainList[userInput-1].addVoteCount()

    count = 0
    print("Councilor:")
    for councilor in councilorList:
        count += 1
        print(f"\t{count}.",councilor.name)

    for x in range(7):
        userInput = int(input("Select Councilor Number: "))
        if userInput not in userSet:
            userSet.add(userInput)
            councilorList[userInput - 1].addVoteCount()
        else:
            continue
    userSet.clear()
    
def viewResult():
    sortedCaptain = sorted(captainList, key=lambda x: x.name)
    sortedCouncilor = sorted(councilorList, key=lambda x: x.name)

    print("")
    print("Here are the electoral results!")
    print("-------------------------------")
    print("Captains: ")
    for obj in sorted(sortedCaptain, key=lambda x: x.voteCount, reverse=True):
        print(f"{obj.name} = {obj.voteCount}")
    print("")
    print("Councilors: ")
    for obj in sorted(sortedCouncilor, key=lambda x: x.voteCount, reverse=True):
        print(f"{obj.name} = {obj.voteCount}")
        

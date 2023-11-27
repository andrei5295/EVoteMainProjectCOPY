import ConstantStrings
import CommonFunctions
from Admin import Admin
from CommonFunctions import candidateList

adminList = []

baseAdmin = Admin("Admin","Admin")
adminList.append(baseAdmin)

while True:
    print(ConstantStrings.mainMenuString)
    choice = input("Select Number: ")

    if choice == "1":
        isLoggedIn = CommonFunctions.loginVoter()
        if isLoggedIn:
            CommonFunctions.voteForCaptains()

    elif choice == "2":
        loginSuccess = CommonFunctions.loginAsAdmin(adminList)
        if loginSuccess:
            print("Login Successful")
            while True:
                print(ConstantStrings.adminMenuString)
                choice = input("Select Number: ")
                print("")
                if choice == "1":
                    CommonFunctions.registerAdmin(adminList)
                elif choice == "2":
                    CommonFunctions.registerCandidate(candidateList)
                elif choice == "3":
                    break
        else:
            print("Invalid user")

    elif choice == "3":
        CommonFunctions.viewResult()
        print("")

    elif choice == "4":
        sureInput = input("Are you sure you want to exit? [Y/N]: ").lower()
        if sureInput == "y":
            print("Exiting Program")
            break


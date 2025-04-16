import welcome # Welcome_Screen()
import login # Valid_User()
import menu # Gen_Menu(User)
import log_workout # Log_Workout(User)

def Usyd_Fitness_Tracker():
    lstat = False
    authUser = ["Coach", "Sammy", "Scott"]
    User = ""
    print()
    welcome.Welcome_Screen()
    print()
    User = login.Valid_User()
    if User in authUser:
        lstat = True # Set login state
        while lstat == True:
            menu.Gen_Menu(User)
            print("[4] Logout")
            sel = int(input("Enter selection: "))
            if sel == 1:
                log_workout.Log_Workout(User)
            if sel == 4:
                lstat == False
                break





Usyd_Fitness_Tracker()
import welcome # Welcome_Screen()
import login # Valid_User()
import menu # Gen_Menu(User)

def Usyd_Fitness_Tracker():
    print()
    welcome.Welcome_Screen()
    print()
    menu.Gen_Menu(login.Valid_User())

Usyd_Fitness_Tracker()
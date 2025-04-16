import login # For testing only
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~
| Hi Username             |
~~~~~~~~~~~~~~~~~~~~~~~~~~~
| [1] Log an activity     |
| [2] Track your fitness  |
| [3] Plan your health    |
~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# username = login.Valid_User() # Access module as variable

def Gen_Menu(User): # Define function with username argument
    sep = "~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    greet = f"| Hi {User}{" " * (21 - len(User))}|" # Personalise greeter
    menu = [ # Same list method as "welcome.py"
        sep,
        greet,
        sep,
        "| [1] Log an activity     |",
        "| [2] Track your fitness  |",
        "| [3] Plan your health    |",
        sep
    ]
    for line in menu:
        print(line)

# Gen_Menu(login.Valid_User())
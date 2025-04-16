"""
Login with your username: SammySammySammySammy
Your username is too long.

Login with your username: Sammy
~~~~~~~~~~~~~~~~~~~~~~~~~~~
| Hi Sammy                |
~~~~~~~~~~~~~~~~~~~~~~~~~~~
| [1] Log an activity     |
| [2] Track your fitness  |
| [3] Plan your health    |
~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

def Valid_User(): # Function to validate username
    while True:
        User = input(str("Login with your username: ")) # Get username
        if (len(User)) > 20: # Catch invalid input
            print("Your username is too long.") # Inform user, ask again
        if (len(User)) <= 20: # Valid input
            return User # Return username variable
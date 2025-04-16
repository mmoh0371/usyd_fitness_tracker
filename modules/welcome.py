"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*
| WELCOME TO USYD FITNESS |
*-*-*-*-*-*-*-*-*-*-*-*-*-*
*    LOGS YOUR WORKOUT    *
*   TRACKS YOUR FITNESS   *
*    GET FIT & HEALTHY    *
*-*-*-*-*-*-*-*-*-*-*-*-*-*
"""

def Welcome_Screen(): # Self contained function to print welcome screen
    sep = "*-*-*-*-*-*-*-*-*-*-*-*-*-*" # Define separator
    output = [ # List containing each welcome message line
        sep,
        "| WELCOME TO USYD FITNESS |",
        sep,
        "*    LOGS YOUR WORKOUT    *",
        "*   TRACKS YOUR FITNESS   *",
        "*    GET FIT & HEALTHY    *",
        sep
    ]
    for line in output: # For loop to print welcome message
        print(line)

# Welcome_Screen()
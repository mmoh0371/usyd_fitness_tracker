import date # Date validation function

username = "Coach" # Test case user # One-man cheeseburger apocalypse

def Log_Workout(username: str): # Workout logging module
    exercise = "" # str
    date = "" # str
    distance = "" # str >> float, str
    duration = 0 # int
    valid_exercise = ["swim", "run", "cycle"] # List of valid exercises 
    user_prompts = ["What exercise would you like to log?"] # Initial user prompt

    while True:
        exercise = str(input(user_prompts[0]))
        user_prompts.append(f"Sorry, {exercise} is not supported.") # Include exception message after user input
        try: # Excpetion handling
            assert exercise.lower() in valid_exercise # Assert user input against valid inputs
        except AssertionError: # Exeption if assert returns false
            print(user_prompts[1]) # Tell user they are wrong and should not be allowed near a computer
            break # Kill program for whatever reason (why? what is the point of exception handling if you want to kill it anyway)
        else:
            prompts = [ # New lists to contain variable defined f-strings due to workaround
                 f"What month did you {exercise} (mm/yyyy)?",
                 f"What distance did you {exercise} (km or miles)?", # This is horrible way of asking this
                 f"How long did you {exercise} (minutes)?"
            ]
            user_prompts.extend(prompts) # Update original list for simplicity
            
           
Log_Workout(username)

# Issue: f-string exercise variables don't update in list after user input. An oversight
# Solution: Append f-strings containing variables after user input
# There are more interesting ways to solve this, but I don't have time
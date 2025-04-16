import date # Date validation function

username = "Coach" # Test case user # One-man cheeseburger apocalypse

def Log_Workout(username: str): # Workout logging module
    User = username
    exercise = "" # str
    month = "" # str
    distance = "" # str >> float, str
    duration = 0 # int
    valid_exercise = ["swim", "run", "cycle"] # List of valid exercises 
    user_prompts = ["What exercise would you like to log? "] # [0] # Initial user prompt

    while True:
        # EXERCISE
        exercise = str(input(user_prompts[0]))
        exercise = exercise.lower()
        user_prompts.append(f"Sorry, {exercise} is not supported.") # [1] # Include exception message after user input
        try: # Excpetion handling
            assert exercise in valid_exercise # Assert user input against valid inputs
        except AssertionError: # Exeption if assert returns false
            print(user_prompts[1]) # Tell user they are wrong and should not be allowed near a computer
            break # Kill program for whatever reason (why? what is the point of exception handling if you want to kill it anyway)
        else:
            prompts = [ # New lists to contain variable defined f-strings due to workaround
                 f"What month did you {exercise} (mm/yyyy)? ", # [2]
                 f"What distance did you {exercise} (km or miles)? ", # [3] # This is horrible way of asking this
                 f"How long did you {exercise} (minutes)? " # [4]
            ]
            user_prompts.extend(prompts) # Update original list for simplicity
        # MONTH
        month = str(input(user_prompts[2])) # User inputs a fairly useless date (no day?)
        try:
            assert date.Is_Valid_Date(month) == True # Should print error message
        except AssertionError:
            break # If Is_Valid_Date returns false will kill process
        # DISTANCE
        def Metric_Conversion(val, unit): # Do exactly before saving data
            udef = ["km", "miles"] # Defined units of measurement
            if unit == udef[0]:
                km = val
            if unit == udef[1]:
                km = f"{val * 1.6:.1f}"
            return km
        distance = str(input(user_prompts[3])) # Assume valid input "x km" OR "x.x miles"
        dvars = distance.split(" ") # Split input
        dval = float(dvars[0]) # Distance value # val
        dunit = str(dvars[1]) # Distance measurement # unit
        if dval < 0: # Avoid erronious entries
            print("Error: Distance must be greater than zero.")
            break
        # DURATION
        duration = int(input(user_prompts[4])) # Must be positive integer
        if duration < 1: # Avoid erronious entries
            print("Error: Duration must be a positive whole integer.")
            break
        # EXPORT
        with open(f"{User}.txt", "a") as wlog: # Open or create $User.txt
            wlog.write(f"{exercise},{Metric_Conversion(dval, dunit)},{duration},{month}\n") # Print fist line # Lazy new line method
            wlog.close()
        break

Log_Workout(username)

# Issue: f-string exercise variables don't update in list after user input. An oversight
# Solution: Append f-strings containing variables after user input
# There are more interesting ways to solve this, but I don't have time
# mm/yyyy format
# mm = 01 - 12
# yyyy = 2000 - 2025
# sep = "/"

# Zero thought approach to this # This came back to haunt me
def Is_Valid_Date(date: str): # Use snake_case with Capital_Letters because I prefer it.
    mm = "" # Empty variables to contain separated values
    yyyy = ""
    sep = ""
    valid = True # Boolean variable # Innocent until proven guilty
    err_values = [] # Part of error message hotfix
    dchar = [] # List to contain each value of date string (hotfix)
    valid_ints = [] # Will be populated to all valid integers as strings
    irr_val = 0 # Variable to contain position or irregular value

    # Comparing lists to find location of irregular separator
    if (len(date) < 7 or len(date) > 7): # Hotfix 2, oversight due to irregular date input debugging
        for i in range(10):
            valid_ints.append(str(i)) # Valid values
        for i in date:
            dchar.append(i) # Date values
        for i in range(len(dchar)):
            if (dchar[i] not in valid_ints): # Identify position of separator
                irr_val = i
        sep = dchar[irr_val] # Separator variable
        mmyyyy = date.split(dchar[irr_val]) # List containing individual mm / yyyy
        mm = mmyyyy[0] # Assign mm / yyyy to variable
        yyyy = mmyyyy[1]

    for i in range(len(date)): # Arbitrary method to separate values # Remembered about split() after I wrote this
        if (len(date) < 7 or len(date) > 7): # Should have used split for all of it, but it works
            break
        if (i <= 1):
            mm += date[i]
        if (i == 2):
            sep += date[i]
        if (i >= 3):
            yyyy += date[i]

    mmL = [] # Create empty list for all possible values
    yyyyL = [] # Something very uninspired is brewing

    for i in range(12): # Append empty lists to contain all valid values for "mm" & "yyyy"
        if (i <= 8):
            mx = f"0{str(i + 1)}"
            mmL.append(mx)
        if (i >= 9):
            mx = str(i + 1)
            mmL.append(mx)
    for i in range(26): # This is a horrible way of doing this.
        if (i < 9):
            yyxx = f"200{str(i)}"
            yyyyL.append(yyxx)
        if (i == 9):
            yyxx = f"200{str(i)}"
            yyyyL.append(yyxx)
        if (i > 9):
            yyxx = f"20{str(i)}"
            yyyyL.append(yyxx)

    if sep != "/": # Quick and dirty way to determine validity using innocent until proven guilty methodology
        valid = False
        err_values.append(0) # Append zero or one to err_values list, where 0 = valid value not present and 1 = valid value is present
    else:
        err_values.append(1)
    if mm not in mmL:
        valid = False
        err_values.append(0)
    else:
        err_values.append(1)
    if yyyy not in yyyyL:
        valid = False
        err_values.append(0)
    else:
        err_values.append(1)

    # Forgot to write error messages
    # Hotfix
    # Even quicker and dirtier way to spit error messages
    # Note: Was not quicker
    # Print only one error message
    # Prority 1 - 3

    err_message = [
        "Please use '/' as a separator.", # Priority 1
        "Please enter a valid month.", # Priority 2
        "Please enter a valid year." # Priority 3
    ]

    for i in range(len(err_values)): # Simple hotfix to print error messages based on binary value (valid / not valid) with respect to priority
        if (err_values[i] == 0):
            print(err_message[i])
            break

    return valid # Return boolean value............................

# This could have been a lot simpler...

"""
# Test case
# Prints True / False
print(Is_Valid_Date("07/2012")) # Random date # Valid
print(Is_Valid_Date("11/2009")) # Left 4 Dead 2 release month / year # Valid
print(Is_Valid_Date("12/1999")) # Quake 3 Arena release # Invalid
print(Is_Valid_Date("10-2010")) # Fallout: New Vegas release # Invalid
print(Is_Valid_Date("4/2003")) # POSTAL 2 release # Invalid
print(Is_Valid_Date("11/1998")) # Half-Life release # Invalid
print(Is_Valid_Date("11/04")) # Half-Life 2 release # Invalid
print(Is_Valid_Date("03/2007")) # S.T.A.L.K.E.R.: Shadow of Chernobyl # Valid
# Prints Error Message
Is_Valid_Date("07/2012") # Random date # Valid
Is_Valid_Date("11/2009") # Left 4 Dead 2 release month / year # Valid
Is_Valid_Date("12/1999") # Quake 3 Arena release # Invalid
Is_Valid_Date("10-2010") # Fallout: New Vegas release # Invalid
Is_Valid_Date("4/2003") # POSTAL 2 release # Invalid
Is_Valid_Date("11/1998") # Half-Life release # Invalid
Is_Valid_Date("11/04") # Half-Life 2 release # Invalid
Is_Valid_Date("03/2007") # S.T.A.L.K.E.R.: Shadow of Chernobyl # Valid
# Debug
print(mm, sep, yyyy)
print(valid)
print(mmL)
print(yyyyL)
print(err_values, valid)
print(valid)
print(err_values) # Useful values for visualisation
print("[s, m, y]")
print()
print(err_values)
"""

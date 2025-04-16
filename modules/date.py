# mm/yyyy format
# mm = 01 - 12
# yyyy = 2000 - 2025
# sep = "/"

# Zero thought approach to this
def Is_Valid_Date(date: str): # Use snake_case with Capital_Letters because I prefer it.
    mm = "" # Empty variables to contain separated values
    yyyy = ""
    sep = ""
    valid = True # Boolean variable # Innocent until proven guilty
    for i in range(len(date)): # Arbitrary method to separate values # Remembered about split() after I wrote this
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
        if (i <= 8):
            yyxx = f"200{str(i)}"
            yyyyL.append(yyxx)
        if (i >= 9):
            yyxx = f"20{str(i)}"
            yyyyL.append(yyxx)
    if mm not in mmL: # Quick and dirty way to determine validity using innocent until proven guilty methodology
        valid = False
    if sep != "/":
        valid = False
    if yyyy not in yyyyL:
        valid = False
    
    return valid # Return boolean value............................

# I'm dissapointed in even myself for writing this to be completely honest

# Test case
"""
print(Is_Valid_Date("07/2012")) # Random date # Valid
print(Is_Valid_Date("11/2009")) # Left 4 Dead 2 release month / year # Valid
print(Is_Valid_Date("12/1999")) # Quake 3 Arena release # Invalid
print(Is_Valid_Date("10-2010")) # Fallout: New Vegas release # Invalid
print(Is_Valid_Date("4/2003")) # POSTAL 2 release # Invalid
print(Is_Valid_Date("11/1998")) # Half-Life release # Invalid
print(Is_Valid_Date("11/04")) # Half-Life 2 release # Invalid
print(Is_Valid_Date("03/2007")) # S.T.A.L.K.E.R.: Shadow of Chernobyl # Valid
"""

# Debug
"""
print(mm, sep, yyyy)
print(valid)
print(mmL)
print(yyyyL)
"""
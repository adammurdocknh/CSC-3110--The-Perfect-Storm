"""
Adam Murdock
November 5, 2020
cyclone_murdock_adam.py
Version 1

"""


"""
Simple greeting message.
"""
def printGreeing():
    print("Welcome to our tropical cyclone resource.")
    print("*****************************************")

"""
Prints instructions for the user.
"""
def printInstructions():
    print('Would you like to use kilometers per hour or miles per hour?')
    print('Enter k for km/hr, m for mph or q to quit.')

"""                
Checks if the variable input is a positive number.
Returns true if @input is a positive number,
Return false if @input is not a positive number and prints an error message.
"""
def checkValidInput(input):
    if(input > 0):
        return True
    else:
        print("You didn't enter a valid number. Please enter non-negative numbers.")
        return False

"""
Converts the variable @kmh into mph.
"""
def kilometerToMiles(kmh):
    return kmh * 0.621371

"""
Converts the variable @mph into km/hr.
"""
def milesToKilometers(mph):
    return mph * 1.61

"""             
Converts the variable @mph into knots
"""
def milesToKnots(mph):
    return mph * 0.868976

"""
This function prints the hurricane's strength based on the @mph input.
Uses an if/elif tree to decide.
"""
def hurricaneStrength(mph):
    print("On the hurricane scale this is a:")
    if(mph < 39):
        print("Tropical depression")
    elif(mph >= 39 and mph < 74 ):
        print("Tropical storm")
    elif(mph >= 74 and mph < 96):
        print("Category 1 Hurricane")
    elif(mph >= 96 and mph < 111):
        print("Category 2 Hurricane")
    elif(mph >= 111 and mph < 130):
        print("Category 3 Hurricane")
    elif(mph >= 130 and mph < 157):
        print("Category 4 Hurricane")
    elif(mph >= 157):
        print("Category 5 Hurricane")
    print("***")

"""
This function prints the typhoon's strength based on the @kmh input.
Uses an if/elif tree to decide.
"""
def typhoonStrength(kmh):
    print("On the typhoon scale this is a:")
    if(kmh < 63):
        print("Tropical depression")
    elif(kmh >= 63 and kmh < 88):
        print("Tropical storm")
    elif(kmh >= 88 and kmh < 118):
        print("Severe tropical storm")
    elif(kmh >= 118 and kmh < 150):
        print("Typhoon")
    elif(kmh >= 150 and kmh < 185):
        print("Severe Typhoon")
    elif(kmh >= 185):
        print("Super Typhoon")
    print("***")


"""
This function prints the storm's strength using the beaufort wind scale
based on the @knots input. Uses an if/elif tree to decide.
"""
def beaufortStrength(knots):
    print("On the beaufort wind scale this is:")
    if(knots < 1):
        print("Calm")
    elif(knots >= 1 and knots < 4):
        print("Light air")
    elif(knots >= 4 and knots < 7):
        print("A Light Breeze")
    elif(knots >= 7 and knots < 11):
        print("A 'Gentle Breeze' registered trademark of Proctor and Gamble ")
    elif(knots >= 11 and knots < 17):
        print("A Moderate Breeze")
    elif(knots >= 17 and knots < 22):
        print("A Fresh Breeze")
    elif(knots >= 22 and knots < 28):
        print("A Strong Breeze")
    elif(knots >= 28 and knots < 34):
        print("A Near Gale")
    elif(knots >= 34 and knots < 41):
        print("A Gale")
    elif(knots >= 41 and knots < 48):
        print("A Strong Gale")
    elif(knots >= 48 and knots < 56):
        print("A Storm")
    elif(knots >= 56 and knots < 64):
        print("A Violent Storm")
    elif(knots >= 64):
        print("A Hurricane")
    print("***")
    
"""
Function takes no inputs and returns void. 
This function pulls all the other functions together, 
and calls on them.
"""
def main():
    printGreeing()
    finished = False
    while(not finished):
        printInstructions()
        inputVal = input()
        if (inputVal.upper() == "M"):
            print("What is the speed of the hurricane in mph?")
            # Getting user input and casting to float
            inputVal = float(input())
            # Verifying the float is an acceptable value ie the value
            # is positive and is not zero.
            if(checkValidInput(inputVal)):
                print("That is", milesToKilometers(inputVal), "km/hr")
                print("That is", milesToKnots(inputVal), "knots")
                hurricaneStrength(inputVal)
                typhoonStrength(milesToKilometers(inputVal))                    
                beaufortStrength(milesToKnots(inputVal))
    
        if (inputVal.upper() == "K"):
            print("What is the speed of the hurricane in km/hour?")
            # Getting user input and casting to float
            inputVal = float(input())
            # Verifying the float is an acceptable value ie the value
            # is positive and is not zero.
            if(checkValidInput(inputVal)):
                print("That is", kilometerToMiles(inputVal), "mph")
                print("That is", milesToKnots(kilometerToMiles(inputVal)), "knots")
                hurricaneStrength(inputVal)
                typhoonStrength(kilometerToMiles(inputVal))
                beaufortStrength(milesToKnots(kilometerToMiles(inputVal)))
    
        if (inputVal.upper() == "Q"):
            print("I hope this to was helpful. May munsell be with you.")
            finished = True
    
main()

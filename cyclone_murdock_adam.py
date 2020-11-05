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
Checks if @kmh is a valid input and then returns a float.
"""
def kilometerToMiles(kmh):
    return kmh * 0.621371

"""
Converts the variable @mph into km/hr.
Checks if @mph is a valid input and then returns a float.
"""
def milesToKilometers(mph):
    return mph * 1.61
                

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
# """
# def beaufortStrength(knots):
#     print("On the beaufort wind scale this is a:")
    
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
        if (inputVal == "m"):
            print("What is the speed of the hurricane in mph?")
            # Getting user input and casting to float
            inputVal = float(input())
            if(checkValidInput(inputVal)):
                print("That is", milesToKilometers(inputVal), "km/hr")
                hurricaneStrength(inputVal)
                typhoonStrength(milesToKilometers(inputVal))
        if (inputVal == "k"):
            print("What is the speed of the hurricane in km/hour?")
            # Getting user input and casting to float
            inputVal = float(input())
            # Verifying the float is an acceptable value ie the value
            # is positive and is not zero.
            if(checkValidInput(inputVal)):
                print("That is", kilometerToMiles(inputVal), "mph")
                hurricaneStrength(inputVal)
                typhoonStrength(kilometerToMiles(inputVal))
        if (inputVal == "q"):
            print("I hope this to was helpful. May munsell be with you.")
            finished = True
    
main()

import math


def main():
    """
    Main function to orchestrate the program flow and tell the story of the program.
    """
    #program description function
    displayProgramDescription()

    #input
    number = getPosFloat()
    
    #processing
    rounding_error = calculateRoundingError(number)

    #output
    displayResult(rounding_error)


def displayProgramDescription():
    """
    Displays a brief description of the program's purpose.
    """
    print("This program demonstrates rounding errors.\n"
          "It takes a number, calculates its square root, squares the result,\n"
          "and shows the difference from the original.\n")


def getPosFloat():
    """
    Prompts the user to enter a positive number and validates the input.

    Parameters: 
        none

    Returns: 
        float: a positive number the user has input.
    """
    while True:
        #get user input string
        number_input = input("Enter a number above 0: ")
        if isUserInputPosFloat(number_input):
            print("")  #insert spacing
            return float(number_input)  #cast input to float and return the resulting float


def isUserInputPosFloat(number_input):
    """
    Validates user's input based on criteria: must be a positive number greater than 0.

    Parameters: 
        number_input (str): User's input that needs to be validated.

    Returns: 
        bool: True if the input matches the criteria, False if it doesn't.
    """
    try:  #try the following...
        number_input = float(number_input)  #try to cast number_input to float
        if number_input > 0:
            return True  #a number is greater than 0
        else:
            print("Wrong Input. The input number should be greater than zero.")
            return False  #a number is not greater than 0
    except:  #if casting number_input to float fails display...
        print("Wrong Input. Input a number instead.")
        return False  #the input is not a number


def calculateRoundingError(number):
    """
    Calculates the rounding error by taking the square root of a number, squaring it, and finding the modulus with the original number.

    Parameters: 
        number (float): A positive number to demonstrate rounding error on.

    Returns: 
        float: The rounding error (difference) of squared sqrt with original number).
    """
    sqrt_result = math.sqrt(number)
    squared_result = sqrt_result ** 2
    rounding_error = abs(squared_result - number)
    return rounding_error


def displayResult(rounding_error):
    """
    Displays the rounding error result.
    
    Parameters:
        rounding_error (float): The calculated rounding error.
    """
    print(f"Rounding error: {rounding_error}.")


#call main function when script is executed
if __name__ == "__main__":
    main()

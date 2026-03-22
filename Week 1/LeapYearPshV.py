def main():
    """
    Main function to orchestrate the program flow and tell the story of the program.
    """
    #program description function
    displayProgramDescription()

    #input
    year = getPosInt()
    
    #processing
    is_leap_year = isLeapYear(year)

    #output
    displayResult(is_leap_year, year)


def displayProgramDescription ():
    """
    Displays a brief description of the program's purpose. 
    """
    print("This program will take a year and check if it fits the conditions\n"+
          "for it to be considered a leap year using modulus operator\n")


def getPosInt():
    """
    Prompts the user to enter a positive integer and validates the input.

    Parameters: 
        none

    Returns: 
        str: a year the users has input.
    """
    while True:
        #get user input string
        year_input = input("Enter a year from 1 to 9999: ")
        if isUserInputPosInt(year_input):
            print("") #insert spacing
            return int(year_input) #cast input to integer and return the resulting int


def isUserInputPosInt (year_input):
    """
    Validates users input based on criterias like if it is between 1 and 9999, and if it is a whole number/integer.

    Parameters: 
        year_input (str): Users input that needs to be validated.

    Returns: 
        bool: True if the input matches the criterias, False if doesn't.
    """
    try: #try the following...
        year_input = int(year_input) #try to cast year_input to int
        if 1 <= year_input < 9999:
           return True #a number is in the range between 1 and 9999
        else:
            print("Wrong input. Input a number in a range from 1 to 9999")
            return False #a number is not in the range between 1 and 9999
    except: #if casting year_input to int fails display...
        print("Wrong input. Input a number instead")
        return False # the input is not a number


def isLeapYear(year):
    """
    isLeapYear is a function that verifies if a year is a leap year using modulus operator.

    Parameters: integer

    Output: boolean 
    """

    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True #input is a leap year
            else:
                return False #input is not a leap year
        else:
            return True #input is a leap year
    else: 
        return False #input is not a leap year
    

def displayResult(is_leap_year, year):
    """
    Displays the output with the input variable based on the bool return of is_leap_year
    
    is_leap_year (bool): A bool, output is based on.
    year (int): A year to be displayed
    """
    if is_leap_year: #if is_leap_year return is True display the following...
        print(f"{year} is a leap year.")
    else: #if is_leap_year return is False display the following...
        print(f"{year} is not a leap year.")


#call main function when script is executed
if __name__ == "__main__": 
    main()

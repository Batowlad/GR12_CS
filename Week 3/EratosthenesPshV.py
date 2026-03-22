def main():
    """
    Main function to orchestrate the program flow and tell the story of the program.
    """
    #program description function
    displayProgramDescription()

    #input
    upper_limit = getUpperLimit()

    #processing
    #one list only: initialized with integers 2 to upper_limit (inclusive)
    prime_list = list(range(2, upper_limit + 1))
    sieveEliminateMultiples(prime_list)

    #output
    displayResult(prime_list, upper_limit)


def displayProgramDescription():
    """
    Displays a brief description of the program's purpose.
    """
    print("This program will find all prime numbers up to a number you specify\n"+
          "using the Sieve of Eratosthenes. A prime is a whole number greater than one\n"+
          "with no exact divisors except one and itself. Multiples of each prime are eliminated.\n")


def getUpperLimit():
    """
    Prompts the user to enter the upper limit (inclusive) and validates the input.

    Parameters:
        none

    Returns:
        int: The validated upper limit (>= 2). The list will contain integers from 2 to this value.
    """
    while True:
        #get user input
        user_input = input("Enter an integer as the upper limit (inclusive). The program will find all primes from 2 up to this number. Minimum value is 2: ")
        if not isUpperLimitValid(user_input):
            continue
        print("") #insert spacing
        return int(user_input) #cast input to integer and return the resulting int


def isUpperLimitValid(user_input):
    """
    Validates user's input for upper limit based on criteria: must be an integer >= 2.

    Parameters:
        user_input (str): User's input that needs to be validated.

    Returns:
        bool: True if the input matches the criteria, False if it doesn't.
    """
    try: #try the following...
        value = int(user_input) #try to cast user_input to int
        if value >= 2:
            return True #a number is in the valid range
        else:
            print("The lowest number in the list is 2. Please enter an integer greater than or equal to 2.")
            return False #a number is not in the valid range
    except: #if casting user_input to int fails display...
        print("Please enter a valid integer.")
        return False #the input is not a number


def sieveEliminateMultiples(prime_list):
    """
    Implements the Sieve of Eratosthenes in place: for each number still in the list,
    remove all its multiples (except itself). Uses only this one list; no other data structures.

    Parameters:
        prime_list (list): List of integers from 2 to some upper limit (modified in place).

    Returns:
        none
    """
    index = 0
    while index < len(prime_list):
        prime = prime_list[index]
        remove_index = index + 1
        while remove_index < len(prime_list):
            if prime_list[remove_index] % prime == 0:
                prime_list.pop(remove_index)
            else:
                remove_index += 1
        index += 1


def displayResult(prime_list, upper_limit):
    """
    Displays the list of primes found up to the given limit.

    Parameters:
        prime_list (list): The list of prime numbers after the sieve.
        upper_limit (int): The upper limit that was used.
    """
    print(f"Primes from 2 to {upper_limit}: {prime_list}")


#call main function when script is executed
if __name__ == "__main__":
    main()

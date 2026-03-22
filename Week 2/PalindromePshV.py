def main():
    """
    Main function to orchestrate the program flow and tell the story of the program.
    """
    #program description function
    displayProgramDescription()

    #input
    word = getWord()
    
    #processing
    reverse_word = reverseWord(word)
    is_palindrome = isPalindrome(word, reverse_word)
    
    #output
    displayResult(is_palindrome, word, reverse_word)


def displayProgramDescription ():
    """
    Displays a brief description of the program's purpose. 
    """
    print("This program will take a word and check if it is a palindrome\n"+
          "by reversing the word and comparing it to the original.\n")


def getWord():
    """
    Prompts the user to enter a word and validates the input.

    Parameters: 
        none

    Returns: 
        str: a word the user has input.
    """
    while True:
        #get user input string
        word_input = input("Enter a word without spaces, numbers, or special characters: ")
        if isUserInputValid(word_input):
            print("") #insert spacing
            return word_input #return the validated word string


def isUserInputValid (word):
    """
    Validates user's input based on criteria: must not be empty, must not contain spaces, and must not contain numbers.

    Parameters: 
        word (str): User's input that needs to be validated.

    Returns: 
        bool: True if the input matches the criteria, False if it doesn't.
    """
    if word == "":
        exit() #exit program if input is empty
    else:
        if word.find(" ") != -1: #check if word contains a space
            print("No spaces allowed.")
            return False #word contains a space
        for char in word: #iterate through each character in the word
            for x in range(48, 58): #check unicode values for digits (0-9)
                if ord(char) == x: #if character is a digit
                    print("No numerals allowed.")
                    return False #word contains a number
    return True #word is valid (no spaces, no numbers)
        


def reverseWord(word):
    """
    Reverses a word using a for loop that adds the string backwards.

    Parameters: 
        word (str): The word to be reversed.

    Returns: 
        str: The reversed word.
    """
    reverse_word = ""
    for x in range(len(word)):
        reverse_word = word[x] + reverse_word

    return reverse_word
    
    
def isPalindrome(word, reverse_word):
    """
    Checks if a word is a palindrome by comparing the original word with its reverse (case-insensitive).

    Parameters: 
        word (str): The original word.
        reverse_word (str): The reversed version of the word.

    Returns: 
        bool: True if the word is a palindrome, False if it isn't.
    """
    if word.lower() == reverse_word.lower(): #compare lowercase versions of both words
        return True #word is a palindrome
    else:
        return False #word is not a palindrome

def displayResult(is_palindrome, word, reverse_word):
    """
    Displays the output with the input variables based on whether the word is a palindrome.
    
    Parameters:
        is_palindrome (bool): A bool indicating if the word is a palindrome.
        word (str): The original word to be displayed.
        reverse_word (str): The reversed word to be displayed.
    """
    print(f"Initial word: {word}")
    print(f"Reversed word: {reverse_word}")
    if is_palindrome == True: #if word is a palindrome display the following...
        print(f"Reversed word of Initial word is a palindrome.")
    else: #if word is not a palindrome display the following...
        print(f"Reversed word of Initial word is not a palindrome")


#call main function when script is executed
if __name__ == "__main__": 
    main()

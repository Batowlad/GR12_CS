#vowels (a, e, i, o, u, y) are kept as-is; consonants become consonant + "o" + consonant
vowels = "aeiouy"


def main():
    """
    Main function to orchestrate the program flow and tell the story of the program.
    """
    #program description function
    displayProgramDescription()

    #input
    word_to_translate = getWordToTranslate()
    #store each character as an element in a single list; alter list in place
    char_list = stringToList(word_to_translate)
    alterListToRovarsparket(char_list)
    result_message = "".join(char_list)

    #output
    displayResult(result_message)


def displayProgramDescription():
    """
    Displays a brief description of the program's purpose.
    """
    print("This program will translate any non-empty string you enter into Rövarspråket (Robber's Language).\n"+
          "Vowels (a, e, i, o, u, y) stay the same. Each consonant is replaced by that consonant,\n"+
          "then 'o', then the same consonant again (e.g. 'bubble' becomes 'bobubobboblole').\n")


def getWordToTranslate():
    """
    Prompts the user to enter a non-empty string to translate and validates the input.

    Parameters:
        none

    Returns:
        str: The string the user has input.
    """
    while True:
        #get user input string
        word_input = input("Enter a single string of any length (at least one character) to translate into Rövarspråket: ")
        if len(word_input) < 1:
            print("Input must not be empty. Please enter at least one character.")
            continue
        print("") #insert spacing
        return word_input #return the validated string


def stringToList(word):
    """
    Stores each character of the string as a single-character element in a list.

    Parameters:
        word (str): The input string.

    Returns:
        list: A list where each element is one character from the string.
    """
    return list(word) #return the list of single-character elements


def alterListToRovarsparket(char_list):
    """
    Alters the list in place so it represents Rövarspråket: after each consonant
    (non-vowel letter), inserts 'o' and the same consonant. Every element remains a single character.

    Parameters:
        char_list (list): List of single-character elements (modified in place).

    Returns:
        none
    """
    #iterate from the end so insertions do not shift indices we have not yet processed
    index = len(char_list) - 1
    while index >= 0:
        char = char_list[index]
        char_lower = char.lower()
        if char_lower in vowels or not char_lower.isalpha():
            index -= 1
            continue
        #consonant: insert 'o' and same character after this element
        char_list.insert(index + 1, "o")
        char_list.insert(index + 2, char)
        index -= 1


def displayResult(result_message):
    """
    Displays the translated text in Rövarspråket.

    Parameters:
        result_message (str): The text in Rövarspråket to be displayed.
    """
    print(f"Translation: {result_message}")


#call main function when script is executed
if __name__ == "__main__":
    main()

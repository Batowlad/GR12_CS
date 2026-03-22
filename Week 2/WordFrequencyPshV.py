def main():
    """
    Main function to orchestrate the program flow and tell the story of the program.
    """
    #program description function
    displayProgramDescription()

    #input
    word = getWord().lower()
    passage = getPassage().lower()
    
    #processing
    word_count = SearchForWord(word, passage)
    
    #output
    displayResult(word, word_count, passage)


def displayProgramDescription ():
    """
    Displays a brief description of the program's purpose. 
    """
    print("This program will search for a word in a passage\n"+
          "and count how many times it appears as a complete word.\n")


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
        word_input = input("Enter a word to be found (It should not be an empty string): ")
        if isWordInputValid(word_input):
            print("") #insert spacing
            return word_input #return the validated word string


def isWordInputValid (word):
    """
    Validates user's input based on criteria: must not be an empty string.

    Parameters: 
        word (str): User's input that needs to be validated.

    Returns: 
        bool: True if the input matches the criteria, False if it doesn't.
    """
    if word == "":
        print("Word must not be an empty string.")
        return False #word is empty
    return True #word is valid (not empty)
        
def getPassage():
    """
    Prompts the user to enter a passage where the word will be searched.

    Parameters: 
        none

    Returns: 
        str: The passage the user has input.
    """
    while True:
        #get user input string
        passage_input = input("Enter a passage for the word to be found in: ")
        return passage_input #return the passage string

        
def SearchForWord(word, passage):
    """
    Searches for a word in a passage and counts how many times it appears as a complete word (not as part of another word).

    Parameters: 
        word (str): The word to search for.
        passage (str): The passage to search in.

    Returns: 
        int: The count of how many times the word appears as a complete word.
    """
    count = 0 #initialize counter for word occurrences
    while True:
        try: 
            start_index = passage.index(word) #find the first occurrence of the word
        except:
            break #exit loop if word is not found

        word_len = len(word) - 1 #calculate length of word minus 1 for index calculation
        end_index = start_index + word_len #calculate the end index of the word

        if end_index == len(passage)-1: #if word is at the end of the passage
            if passage[start_index - 1].isalpha() and start_index != 0: #check if character before word is a letter
                passage = passage.replace(passage[start_index - 1]+word, "", 1) #remove word with preceding letter (not a complete word)

            else:
                count += 1 #increment count (word is complete)
                passage = passage.replace(word, "", 1) #remove the found word from passage

        else:
            if passage[start_index - 1].isalpha() and start_index != 0: #check if character before word is a letter
                passage = passage.replace(passage[start_index - 1]+word, "", 1) #remove word with preceding letter (not a complete word)

            elif passage[end_index + 1].isalpha() and end_index != 0: #check if character after word is a letter
                passage = passage.replace(word+passage[end_index + 1], "", 1) #remove word with following letter (not a complete word)

            else:
                count += 1 #increment count (word is complete)
                passage = passage.replace(word, "", 1) #remove the found word from passage

    return count #return the total count of word occurrences




def displayResult(word, word_count, passage):
    """
    Displays the word frequency count result.
    
    Parameters:
        word (str): The word that was searched for.
        word_count (int): The number of times the word was found.
        passage (str): The passage that was searched.
    """
    print(f"{word}, was found {word_count} times in the {passage}")


#call main function when script is executed
if __name__ == "__main__": 
    main()

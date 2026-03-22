def main():
    """
    Main function to orchestrate the program flow and tell the story of the program.
    """
    #program description function
    displayProgramDescription()

    #input
    choice = inputChoice()
    message = inputMessage()
    rotation_amount = inputRotationAmount()

    #processing
    if choice == "encrypt":
        result_message = encrypt(message, rotation_amount)
    elif choice == "decrypt":
        result_message = decrypt(message, rotation_amount)
    
    #output
    displayResult(choice, result_message)


def displayProgramDescription ():
    """
    Displays a brief description of the program's purpose. 
    """
    print("This program will encrypt or decrypt a message\n"+
          "using a Caesar cipher with a specified rotation amount.\n")


def inputChoice():
    """
    Prompts the user to choose between encrypting or decrypting a message and validates the input.

    Parameters: 
        none

    Returns: 
        str: The user's choice ("encrypt" or "decrypt").
    """
    while True:
        choice = input("Choose whether you want to encrypt or decrypt a message(Type: Encrypt/Decrypt): ").lower() #get user input and convert to lowercase
        if choice == "encrypt" or choice == "decrypt": #check if choice is valid
            return choice #return the validated choice
        else:
            print("Wrong input. Try again.") #display error message if input is invalid


def inputMessage():
    """
    Prompts the user to enter a message to be encrypted or decrypted.

    Parameters: 
        none

    Returns: 
        str: The message the user has input.
    """
    #get user input string
    message = input("Enter a message to be encrypted or decrypted based on your choice: ")
    return message #return the message string


def inputRotationAmount():
    """
    Prompts the user to enter a rotation amount and validates the input.

    Parameters: 
        none

    Returns: 
        int: The validated rotation amount (between 1 and 25).
    """
    while True:
        rotation_amount = input("Enter a number you want your message to be rotated by (from 1 to 25): ") #get user input
        if isRotationAmountValid(rotation_amount): #validate the input
            print("") #insert spacing
            return int(rotation_amount) #cast input to integer and return the resulting int



def isRotationAmountValid(rotation_amount):
    """
    Validates user's input for rotation amount based on criteria: must be an integer between 1 and 25.

    Parameters: 
        rotation_amount (str): User's input that needs to be validated.

    Returns: 
        bool: True if the input matches the criteria, False if it doesn't.
    """
    try: #try the following...
        int(rotation_amount) #try to cast rotation_amount to int
        if 0 < int(rotation_amount) < 26: #check if number is in the range between 1 and 25
            return True #a number is in the valid range
        else:
            print("Enter a number from 1 to 25.")
            return False #a number is not in the valid range
    except: #if casting rotation_amount to int fails display...
        print("Enter a number.")
        return False #the input is not a number


def encrypt(message, rotation_amount):
    """
    Encrypts a message using a Caesar cipher with the specified rotation amount.

    Parameters: 
        message (str): The message to be encrypted.
        rotation_amount (int): The number of positions to rotate each letter.

    Returns: 
        str: The encrypted message.
    """
    encrypted_message = "" #initialize empty string for encrypted message
    for char_index in range(len(message)): #iterate through each character in the message
        if message[char_index].isalpha(): #check if character is a letter

            char_uni = ord(message[char_index]) #get unicode value of the character

            if message[char_index].islower(): #if character is lowercase
                if char_uni+rotation_amount > 122: #if rotation exceeds 'z' (122), wrap around
                    encrypted_char = chr(char_uni + rotation_amount - 122 + 96) #wrap to beginning of alphabet
                else:
                    encrypted_char = chr(char_uni + rotation_amount) #rotate character normally
                
                encrypted_message += encrypted_char #add encrypted character to result

            elif message[char_index].isupper(): #if character is uppercase
                if char_uni+rotation_amount > 90: #if rotation exceeds 'Z' (90), wrap around
                    encrypted_char = chr(char_uni + rotation_amount - 90 + 64) #wrap to beginning of alphabet
                else:
                    encrypted_char = chr(char_uni + rotation_amount) #rotate character normally
                
                encrypted_message += encrypted_char #add encrypted character to result
        else:
            encrypted_message += message[char_index] #keep non-alphabetic characters unchanged
    
    return encrypted_message #return the encrypted message

def decrypt(message, rotation_amount):
    """
    Decrypts a message using a Caesar cipher with the specified rotation amount.

    Parameters: 
        message (str): The message to be decrypted.
        rotation_amount (int): The number of positions to rotate each letter backwards.

    Returns: 
        str: The decrypted message.
    """
    decrypted_message = "" #initialize empty string for decrypted message
    for char_index in range(len(message)): #iterate through each character in the message
        if message[char_index].isalpha(): #check if character is a letter

            char_uni = ord(message[char_index]) #get unicode value of the character

            if message[char_index].islower(): #if character is lowercase
                if char_uni-rotation_amount < 97: #if rotation goes below 'a' (97), wrap around
                    encrypted_char = chr(char_uni - rotation_amount + 122 - 96) #wrap to end of alphabet
                else:
                    encrypted_char = chr(char_uni - rotation_amount) #rotate character backwards normally
                
                decrypted_message += encrypted_char #add decrypted character to result

            elif message[char_index].isupper(): #if character is uppercase
                if char_uni-rotation_amount < 65: #if rotation goes below 'A' (65), wrap around
                    encrypted_char = chr(char_uni - rotation_amount + 90 - 64) #wrap to end of alphabet
                else:
                    encrypted_char = chr(char_uni - rotation_amount) #rotate character backwards normally
                
                decrypted_message += encrypted_char #add decrypted character to result
        else:
            decrypted_message += message[char_index] #keep non-alphabetic characters unchanged
    
    return decrypted_message #return the decrypted message
    


def displayResult(choice, result_message):
    """
    Displays the encrypted or decrypted message result.
    
    Parameters:
        choice (str): The user's choice ("encrypt" or "decrypt").
        result_message (str): The encrypted or decrypted message to be displayed.
    """
    print(f"\nHere is your {choice}ed message: {result_message}")


#call main function when script is executed
if __name__ == "__main__": 
    main()

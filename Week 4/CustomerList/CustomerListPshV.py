import json
from pathlib import Path


def main():
    """
    Main function to orchestrate the program flow and tell the story of the program.
    """
    #program description function
    displayProgramDescription()

    #display existing entries
    displayInformation()

    #input
    count = getHowManyToAdd()

    #processing
    for x in range(count):
        information = receiveInput()
        writeInput(information)

    #output
    displayInformation()


def displayProgramDescription():
    """
    Displays a brief description of the program's purpose.

    Parameters:
        none

    Returns:
        none
    """
    print("This program stores customer name, address, city, province, and postal code in a text file.\n" +
          "It will show existing data, ask how many customers to add, then collect and save each one.\n" +
          "Postal code must be in Canadian format (L#L #L# or L#L#L#). All data is shown again at the end.\n")



def getFilePath():
    """Returns the path to the customers JSON file."""
    return Path(__file__).resolve().parent / "customers_list.json"


def displayInformation():
    """
    Reads the customers JSON file and prints its contents in a readable format.
    If the file does not exist or is empty, informs the user.

    Parameters:
        none

    Returns:
        none
    """
    filepath = getFilePath()
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
        if isinstance(data, list):
            if not data:
                print("No entry exists yet.\n")
                return
            for entry in data:
                print(f"{json.dumps(entry, indent=4)}\n")
        else:
            print(f"{json.dumps(data, indent=4)}\n")
    except (FileNotFoundError, json.JSONDecodeError):
        print("No entry exists yet.\n")



def getHowManyToAdd():
    """
    Prompts the user for how many customers to add and returns a positive integer.

    Parameters:
        none

    Returns:
        int: Number of customers to add (at least 1).
    """
    while True:
        try:
            value = input("How many customers do you want to add?: ")
            count = int(value)
            if count < 1:
                print("Enter a number greater than 0.")
                continue
            return count
        except ValueError:
            print("Enter a valid whole number.")

def receiveInput():
    """
    Prompts the user for name, address, city, province, and postal code; validates the postal
    code and returns the collected information as a dictionary. 

    Parameters:
        none

    Returns:
        dict: Customer information with keys "name", "address", "city", "province", "postal code".
    """
    name = input("\nWhat is the customer's name: ")
    address = input("What is the address: ")
    city = input("What is the city: ")
    province = input("What is the province: ")
    while True:
        postal_code = input("What is your postal code(The correct format is L#L #L# or L#L#L#): ")
        if validatePostalCode(postal_code):
            break

    information = {
        "name": name,
        "address": address,
        "city": city,
        "province": province,
        "postal code": postal_code,
    }
    return information


def validatePostalCode(postal_code):
    """
    Validates a Canadian postal code by extracting each character and checking that the format
    is L#L#L# (letter, digit, letter, digit, letter, digit), with optional space after the
    third character.

    Parameters:
        postal_code (str): The postal code string to validate.

    Returns:
        bool: True if the format is valid, False otherwise.
    """
    for x in list(postal_code):
        if x == " ":
            postal_code = postal_code.replace(x, "")
    if len(postal_code) != 6:
        print("Wrong input. Postal code must be 6 characters (L#L #L# or L#L#L#).")
        return False
    #check positions: 0, 2, 4 are letters; 1, 3, 5 are digits
    if postal_code[0].isalpha() and postal_code[2].isalpha() and postal_code[4].isalpha() and postal_code[1].isdigit() and postal_code[3].isdigit() and postal_code[5].isdigit():
        return True
    print("Wrong input. Format must be L#L #L# or L#L#L# (L=letter, #=digit).")
    return False


def writeInput(information):
    """
    Appends the given customer information to the customers JSON file.

    Parameters:
        information (dict): Customer data to write (name, address, city, province, postal code).

    Returns:
        none
    """
    filepath = getFilePath()
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
        if not isinstance(data, list):
            data = [data]
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(information)

    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)


#call main function when script is executed
if __name__ == "__main__":
    main()
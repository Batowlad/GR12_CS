import random
from pathlib import Path


def main():
    """
    Main function to orchestrate the program flow and tell the story of the program.
    """
    #program description function
    displayProgramDescription()

    #input
    path_to_directory = getPath()
    quotes_list = getQuotesFromFile(path_to_directory)

    #processing
    if not quotes_list:
        print("The file has no quotes.")
        return

    quote = quoteChoice(quotes_list)

    #output
    displayQuote(quote)


def displayProgramDescription():
    """
    Displays a brief description of the program's purpose.

    Parameters:
        none

    Returns:
        none
    """
    print("This program will ask for the name of a text file containing quotes (e.g. quotes.txt).\n" +
          "Each quote should be on a separate line. The program will then display a random quote.\n" +
          "You can use different files for different categories (e.g. inspirational, thought-provoking).\n")


def getPath():
    """
    Returns the directory containing this script (where quote files are expected).

    Parameters:
        none

    Returns:
        Path: The script's parent directory path.
    """
    script_directory = Path(__file__).resolve().parent
    return script_directory


def getQuotesFromFile(path_to_directory):
    """
    Prompts the user for the name of the text file, opens it with exception handling, reads
    each line into a list (one quote per line), and returns the list. Empty lines are excluded.
    Re-prompts if the file is not found or cannot be read.

    Parameters:
        path_to_directory (Path): Directory path where quote files are stored.

    Returns:
        list: Non-empty lines from the file as quotes; empty list if file has no quotes.
    """
    while True:
        quote_selection = input("Select the genre of the quote you wish to receive(Inspirational or Philosophical): ").lower()
        if quoteValidation(quote_selection, path_to_directory):
            with open(f"{path_to_directory}/{quote_selection}_quotes.txt", "r") as file:
                return file.readlines()


def quoteValidation(quote_selection, path_to_file):
    """
    Checks whether a quote file exists for the given genre selection.

    Parameters:
        quote_selection (str): The genre name (e.g. "inspirational", "philosophical").
        path_to_file (Path): Directory path where quote files are stored.

    Returns:
        bool: True if the file exists, False otherwise. Prints "No such file found." when missing.
    """
    try:
        open(f"{path_to_file}/{quote_selection}_quotes.txt", "r")
        return True
    except FileNotFoundError:
        print("No such file found.")
        return False


def quoteChoice(quotes_list):
    """
    Selects and returns one quote at random from the list.

    Parameters:
        quotes_list (list): List of quote strings.

    Returns:
        str: A randomly chosen quote.
    """
    return random.choice(quotes_list)


def displayQuote(quote):
    """
    Prints the given quote to the console with leading newline.

    Parameters:
        quote (str): The quote text to display.

    Returns:
        none
    """
    print(f"\n{quote}")


#call main function when script is executed
if __name__ == "__main__":
    main()
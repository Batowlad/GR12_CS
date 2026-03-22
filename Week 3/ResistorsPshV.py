#dictionary: colour name -> value (0-9). First two bands = digits; third band = power of 10.
resistor_color_codes = {
    "Black": 0,
    "Brown": 1,
    "Red": 2,
    "Orange": 3,
    "Yellow": 4,
    "Green": 5,
    "Blue": 6,
    "Violet": 7,
    "Grey": 8,
    "White": 9
}

valid_colours_str = "Black, Brown, Red, Orange, Yellow, Green, Blue, Violet, Grey, White"


def main():
    """
    Main function to orchestrate the program flow and tell the story of the program.
    """
    #program description function
    displayProgramDescription()

    #input
    band_tuple = getResistorBandsInput()

    #processing
    resistance_ohms = computeResistance(band_tuple)

    #output
    displayResult(band_tuple, resistance_ohms)


def displayProgramDescription():
    """
    Displays a brief description of the program's purpose.
    """
    print("This program will take three colours from you, separated by hyphens,\n"+
          "and then print the value of the resistor in ohms.\n"+
          "The first two colours are used as ordinary numbers; the third is a power of 10.\n"+
          "Example: Red-Brown-Orange = 21 × 10^3 = 21000 ohms.\n")


def getResistorBandsInput():
    """
    Prompts the user for three colours separated by hyphens and validates the input. Stores them in a tuple.

    Parameters:
        none

    Returns:
        tuple: A tuple of three colour names (e.g. ("Red", "Brown", "Orange")).
    """
    while True:
        #get user input string
        user_input = input("Enter the three band colours separated by hyphens (e.g. Red-Brown-Orange). Valid colours: " + valid_colours_str + ": ")
        #store the three colours in a tuple (never in a list first, per assignment)
        band_tuple = tuple(part.strip() for part in user_input.split("-"))
        if len(band_tuple) != 3:
            print("Please enter exactly three colours separated by hyphens (e.g. Red-Brown-Orange).")
            continue
        if not all(band in resistor_color_codes for band in band_tuple):
            print("Each band must be one of: " + valid_colours_str + ".")
            continue
        print("") #insert spacing
        return band_tuple #return the tuple of three colour names


def computeResistance(band_tuple):
    """
    Computes the resistance in ohms: first two bands form a two-digit number, third band is the exponent of 10.

    Parameters:
        band_tuple (tuple): Tuple of three colour names.

    Returns:
        int: The resistance in ohms.
    """
    digit_one = resistor_color_codes[band_tuple[0]]
    digit_two = resistor_color_codes[band_tuple[1]]
    multiplier_exponent = resistor_color_codes[band_tuple[2]]
    base_value = digit_one * 10 + digit_two
    return base_value * (10 ** multiplier_exponent)


def displayResult(band_tuple, resistance_ohms):
    """
    Displays the band colours and the computed resistance in ohms.

    Parameters:
        band_tuple (tuple): The three band colour names.
        resistance_ohms (int): The resistance value in ohms.
    """
    bands_str = "-".join(band_tuple) #join the band colours for display
    print(f"Bands: {bands_str}")
    print(f"Resistance: {resistance_ohms} ohms (Ω)")


#call main function when script is executed
if __name__ == "__main__":
    main()

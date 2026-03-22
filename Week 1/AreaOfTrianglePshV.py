import math

def main():
    """
    Main function to orchestrate the program flow and tell the story of the program.
    """
    #program description function
    displayProgramDescription()
    
    #input
    side_a = receiveInput("side", "side a that has to be above 0")
    side_b = sideBInput(side_a)
    angle_C = receiveInput("angle", "angle C that has to be in the range between 1 and 180")

    #processing
    area_of_triangle = areaOfTriangle(side_a, side_b, angle_C)
    #output
    displayResult(side_a, side_b, angle_C, area_of_triangle)



def displayProgramDescription():
    """
    Displays a brief description of the program's purpose. 
    """
    print("This program will 2 sides and an angle,\n"+
          "and calculate the area of the triangle\n"+
          "using trigonometry, and output the result.\n")
    


def receiveInput(value_type, value_description):
    """
    Prompts the user to enter a value and validates the input based on the value type.

    Parameters: 
        value_type (str): The type of value to receive ("side" or "angle").
        value_description (str): Description of what value to input.

    Returns: 
        int or float: The validated input value (int for sides, float for angles).
    """
    while True:
        input_value = input(f"Enter the {value_description}: ")
        if value_type == "side":
            if isSideAcceptable(input_value):
                print("")
                return int(input_value) #cast the input value to int
            
        elif value_type == "angle":
                if isAngleAcceptable(input_value):
                    print("")
                    return float(input_value) #cast the input value to float


def isSideAcceptable(value):
    """
    Validates user's input for a side based on criteria: must be a positive integer greater than 0.

    Parameters: 
        value (str): User's input that needs to be validated.

    Returns: 
        bool: True if the input matches the criteria, False if it doesn't.
    """
    try: 
        side = int(value) #cast the variable to int
        if side < 0:
            print("Input a number larger than 0.")
            return False #a number is not greater than 0
        else:
            
            return True #a number is greater than 0
    except:
        print("Input an integer.")
        return False #the input is not a number


def sideBInput(side_a):
    """
    Prompts the user to enter side b and validates that it is different from side a.

    Parameters: 
        side_a (int): The value of side a that side b must be different from.

    Returns: 
        int: A validated side b value that is different from side a.
    """
    while True:
        side_b = receiveInput("side", "side b that has to be above 0")
        if side_a == side_b:
            print("Side b cannot equal side a.")
        else:
            return side_b


def isAngleAcceptable(value):
    """
    Validates user's input for an angle based on criteria: must be a number between 0 and 180.

    Parameters: 
        value (str): User's input that needs to be validated.

    Returns: 
        bool: True if the input matches the criteria, False if it doesn't.
    """
    try:
        angle = float(value)
        if 0 < angle < 180:
            return True #an angle is in the range between 0 and 180
        else:
            print("Angle value has to be in the range between 0 and 180.")
            return False #an angle is not in the range between 0 and 180
    except:
        print("Input a number.")
        return False #the input is not a number


def areaOfTriangle(a, b, C):
    """
    Calculates the area of a triangle using two sides and the included angle.

    Parameters: 
        a (int): Length of side a.
        b (int): Length of side b.
        C (float): Angle C in degrees between sides a and b.

    Returns: 
        float: The calculated area of the triangle.
    """
    area = (a*b*(math.sin(math.radians(C))))/2
    return area


def displayResult(a, b, C, area):
    """
    Displays the triangle area calculation result.

    Parameters:
        a (int): Length of side a.
        b (int): Length of side b.
        C (float): Angle C in degrees.
        area (float): The calculated area of the triangle.
    """
    print(f"Triangle with sides {a} and {b}, and an angle {C} will result in an area of {area}.")

#call main function when script is executed
if __name__ == "__main__":
    main()
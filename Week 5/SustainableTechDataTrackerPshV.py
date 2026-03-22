import json
import os

#name of the JSON file where data centre records are stored
DATA_FILE_NAME = "data_centre_records.json"


def main():
    """
    Main function to orchestrate the program flow and tell the story of the program.
    """
    #program description function
    displayProgramDescription()

    #load the data
    records_list = loadData()


    while True:
        #input
        user_choice = displayMenuAndGetChoice()

        #processing and output
        if user_choice == '1':
            viewRecords(records_list)
        elif user_choice == '2':
            addRecord(records_list)
        elif user_choice == '3':
            editRecord(records_list)
        elif user_choice == '4':
            deleteRecord(records_list)
        elif user_choice == '5':
            analyzeRecords(records_list)
        elif user_choice == '6':
            saveData(records_list)
            return #exit program after saving
        else:
            print("\nError: Invalid choice. Please type a number between 1 and 6.\n")


def displayProgramDescription():
    """
    Displays a brief description of the program's purpose.
    """
    print("=====================================================")
    print("    AI Data Centre Energy Tracker - Sustainability   ")
    print("=====================================================")
    print("This program helps you track and analyze the")
    print("energy consumption of various AI data centres.")
    print("You can add, edit, delete, and analyze records to")
    print("better understand their environmental impact.")
    print("=====================================================\n")


def getValidFloat(prompt_message):
    """
    Prompts the user for a numeric (float) input and handles invalid entries.

    Parameters:
        prompt_message (str): The message displayed to the user.

    Returns:
        float: A validated float number.
    """
    while True:
        try:
            user_input = float(input(prompt_message))
            if user_input < 0:
                print("Please enter a positive number.\n")
            else:
                return user_input #return the validated float
        except ValueError:
            print("Invalid input. Please enter numbers only.\n")



def getValidInteger(prompt_message):
    """
    Prompts the user for an integer input and handles invalid entries.

    Parameters:
        prompt_message (str): The message displayed to the user.

    Returns:
        int: A validated integer number.
    """
    while True:
        try:
            return int(input(prompt_message)) #return the validated integer
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")

    


def loadData():
    """
    Loads saved data centre records from a JSON file if it exists.

    Parameters:
        none

    Returns:
        list: A list of dictionaries containing data centre records.
    """
    records_list = []
    if os.path.exists(DATA_FILE_NAME):
        try:
            with open(DATA_FILE_NAME, "r") as file_reference:
                records_list = json.load(file_reference)
        except json.JSONDecodeError:
            print("Error reading file.\n")
    else:
        print("No existing data file found.\n")

    return records_list #return the list of loaded records


def saveData(records_list):
    """
    Saves the current list of data centre records to a JSON file.

    Parameters:
        records_list (list): The list of dictionaries to save.

    Returns:
        none
    """
    try:
        with open(DATA_FILE_NAME, "w") as file_reference:
            json.dump(records_list, file_reference, indent=4)

        print("\nData successfully saved. Thank you for using the tracker!")
    except IOError:
        print("\nError: Could not save data to file.")


def displayMenuAndGetChoice():
    """
    Displays the main menu options and collects the user's choice.

    Parameters:
        none

    Returns:
        str: The user's menu selection.
    """
    print("---------------------------------------")
    print("               MAIN MENU               ")
    print("---------------------------------------")
    print("1. View Data Centres")
    print("2. Add a Data Centre")
    print("3. Edit a Data Centre")
    print("4. Delete a Data Centre")
    print("5. Analyze Sustainability Data")
    print("6. Save and Exit")
    print("---------------------------------------")

    user_choice = input("Enter your choice (1-6): ")
    return user_choice #return the user's menu selection


def viewRecords(records_list):
    """
    Displays all stored data centre records in a formatted list.

    Parameters:
        records_list (list): The list of data centre records.

    Returns:
        none
    """
    print("\n--- Current Data Centre Records ---")
    if len(records_list) == 0:
        print("No data centres currently tracked.")
    else:
        for index, centre in enumerate(records_list):
            print(f"[{index + 1}] Facility Name: {centre['facility_name']}")
            print(f"    Energy Consumed: {centre['energy_mwh']} MWh")
            print(f"    Renewable Share: {centre['renewable_percent']}%")
            print("    - - - - - - - - - - - - - - - -")
    print("\n")


def addRecord(records_list):
    """
    Prompts the user for new data centre information and adds it to the list.

    Parameters:
        records_list (list): The current list of data centre records.

    Returns:
        none
    """
    print("\n--- Add New Data Centre ---")
    facility_name = input("Enter the facility name (e.g., 'Google Dalles'): ")
    energy_mwh = getValidFloat("Enter total energy consumed (in MWh): ")
    renewable_percent = getValidFloat("Enter the percentage of renewable energy used (0-100): ")

    new_record = {
        "facility_name": facility_name,
        "energy_mwh": energy_mwh,
        "renewable_percent": renewable_percent
    }
    records_list.append(new_record)

    print(f"\nSuccess: '{facility_name}' has been added to the tracker.\n")


def editRecord(records_list):
    """
    Allows the user to select an existing record and update its data.

    Parameters:
        records_list (list): The current list of data centre records.

    Returns:
        none
    """
    if len(records_list) == 0:
        print("\nNo records available to edit.\n")
        return #no records to edit

    viewRecords(records_list)
    index = getValidInteger("Enter the number of the record you want to edit: ") - 1

    if 0 <= index < len(records_list):
        print(f"\nEditing: {records_list[index]['facility_name']}")
        new_energy = getValidFloat("Enter the updated energy consumption (MWh): ")
        new_renewable = getValidFloat("Enter the updated renewable energy percentage (0-100): ")

        records_list[index]['energy_mwh'] = new_energy
        records_list[index]['renewable_percent'] = new_renewable

        print("\nSuccess: Record has been updated.\n")
    else:
        print("\nError: Invalid record number.\n")


def deleteRecord(records_list):
    """
    Allows the user to select an existing record and delete it.

    Parameters:
        records_list (list): The current list of data centre records.

    Returns:
        none
    """

    if len(records_list) == 0:
        print("\nNo records available to delete.\n")
        return #no records to delete

    viewRecords(records_list)
    index = getValidInteger("Enter the number of the record you want to delete: ") - 1

    if 0 <= index < len(records_list):
        deleted_name = records_list[index]['facility_name']
        del records_list[index]
        print(f"\nSuccess: '{deleted_name}' has been deleted.\n")
    else:
        print("\nError: Invalid record number.\n")


def analyzeRecords(records_list):
    """
    Performs basic sustainability analysis on the stored data.

    Parameters:
        records_list (list): The current list of data centre records.

    Returns:
        none
    """
    if len(records_list) == 0:
        print("\nNot enough data to perform analysis. Please add records first.\n")
        return #not enough data for analysis

    total_energy = 0.0
    total_renewable = 0.0
    highest_consumer = {}
    max_energy = -1.0

    for centre in records_list:
        total_energy += centre['energy_mwh']
        total_renewable += centre['energy_mwh'] * (centre['renewable_percent'] / 100)
        if centre['energy_mwh'] > max_energy:
            max_energy = centre['energy_mwh']
            highest_consumer = centre

    print("\n--- Sustainability Analysis Report ---")
    print(f"Total Facilities Tracked: {len(records_list)}")
    print(f"Total Energy Consumed:    {total_energy:.2f} MWh")
    print(f"Average Consumption:      {total_energy / len(records_list):.2f} MWh")
    print(f"Overall Renewable Share:  {(total_renewable / total_energy) * 100 if total_energy > 0 else 0.0:.2f}%")
    print("\n")
    print(f"Highest Energy Consumer:  {highest_consumer['facility_name']} ({highest_consumer['energy_mwh']} MWh)")
    print("\n")


#call main function when script is executed
if __name__ == "__main__":
    main()

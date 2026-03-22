import random

#board cell constants: 0 = empty, 1 = first player, 4 = second player
cell_empty = 0
player_mark = 1
ai_mark = 4
board_size = 3

#first player's marker = 1 (sum 3 wins); second player's marker = 4 (sum 12 wins)
winning_sum_first = 3
winning_sum_second = 12


def main():
    """
    Main function to orchestrate the program flow and tell the story of the program.
    """
    #program description function
    displayProgramDescription()

    #input
    player_goes_first = getGoFirstOrSecond()
    game_board = createEmptyBoard()

    #processing and output
    runGameLoop(game_board, player_goes_first)


def displayProgramDescription():
    """
    Displays a brief description of the program's purpose.
    """
    print("This program will let you play Tic-Tac-Toe against the computer.\n"+
          "You will enter your position as a row number and a column number separated by a space.\n"+
          "Top-left is 1 1, bottom-right is 3 3 (e.g. 2 2 for the center).\n"+
          "First player uses 1, second player uses 4. You cannot choose a spot that is already taken.\n")


def getGoFirstOrSecond():
    """
    Prompts the user to choose whether to go first or second and validates the input.

    Parameters:
        none

    Returns:
        bool: True if the user goes first, False if the user goes second.
    """
    while True:
        #get user input
        choice = input("Do you want to go first or second? Enter 1 to go first, 2 to go second: ")
        if choice.strip() == "1":
            print("") #insert spacing
            return True #return that the user goes first
        if choice.strip() == "2":
            print("") #insert spacing
            return False #return that the user goes second
        print("Please enter 1 to go first or 2 to go second.") #display error message if input is invalid


def createEmptyBoard():
    """
    Creates and returns a 3x3 board filled with empty cells (0).

    Parameters:
        none

    Returns:
        list: A 2D list representing the game board.
    """
    return [
        [cell_empty, cell_empty, cell_empty],
        [cell_empty, cell_empty, cell_empty],
        [cell_empty, cell_empty, cell_empty]
    ]


def displayBoard(board):
    """
    Prints the current state of the game board to the console.

    Parameters:
        board (list): The 2D list representing the game board.
    """
    print("\n")
    for row in board:
        #join the elements of the row into a single string for display
        print(" ".join(str(cell) for cell in row))
    print("\n")


def getPlayerPosition(board):
    """
    Prompts the user for a board position and validates it (must be empty and in range).

    Parameters:
        board (list): The current game board.

    Returns:
        tuple: (row_index, col_index) as zero-based indices.
    """
    while True:
        #get user input
        user_input = input("Enter row number and column number separated by a space (top-left is 1 1, bottom-right is 3 3): ")
        parts = user_input.split()

        if len(parts) != 2:
            print("Please enter exactly two numbers (row and column) separated by a single space.")
            continue

        try: #try the following...
            row_index = int(parts[0]) - 1
            col_index = int(parts[1]) - 1
        except ValueError: #if casting to int fails...
            print("Please enter valid numbers.")
            continue

        if row_index < 0 or row_index >= board_size or col_index < 0 or col_index >= board_size:
            print("Row and column must each be 1, 2, or 3 (top-left is 1 1, bottom-right is 3 3).")
            continue

        if board[row_index][col_index] != cell_empty:
            print("That location is already taken. Choose an empty spot.")
            continue

        return row_index, col_index #return the validated position


def checkWinner(board):
    """
    Determines the winner by calculating the sum of each row, column, and diagonal.
    First player (marker 1) wins when a sum is 3; second player (marker 4) wins when a sum is 12.

    Parameters:
        board (list): The current game board.

    Returns:
        int or None: player_mark if first player wins, ai_mark if second player wins, None if no winner yet.
    """
    #check sum of each row
    for row in board:
        row_sum = row[0] + row[1] + row[2]
        if row_sum == winning_sum_first:
            return player_mark
        if row_sum == winning_sum_second:
            return ai_mark

    #check sum of each column
    for col_index in range(board_size):
        col_sum = board[0][col_index] + board[1][col_index] + board[2][col_index]
        if col_sum == winning_sum_first:
            return player_mark
        if col_sum == winning_sum_second:
            return ai_mark

    #check sum of main diagonal
    main_diag_sum = board[0][0] + board[1][1] + board[2][2]
    if main_diag_sum == winning_sum_first:
        return player_mark
    if main_diag_sum == winning_sum_second:
        return ai_mark

    #check sum of anti-diagonal
    anti_diag_sum = board[0][2] + board[1][1] + board[2][0]
    if anti_diag_sum == winning_sum_first:
        return player_mark
    if anti_diag_sum == winning_sum_second:
        return ai_mark

    return None #no winner yet


def isBoardFull(board):
    """
    Returns True if every cell on the board is occupied.

    Parameters:
        board (list): The current game board.

    Returns:
        bool: True if the board is full, False if it doesn't.
    """
    for row in board:
        for cell in row:
            if cell == cell_empty:
                return False #board is not full
    return True #board is full


def makeAIMove(board):
    """
    Chooses a random empty cell and places the computer's mark (4) there.

    Parameters:
        board (list): The current game board (modified in place).

    Returns:
        none
    """
    while True:
        row_index = random.randint(0, board_size - 1)
        col_index = random.randint(0, board_size - 1)
        if board[row_index][col_index] == cell_empty:
            board[row_index][col_index] = ai_mark
            break


def runGameLoop(board, player_goes_first):
    """
    Runs the main game loop. If the player goes second, the computer moves first.
    After each turn the entire board is displayed. Game ends when there is a winner or the board is full.

    Parameters:
        board (list): The game board (modified in place).
        player_goes_first (bool): True if the user plays first (marker 1), False if second (marker 4).

    Returns:
        none
    """
    if not player_goes_first:
        makeAIMove(board)
        print("The computer has made its move.")
        displayBoard(board)

    while True:
        #player turn: get position and place mark
        row_index, col_index = getPlayerPosition(board)
        board[row_index][col_index] = player_mark

        displayBoard(board)
        winner = checkWinner(board)
        if winner is not None:
            displayFinalBoardAndAnnounceWinner(board, winner, player_goes_first)
            return
        if isBoardFull(board):
            displayBoard(board)
            print("Cat's game! There is no winner.")
            return

        #computer turn: choose random empty cell
        makeAIMove(board)
        print("The computer has made its move.")
        displayBoard(board)

        winner = checkWinner(board)
        if winner is not None:
            displayFinalBoardAndAnnounceWinner(board, winner, player_goes_first)
            return
        if isBoardFull(board):
            displayBoard(board)
            print("Cat's game! There is no winner.")
            return


def displayFinalBoardAndAnnounceWinner(board, winner, player_goes_first):
    """
    Announces the winner (the final board was already displayed after the last move).

    Parameters:
        board (list): The final game board (already shown to the user).
        winner (int): player_mark (1) or ai_mark (4).
        player_goes_first (bool): True if the user is the first player.
    """
    if winner == player_mark: #if first player won...
        if player_goes_first:
            print("You win!")
        else:
            print("The computer wins.")
    else: #if second player won...
        if player_goes_first:
            print("The computer wins.")
        else:
            print("You win!")


#call main function when script is executed
if __name__ == "__main__":
    main()

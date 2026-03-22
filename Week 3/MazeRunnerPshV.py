def main():
    """
    Main function to orchestrate the program flow and tell the story of the program.
    """
    #program description function
    displayProgramDescription()

    #input
    maze_grid = buildMaze()
    player_row, player_col = getInitialPlayerPosition()

    #processing and output
    runMazeGameLoop(maze_grid, player_row, player_col)


def displayProgramDescription():
    """
    Displays a brief description of the program's purpose.
    """
    print("This program is a maze game. Navigate from the start (*) to the exit (E).\n"+
          "Walls are shown as X; you cannot move through them. Reach E to win.\n")


def buildMaze():
    """
    Builds and returns the 10x10 maze grid. Walls are " X ", empty cells "   ", exit " E ".

    Parameters:
        none

    Returns:
        list: A 2D list representing the maze. Start is at (0, 1).
    """
    #start at (0, 1); exit 'E' at (7, 6)
    maze_grid = [
        [" X ", " * ", " X ", " X ", " X ", " X ", " X ", " X ", " X ", " X "],
        [" X ", "   ", "   ", "   ", "   ", "   ", " X ", "   ", "   ", " X "],
        [" X ", " X ", " X ", " X ", " X ", "   ", " X ", "   ", " X ", " X "],
        [" X ", "   ", "   ", "   ", " X ", "   ", " X ", "   ", "   ", " X "],
        [" X ", "   ", " X ", "   ", " X ", "   ", " X ", " X ", "   ", " X "],
        [" X ", "   ", " X ", "   ", "   ", "   ", "   ", " X ", "   ", " X "],
        [" X ", "   ", " X ", " X ", " X ", " X ", " X ", " X ", "   ", " X "],
        [" X ", "   ", "   ", "   ", "   ", "   ", " E ", " X ", "   ", " X "],
        [" X ", " X ", " X ", " X ", " X ", " X ", " X ", " X ", "   ", " X "],
        [" X ", " X ", " X ", " X ", " X ", " X ", " X ", " X ", " X ", " X "]
    ]
    return maze_grid #return the 2D list representing the maze


def getInitialPlayerPosition():
    """
    Returns the starting position of the player (top-left opening).

    Parameters:
        none

    Returns:
        tuple: (row_index, col_index) for the starting cell.
    """
    return 0, 1


def displayMaze(maze_grid):
    """
    Prints the current state of the maze to the console.

    Parameters:
        maze_grid (list): The 2D list representing the maze.
    """
    print("\n\n")
    for row in maze_grid:
        #join the elements of the row into a single string for display
        print("".join(row))
    print("\n")


def getPlayerMove():
    """
    Prompts the user for a move and returns the chosen direction.

    Parameters:
        none

    Returns:
        str: One of 'W', 'A', 'S', 'D', or 'Q' (uppercase).
    """
    #get user input and convert to uppercase
    move = input("Enter your move: W (up), A (left), S (down), D (right), or Q (quit): ").upper()
    return move #return the validated move


def runMazeGameLoop(maze_grid, player_row, player_col):
    """
    Main game loop: display maze, get move, validate, update position, check win or wall.

    Parameters:
        maze_grid (list): The maze (modified in place; player marked as " * ").
        player_row (int): Current player row index.
        player_col (int): Current player column index.

    Returns:
        none
    """
    print("Welcome to the Maze!")
    print("Enter one letter per move: W = Up, S = Down, A = Left, D = Right. Enter Q to quit.")
    print("After each move you will see the maze and your position (*).\n")

    while True:
        displayMaze(maze_grid)
        move = getPlayerMove()

        if move == "Q":
            print("Thanks for playing! Goodbye.")
            break

        #calculate where the player is trying to go
        new_row, new_col = player_row, player_col
        if move == "W":
            new_row -= 1
        elif move == "S":
            new_row += 1
        elif move == "A":
            new_col -= 1
        elif move == "D":
            new_col += 1
        else:
            print("Invalid input. Please enter one letter: W, A, S, or D (or Q to quit).")
            continue

        #prevent the player from moving outside the bounds of the array
        if new_row < 0 or new_row >= len(maze_grid) or new_col < 0 or new_col >= len(maze_grid[0]):
            print("You can't move outside the maze boundaries!")
            continue

        #collision detection: wall
        if maze_grid[new_row][new_col] == " X ":
            print("You hit a wall. Try a different direction.")
            continue

        #win condition: reached exit
        if maze_grid[new_row][new_col] == " E ":
            maze_grid[player_row][player_col] = "   "
            maze_grid[new_row][new_col] = " * "
            displayMaze(maze_grid)
            print("Congratulations! You found the exit!")
            break

        #move the player: clear old position, set new position
        maze_grid[player_row][player_col] = "   "
        maze_grid[new_row][new_col] = " * "
        player_row, player_col = new_row, new_col


#call main function when script is executed
if __name__ == "__main__":
    main()

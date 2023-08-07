def print_board(board):
    """
    Prints the game board using '|' and '-' to form a grid.

    Args:
        board (list of list): The game board.
    """
    print('-------------')
    for row in board:
        print('|', end='')
        for cell in row:
            if cell == '':
                print('   |', end='')
            else:
                print(f' {cell} |', end='')
        print('\n-------------')


def check_win(board):
    """
    Checks if a player has won the game.

    Args:
        board (list of list): The game board.

    Returns:
        bool: True if a player has won, False otherwise.
    """
    # check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != "":
            return True
    # check columns
    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != "":
            return True
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return True
    return False


def check_draw(board):
    """
    Checks if the game is a draw.

    Args:
        board (list of list): The game board.

    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    for row in board:
        if "" in row:
            return False
    return True


def game():
    """
    Implements the game loop for Tic Tac Toe.

    This function first creates a game board, then enters a loop that continues until a player wins or the game
    is a draw.
    In each loop iteration, the current player is prompted to select a row and column on the board to make a move.
    If the selected spot on the board is empty, the player's move is made and the game status is checked.
    If a player has won or the game is a draw, the game ends and a message is printed.
    If the game has not ended, the current player switches and the next loop iteration begins.

    Note: This function now handles invalid user input.
    """
    # Create a 3x3 game board
    board = [["" for _ in range(3)] for _ in range(3)]

    # Define the current player
    current_player = "X"

    # Game loop
    while True:
        # Display the game board
        print_board(board)

        # Get the current player's move
        while True:
            try:
                row = int(input("Enter the row number (0, 1, 2): "))
                col = int(input("Enter the column number (0, 1, 2): "))
                if row in [0, 1, 2] and col in [0, 1, 2] and board[row][col] == "":
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a valid number.")

        # Make the current player's move
        board[row][col] = current_player

        # Check if the current player has won
        if check_win(board):
            print("Player", current_player, "wins!")
            break

        # Check if the game is a draw
        if check_draw(board):
            print("The game is a draw!")
            break

        # Switch the current player
        current_player = "O" if current_player == "X" else "X"


game()

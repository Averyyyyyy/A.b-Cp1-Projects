#Avery tic tac toe board

import random

# Initialize the board
board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    """Print the current state of the board using a nested loop."""
    print("Current Board:")
    for row in board:
        for cell in row:
            print(cell, end="|")
        print()  # Move to the next line after a row
        print("-" * 5)

def check_winner():
    """Check for a winner or a draw."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":  # Row
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":  # Column
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Check for draw
    if all(cell != " " for row in board for cell in row):
        return "Draw"

    return None

def user_turn():
    """Handle the user's turn."""
    while True:
        try:
            move = input("Enter your move (row and column, e.g., 1 2): ").strip()
            row, col = map(int, move.split())
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("That spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column numbers between 0 and 2.")

def computer_turn():
    """Handle the computer's turn."""
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = "O"
            print(f"Computer chose: {row} {col}")
            break

def play_game():
    """Main function to play the game."""
    print("Welcome to Tic-Tac-Toe!")
    print("You are X and the computer is O.")
    print("Enter your move as row and column numbers separated by a space (e.g., 0 1).")
    
    print_board()
    while True:
        # User's turn
        user_turn()
        print_board()
        result = check_winner()
        if result:
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"{result} wins!")
            break
        
        # Computer's turn
        computer_turn()
        print_board()
        result = check_winner()
        if result:
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"{result} wins!")
            break

# Start the game
play_game()

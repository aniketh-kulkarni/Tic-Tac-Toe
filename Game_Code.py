import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def check_winner(board, symbol):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def get_valid_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                row, col = divmod(move - 1, 3)
                if board[row][col] == ' ':
                    return row, col
                else:
                    print("The chosen square is already occupied. Try again.")
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")

    # Computer's first move
    board[1][1] = 'X'
    print_board(board)

    while True:
        # Player's move
        row, col = get_valid_move(board)
        board[row][col] = 'O'
        print_board(board)

        # Check if the player wins
        if check_winner(board, 'O'):
            print("Congratulations! You win!")
            break

        # Check for a tie
        if is_board_full(board):
            print("It's a tie!")
            break

        # Computer's move
        while True:
            comp_row, comp_col = random.randint(0, 2), random.randint(0, 2)
            if board[comp_row][comp_col] == ' ':
                board[comp_row][comp_col] = 'X'
                print("Computer's move:")
                print_board(board)
                break

        # Check if the computer wins
        if check_winner(board, 'X'):
            print("Sorry, the computer wins. Better luck next time!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()

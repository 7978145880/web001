def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True

    if all([board[i][i] == player for i in range(3)]):  # Check diagonal from top-left to bottom-right
        return True

    if all([board[i][2 - i] == player for i in range(3)]):  # Check diagonal from top-right to bottom-left
        return True

    return False

def is_board_full(board):
    return all([board[i][j] != " " for i in range(3) for j in range(3)])

def get_move(player):
    while True:
        try:
            row = int(input(f"Player '{player}', enter row number (1-3): ")) - 1
            col = int(input(f"Player '{player}', enter column number (1-3): ")) - 1

            if 0 <= row < 3 and 0 <= col < 3:
                return row, col
            else:
                print("Invalid input! Row and column should be between 1 and 3.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Tic Tac Toe Game")

    while True:
        print_board(board)
        player = players[current_player]

        row, col = get_move(player)

        if board[row][col] == " ":
            board[row][col] = player
            if check_win(board, player):
                print_board(board)
                print(f"Player '{player}' wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                current_player = (current_player + 1) % 2
        else:
            print("Cell already occupied! Try again.")

if __name__ == "__main__":
    tic_tac_toe()

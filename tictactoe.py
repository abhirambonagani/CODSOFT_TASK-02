import random


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves


def evaluate(board):
    winner = check_winner(board)
    if winner == "X":
        return 1
    elif winner == "O":
        return -1
    else:
        return 0


def minimax(board, depth, maximizing_player):
    if check_winner(board) == "X":
        return 1
    elif check_winner(board) == "O":
        return -1
    elif len(available_moves(board)) == 0:
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in available_moves(board):
            board[move[0]][move[1]] = "X"
            eval = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in available_moves(board):
            board[move[0]][move[1]] = "O"
            eval = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = " "
            min_eval = min(min_eval, eval)
        return min_eval


def best_move(board):
    best_eval = float('-inf')
    best_move = None
    for move in available_moves(board):
        board[move[0]][move[1]] = "X"
        eval = minimax(board, 0, False)
        board[move[0]][move[1]] = " "
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while not check_winner(board) and len(available_moves(board)) > 0:
        player_move = input("Enter your move (row col): ").split()
        row, col = int(player_move[0]), int(player_move[1])
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = "O"
        print_board(board)
        if check_winner(board):
            print("You win!")
            break
        if len(available_moves(board)) == 0:
            print("It's a draw!")
            break
        print("AI is thinking...")
        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = "X"
        print_board(board)
        if check_winner(board):
            print("AI wins!")
            break
        if len(available_moves(board)) == 0:
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()

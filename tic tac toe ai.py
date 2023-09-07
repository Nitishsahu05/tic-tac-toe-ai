import math

# The game board
board = [' ' for _ in range(9)]

# Winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]            # Diagonals
]

# Function to print the game board
def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---------")

# Function to check if a player has won
def is_winner(player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check if the game is a draw
def is_draw():
    return ' ' not in board

# Function to evaluate the current state of the board
def evaluate_board():
    if is_winner('X'):
        return 1
    elif is_winner('O'):
        return -1
    else:
        return 0

# Minimax algorithm with Alpha-Beta Pruning
def minimax(position, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_winner('X') or is_winner('O') or is_draw():
        return evaluate_board()

    if maximizing_player:
        max_eval = -math.inf
        for move in range(9):
            if board[move] == ' ':
                board[move] = 'X'
                eval = minimax(board, depth - 1, alpha, beta, False)
                board[move] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for move in range(9):
            if board[move] == ' ':
                board[move] = 'O'
                eval = minimax(board, depth - 1, alpha, beta, True)
                board[move] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# AI player's move using Minimax
def ai_move():
    best_move = -1
    best_eval = -math.inf
    for move in range(9):
        if board[move] == ' ':
            board[move] = 'X'
            eval = minimax(board, 5, -math.inf, math.inf, False)
            board[move] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = move
    board[best_move] = 'X'

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    
    while not is_winner('X') and not is_winner('O') and not is_draw():
        player_move = int(input("Enter your move (1-9): ")) - 1
        if board[player_move] == ' ':
            board[player_move] = 'O'
            print_board()
        else:
            print("Invalid move. Try again.")
            continue
        
        if is_winner('O'):
            print("You win! Game over.")
            break
        elif is_draw():
            print("It's a draw! Game over.")
            break
        
        print("AI's move:")
        ai_move()
        print_board()
        
        if is_winner('X'):
            print("AI wins! Game over.")
            break
        elif is_draw():
            print("It's a draw! Game over.")
            break

# Start the game
play_game()

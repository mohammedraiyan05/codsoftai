import math

# Initialize board
board = [' ' for _ in range(9)]

# Print board
def print_board():
    for i in range(3):
        print(board[i*3] + ' | ' + board[i*3+1] + ' | ' + board[i*3+2])
        if i < 2:
            print("--+---+--")

# Check winner
def check_winner(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combinations)

# Check for tie
def is_board_full():
    return ' ' not in board

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner('X'):
        return 1
    if check_winner('O'):
        return -1
    if is_board_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'X'

# Player move
def player_move():
    while True:
        try:
            pos = int(input("Enter your move (1-9): ")) - 1
            if board[pos] == ' ':
                board[pos] = 'O'
                break
            else:
                print("That spot is already taken.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number from 1 to 9.")

# Game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are O. The AI is X.")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner('O'):
            print("You win! 🎉")
            break
        if is_board_full():
            print("It's a tie!")
            break

        print("AI is making a move...")
        ai_move()
        print_board()
        if check_winner('X'):
            print("AI wins! 😎")
            break
        if is_board_full():
            print("It's a tie!")
            break

# Start the game
play_game()

import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check if there's a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([s == player for s in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Check if the board is full
def is_board_full(board):
    return all([cell != ' ' for row in board for cell in row])

# Minimax function
def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    # Check for terminal states
    if check_winner(board, 'O'):  # AI wins
        return 1
    if check_winner(board, 'X'):  # Human wins
        return -1
    if is_board_full(board):  # Draw
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:  # Alpha-Beta Pruning
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:  # Alpha-Beta Pruning
                        break
        return best_score

# Function to find the best move for the AI
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'  # AI is 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, and AI is O.")
    
    while True:
        print_board(board)

        # Human player's turn
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))
        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            print("Cell already taken. Try again.")
            continue

        # Check if the human won
        if check_winner(board, 'X'):
            print_board(board)
            print("Congratulations! You win!")
            break

        # Check if the board is full (draw)
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI's turn
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = 'O'
        
        # Check if AI won
        if check_winner(board, 'O'):
            print_board(board)
            print("AI wins! Better luck next time.")
            break

        # Check if the board is full (draw)
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

# Start the game
play_game()

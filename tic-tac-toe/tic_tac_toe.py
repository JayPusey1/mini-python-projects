import random

board = [" "] * 9

def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print(" ")

def check_winner(board):
    if board[0] == board[1] == board[2] and board[0] != " ":
        return board[0]
    elif board[3] == board[4] == board[5] and board[3] != " ":
        return board[3]
    elif board[6] == board[7] == board[8] and board[6] != " ":
        return board[6]
    elif board[0] == board[3] == board[6] and board[0] != " ":
        return board[0]
    elif board[1] == board[4] == board[7] and board[1] != " ":
        return board[1]
    elif board[2] == board[5] == board[8] and board[2] != " ":
        return board[2]
    elif board[0] == board[4] == board[8] and board[0] != " ":
        return board[0]
    elif board[2] == board[4] == board[6] and board[2] != " ":
        return board[2]
    return None

def check_game_over(board, user_symbol, program_symbol):
    winner = check_winner(board)
    if winner:
        if winner == user_symbol:
            print("You win!")
        else:
            print("Computer wins!")
        return True

    if " " not in board:
        print("It's a draw!")
        return True

    return False

# Randomise who is X / O
team = random.randrange(1, 3)
if team == 1:
    user_symbol = "X"
    program_symbol = "O"
    print("You are X")
else:
    user_symbol = "O"
    program_symbol = "X"
    print("You are O")

print("X goes first.")
print_board(board)

current_turn = "X"

while True:
    # --- USER TURN ---
    if current_turn == user_symbol:
        user_input = input("Enter a number between 1-9: ")

        # Stop it crashing if they type letters
        if not user_input.isdigit():
            print("Enter a valid number between 1-9.")
            continue

        user_num = int(user_input)

        # Range check
        if user_num < 1 or user_num > 9:
            print("Enter a valid number between 1-9.")
            continue

        user_answer = user_num - 1

        # Empty square check
        if board[user_answer] != " ":
            print("That square is taken. Pick another.")
            continue

        board[user_answer] = user_symbol
        print_board(board)

        if check_game_over(board, user_symbol, program_symbol):
            break

        # Switch turn
        current_turn = "O" if current_turn == "X" else "X"

    # --- COMPUTER TURN ---
    else:
        empty_positions = []
        for i in range(9):
            if board[i] == " ":
                empty_positions.append(i)

        program_answer = random.choice(empty_positions)
        board[program_answer] = program_symbol

        print(f"Computer picked {program_answer + 1}.")
        print_board(board)

        if check_game_over(board, user_symbol, program_symbol):
            break

        # Switch turn
        current_turn = "O" if current_turn == "X" else "X"

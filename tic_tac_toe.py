# game board

board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

# globals
current_player = "X"
X_points = 0
O_points = 0

def display_board():
    global board

    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def move(pos):
    global board

    board[pos-1] = current_player    
    return board

def switch_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

    return current_player

def row_winner():
    if board[0] == board[1] == board[2] == "X" or board[0] == board[1] == board[2] == "O":
        return True
    elif board[3] == board[4] == board[5] == "X" or board[3] == board[4] == board[5] == "O":
        return True
    elif board[6] == board[7] == board[8] == "X" or board[6] == board[7] == board[8] == "O":
        return True
    else:
        return False
 
def column_winner():
    if board[0] == board[3] == board[6] == "X" or board[0] == board[3] == board[6] == "O":
        return True
    elif board[1] == board[4] == board[7] == "X" or board[1] == board[4] == board[6] == "O":
        return True
    elif board[2] == board[5] == board[8] == "X" or board[2] == board[5] == board[8] == "O":
        return True
    else:
        return False
    

def diagonal_winner():
    if board[0] == board[4] == board[8] == "X" or board[0] == board[4] == board[8] == "O":
        return True
    elif board[2] == board[4] == board[6] == "X" or board[2] == board[4] == board[6] == "O":
        return True
    else:
        return False

def draw():
    global board

    key = True
    for index in board:
        if index == "-":
           key = False 

    if key:
        return True
    return False


def check_if_win():
    if row_winner() or column_winner() or diagonal_winner():
        return True
    return False

# main function
def main():
    global current_player, X_points, O_points, max_points

    # welcome
    print("Welcome to the game! ")
    prompt = input("Ready to start? (yes or no)").upper().split()

    if prompt == "no":
        quit()

    display_board()

    game_on = True

    while game_on:

        pos = int(input("Give a position from 1 to 9: "))
        while (pos < 1 or pos > 9) or (board[pos-1] == "X" or board[pos-1] == "O"):
            pos = int(input("Give the position again: "))

        move(pos)

        display_board()

        if row_winner() or column_winner() or diagonal_winner():
            game_on = False
            print(f"{current_player} won!")

            if current_player == "X":
                X_points += 1
                print(f"X has {X_points} points!")
            else:
                O_points += 1
                print(f"O has {O_points} points!")

        elif draw():
            game_on = False
            print("That's a draw!")

        switch_player()


max_points = int(input("Give the max player point rate: "))
while True:

    main()

    first_player = current_player
    if first_player == "X":
        first_player = "O"
    else:
        first_player = "X"

    if max_points == X_points:
        print("X is the big winner!")
        break
    elif max_points == O_points:
        print("O is the big winner!")
        break

    board = [
        "-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"
    ]
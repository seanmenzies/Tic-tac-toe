import sys
# create dictionary for board layout
board_dict = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ",
              "6": " ", "7": " ", "8": " ", "9": " "}


# print final board
def print_board():
    print(board_dict["1"] + "|" + board_dict["2"] + "|" + board_dict["3"])
    print("-+-+-")
    print(board_dict["4"] + "|" + board_dict["5"] + "|" + board_dict["6"])
    print("-+-+-")
    print(board_dict["7"] + "|" + board_dict["8"] + "|" + board_dict["9"])


# get player names
player1 = input("Player 1, enter your name: ")
player2 = input("player 2, enter your name: ")
players = {player1: "X", player2: "O"}


# set initial conditions
player = player1
symbol = "X"
# iterate tuns
for i in range(9):
    print(board_dict["1"] + "|" + board_dict["2"] + "|" + board_dict["3"] + "     1|2|3")
    print("-+-+-")
    print(board_dict["4"] + "|" + board_dict["5"] + "|" + board_dict["6"] + "     4|5|6")
    print("-+-+-")
    print(board_dict["7"] + "|" + board_dict["8"] + "|" + board_dict["9"] + "     7|8|9")
    move = input(f"It is {player}'s turn. Select a square: ")
    board_dict[move] = symbol
    # set win conditions
    if board_dict["1"] == board_dict["2"] == board_dict["3"] != " " or \
            board_dict["4"] == board_dict["5"] == board_dict["6"] != " " or \
            board_dict["7"] == board_dict["8"] == board_dict["9"] != " " or \
            board_dict["1"] == board_dict["4"] == board_dict["7"] != " " or \
            board_dict["2"] == board_dict["5"] == board_dict["8"] != " " or \
            board_dict["3"] == board_dict["6"] == board_dict["9"] != " " or \
            board_dict["1"] == board_dict["5"] == board_dict["9"] != " " or \
            board_dict["3"] == board_dict["5"] == board_dict["7"] != " ":
        print(f"{player} wins!")
        print_board()
        sys.exit()
    # change player and player's symbol
    if player == player1:
        player = player2
    else:
        player = player1
    if symbol == "X":
        symbol = "O"
    else:
        symbol = "X"


# draw condition
print("Sometimes in life, there are no winners, just two unlovable losers")
print_board()

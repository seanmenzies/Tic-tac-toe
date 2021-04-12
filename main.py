import sys
import time

while True:
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
    # create list to save all player moves
    moves_list = []
    game_status = "no"
    # iterate turns
    i = 0
    for i in range(9):
        print(board_dict["1"] + "|" + board_dict["2"] + "|" + board_dict["3"] + "     1|2|3")
        print("-+-+-")
        print(board_dict["4"] + "|" + board_dict["5"] + "|" + board_dict["6"] + "     4|5|6")
        print("-+-+-")
        print(board_dict["7"] + "|" + board_dict["8"] + "|" + board_dict["9"] + "     7|8|9")
        move = input(f"It is {player}'s turn. Select a square: ")
        # check for invalid input
        while move not in [*board_dict.keys()]:
            move = input("Select a square, you idiot!: ")
        # check for duplicate moves
        while move in moves_list:
            move = input("Square already used. Select a square: ")
        moves_list.insert(i, move)
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
            game_status = "win"
        else:
            game_status = "draw"
        # change player and player's symbol
        if player == player1:
            player = player2
        else:
            player = player1
        if symbol == "X":
            symbol = "O"
        else:
            symbol = "X"
        if game_status == "win":
            break
    # draw condition
    if game_status == "draw":
        print("Sometimes in life, there are no winners, just two unlovable losers")
        print_board()
    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.lower() == "n":
        break

print("Thanks for playing! See you next time!")
time.sleep(2)
sys.exit()

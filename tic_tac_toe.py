import itertools


def game_display(game_board):
    # Display game board
    print("   "+"  ".join([str(i) for i in range(len(game_board))]))
    for count,row in enumerate(game_board):
        print(count,row)


def win(game_board):
    # Check if there is a victor

    def all_same(li):
        # Check if a column, row or diagonal has the same value
        if li.count(li[0])==len(li) and li[0] != 0:
            return True
        else:
            return False

    # Horizontal victory check
    for row in game_board:
        if all_same(row):
            print(f"Horizontal Victory (-) for player {row[0]}.")
            return True

    # Vertical victory check
    for col in range(len(game_board)):
        check=[]
        for row in game_board:
            check.append(row[col])
        if all_same(check):
            print(f"Vertical Victory (|) for player {check[0]}.")
            return True
            
    # Diagonal victory check
    diags = []
    for ix in range(len(game_board)):
        diags.append(game_board[ix][ix])
    if all_same(diags):
        print(f"Diagonal victory (\\) for player {diags[0]}")
        return True
    del diags[:]
    for col,row in enumerate(reversed(range(len(game_board)))):
        diags.append(game_board[row][col])
    if all_same(diags):
        print(f"Diagonal victory (/) for player {diags[0]}")
        return True

    return False


def game_move(game_board, player_move, col, row):
    # Player move
    if game_board[row][col] != 0:
        print("This position is already occupied.")
        return game_board, False
    game_board[row][col] = player_move
    return game_board, True



play = True
while play:
    game_size = int(input("What size do you want your tic tac toe board to be? "))
    game_board = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    player_choice = itertools.cycle([1,2])
    game_display(game_board)
    while not game_won:
        current_player = next(player_choice)
        print(f"\nCurrent player is {current_player}.")
        col_choice = int(input("What column do you want to play? "))
        row_choice = int(input("What row do you want to play? "))
        game_board, _ = game_move(game_board, current_player, col_choice, row_choice)
        game_display(game_board)

        if win(game_board):
            game_won = True
            again = input("The game is over. Do you want to play again? (y/n) ")
            if again.lower() == 'y':
                print("Starting new game.")
            elif again.lower() == 'n':
                print("Closing game.")
                play = False
            else:
                print("Not a valid option. Closing game.")
                play = False


##board
##display board
##play game
##handle turn
##check win
   ##check rows
   ##check columns
   ##check diagonals
##check tie
##flip player

# ---------------------------- Global Variable ---------------------------------
#Game board
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_",]


# if the game is still going
game_still_going = True


#Who won? or tie?
winner = None


#Who's turn is it?
current_player = "X"


def display_board():
    print (board[0] + " | " + board[1] + " | " + board[2])
    print (board[3] + " | " + board[4] + " | " + board[5])
    print (board[6] + " | " + board[7] + " | " + board[8])


# Play a game of tic tac toe
def play_game():

    # display initial board
    display_board()

    while game_still_going:

        # Handle a single turn of an arbitary player
        handle_turn(current_player)

        
        # check if the game has ended
        check_if_gameover()

        # Flip to the other player
        flip_player()

    #The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# Handle a single turn of an arbitary player   
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
  
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Try again. Choose a position from 1-9: ")
            
        position = int(position) - 1

        if board[position] == "_":
            valid = True
        else:
            print("You can't go there. Try again.")

    board[position] = player
    display_board()

    


def check_if_gameover():
    check_for_winner()
    check_for_tie()


def check_for_winner():

    # set up global variable
    global winner
    
    # check rows
    row_winner = check_rows()
    
    # check columns
    column_winner = check_columns()
    
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
        
    elif column_winner:
        winner = column_winner
        
    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None
    return

def check_rows():

    #set up global variable
    global game_still_going
    
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"

    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return the winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    #set up global variable
    global game_still_going
    
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"

    # If any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False

    # Return the winner X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return
    

def check_diagonals():
    #set up global variable
    global game_still_going
    
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[6] == board[4] == board[2] != "_"

    # If any diagonal does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # Return the winner X or O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return
    

def check_for_tie():
    global game_still_going
    
    if "_" not in board:
        game_still_going = False
    return


def flip_player():

    global current_player
    
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()


#----Game_Board-----
board=[" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "]

#---Global_variable---
game_is_still_going=True

#who_won_???
winner=None

#who's_turn_is_this
current_player= " X "

def display_board():
    print("|" +board[0]+"|" +board[1]+"|" +board[2]+"|" )
    print("|" +board[3]+"|" +board[4]+"|" +board[5]+"|")
    print("|" +board[6]+"|" +board[7]+"|" +board[8]+"|")

def play_game():
    global current_player
    #displaying initial board
    display_board()
    while game_is_still_going:
        
        handle_turn(current_player)

        check_if_game_over()
        
        flip_player()

     
    #the game has ended
    if winner ==" X " or winner==" O ":
        print(winner+" won. ")
    elif winner==None:
        print("Tied")

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner
    
    #check rows
    row_winner=check_rows()
    #check cocloumns
    coloumn_winner=check_coloumns()
    #check diagonals
    diagonl_winner=check_diagonals()
    if row_winner:
        winner=row_winner
    elif coloumn_winner:
        winner=coloumn_winner
    elif diagonl_winner:
        winner=diagonl_winner
    return winner

def check_rows():
    global game_is_still_going

    row1= board[0]==board[1]==board[2] !=" _ "
    row2= board[3]==board[4]==board[5] !=" _ "
    row3= board[6]==board[7]==board[8] !=" _ "
    
    if row1 or row2 or row3:
        game_is_still_going=False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]

def check_coloumns():
    global game_is_still_going

    coloumn1= board[0]==board[3]==board[6] !=" _ "
    coloumn2= board[1]==board[4]==board[7] !=" _ "
    coloumn3= board[2]==board[5]==board[8] !=" _ "
    
    if coloumn1 or coloumn2 or coloumn3:
        game_is_still_going=False
    if coloumn1:
        return board[0]
    if coloumn2:
        return board[3]
    if coloumn3:
        return board[6]

def check_diagonals():
    global game_is_still_going

    diagonal1= board[0]==board[4]==board[8] !=" _ "
    diagonal2= board[2]==board[4]==board[6] !=" _ "
    
    if diagonal1 or diagonal2:
        game_is_still_going=False
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[3]

def check_if_tie():
    global game_is_still_going
    if " _ " not in board:
        game_is_still_going=False

def flip_player():
    global current_player
    if current_player==" X ":
        current_player=" O "
    elif current_player==" O ":
        current_player=" X "
    return current_player

def handle_turn(current_player):
    print(current_player+"s turn.")
    position=int(input("Choose a position from 1-9 :    "))
    valid=False
    while not valid:
        while position not in [1,2,3,4,5,6,7,8,9]:
            position=int(input("Invalid Input!!!.  Choose a position from 1-9 :    "))
        index_position=position-1
        if board[position]==" _ ":
            valid=True
        else:
            print("You cant go there. Go again!!")
    board[index_position]=current_player
    display_board()

play_game()
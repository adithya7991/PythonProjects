new_game = True




def disp(board):
    for x in board:
        print(("{} | {} | {}").format(x[0],x[1],x[2]))

def validate_move(player, move):
    temp = eval(move)    
    if board[temp[0]][temp[1]] == 0:
        if player == "p1":
            board[temp[0]][temp[1]] = 1
        else:
            board[temp[0]][temp[1]] = 2
            disp(board)
        return True
    return False

def check_win(player):
    
    for row in board:
        if row.count(1)==3 or row.count(2)==3:
            print(("{} won the match").format(player))
            return True

    for coln in [0,1,2]:
        temp = []
        for row in [0,1,2]:
            temp.append(board[row][coln])
        if temp.count(1)==3 or temp.count(2)==3:
            print(("{} won the match").format(player))
            return True 
                

    return False

def core_logic(player):
    global new_game    
    pm = input(player + " move...: ")
    if validate_move(player, pm):
        print("Its a Valid move... ")
        print("Current Board...")
        disp(board)
        if check_win(player):            
            new_game = False
            return False

    else:
        print("Invalid move... ")
        if input("Do u want to start new game..(y/n): ") == "y":
            return False
        else:            
            new_game = False
            return False
    return True
            

while(new_game):

    board = [[0,0,0],[0,0,0],[0,0,0]]
    player_changer = 1       
    player_1 = input("Name of player 1: ")
    player_2 = input("Name of player 2: ")
    print("Current Board...")
    disp(board)
    

    while(True):        
        if player_changer%2 !=0:
            if core_logic("p1") == False:
                break
            player_changer += 1
        elif player_changer%2 ==0:
            if core_logic("p2") == False:
                break
            player_changer += 1

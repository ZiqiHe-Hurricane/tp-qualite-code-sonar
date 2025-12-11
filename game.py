def board_init() -> list[list[str]]:
    board = [[" "for _ in range(3)] for _ in range(3)]
    return board

def move(player:str, position:tuple,board):
    row = position[0]
    col = position[1]
    if (row>2 or row<0) or (col>2 or col<0):
        step = input("Out of the board, please entre another position . (row col)")
        row,col = map(int,step.split())
        return move(player=player,position=(row,col),board=board)
    elif board[row][col] == " ":
        board[row][col] = player
    else:
        step = input("This position is already taken, please choose another position . (row col)")
        row,col = map(int,step.split())
        return move(player=player,position=(row,col),board=board)
    print_board(board)

def print_board(board):
    for row in board:
        print("|".join(row))
        print("*" * 5)

def checkwinners(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] !=" " :
            print(f"Game Over! Player {board[row][0]} won the game!")
            print_board(board)
            return True 
    for col in range(3):
        if board[0][col] ==  board [1][col] == board[2][col] !=" " :
            print(f"Game Over! Player {board[0][col]} won the game!")
            print_board(board)
            return True 
    if board[0][0] == board[1][1] == board[2][2] != " " :
        print(f"Game Over! Player {board[0][0]} won the game!")
        print_board(board)
        return True

    if board[0][2] == board[1][1] == board[2][0] != " " :
        print(f"Game Over! Player {board[2][0]} won the game!")
        print_board(board)
        return True 
def main():
    start = True
    print("Please enter player: ")
    player1 = input("Player1 :")
    player2 = input("Player2 :")
    while start :
        conf=input("Confirm game start ? Yes/No ")
        if conf == "Yes" :
            print("The game starts !")
        else :
            print("Exit !")
            break
        board = board_init()
        finish = False
        for i in range(9):
            if i%2 ==0:
                step=input(f"Please {player1} make your move . (row col)")
                row,col = map(int,step.split())
                move(player=player1,position=(row,col),board=board)
                if checkwinners(board=board):
                    finish=True    
                    break
            
            else:
                step=input(f"Please {player2} make your move . (row col)")
                row,col = map(int,step.split())
                move(player=player2,position=(row,col),board=board)
                if checkwinners(board=board):
                    finish=True
                    break
        if finish == False:
            print("Game failed ! No winners !")
        cont = input("Start next game ? Yes/No ")
        if cont == "Yes":
            start = True
        else : 
            start =False

if __name__ == "__main__":
    main()

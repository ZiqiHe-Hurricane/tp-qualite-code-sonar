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
    display_board = []
    for r in range(3):
        row_display = []
        for c in range(3):
            if board[r][c] == " ":
                row_display.append(f"{r},{c}")
            else:
                row_display.append(str(board[r][c]))
        display_board.append(row_display)

    cell_width = max(len(str(cell)) for row in board for cell in row)
    if cell_width <1 :
        cell_width = 1
    for row_display in display_board:
        formatted_cells = [str(cell).center(cell_width) for cell in row_display]
        line = "|".join(formatted_cells)
        print(line)
        print("*" * len(line))

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
        if conf in ("Yes", "yes", "YES") :
            print("The game starts !")
        else :
            print("Exit !")
            break
        board = board_init()
        print_board(board=board)
        finish = False
        for i in range(9):
            if i%2 ==0:
                step=input(f"Please {player1} make your move. (row col)")
                if step == "finish" :
                    finish=False
                    break
                else:
                    clean = step.replace("(","").replace(")","").replace(","," ")
                    row,col = map(int,clean.split())
                    move(player=player1,position=(row,col),board=board)
                    if checkwinners(board=board):
                        finish=True    
                        break
            
            else:
                step=input(f"Please {player2} make your move. (row col)")
                if step == "finish" :
                    finish=False
                    break
                else:
                    clean = step.replace("(","").replace(")","").replace(","," ")
                    row,col = map(int,clean.split())
                    move(player=player2,position=(row,col),board=board)
                    if checkwinners(board=board):
                        finish=True
                        break
        if finish == False:
            print("Game failed ! No winners !")
        conf = input("Start next game ? Yes/No ")
        if conf in ("Yes", "yes", "YES"):
            start = True
        else : 
            start =False

if __name__ == "__main__":
    main()

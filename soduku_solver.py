board=[['.','9','.','5','.','8','.','.','4'],['4','.','8','.','.','9','.','.','2'],['.','.','5','.','3','.','1','8','.'],['.','.','4','1','.','.','6','.','.'],['9','6','1','.','.','3','4','.','7'],['3','.','.','2','.','.','9','.','8'],['8','.','.','.','.','.','.','.','5'],['5','.','9','.','2','6','.','.','.'],['.','.','.','9','.','5','.','.','.']]
def display_board(bo):
    for i in range(len(bo)):
        if i%3==0:
            print("_  _  _  _  _  _  _  _  _  _ _")
        for j in range(len(bo[0])):
            if j%3==0:
                print("|",end="")
            print(" "+bo[i][j]+" ",end="")
        print("|")
    print("_  _  _  _  _  _  _  _  _  _ _")
display_board(board)

def soduku_solver(array):
    if not find_empty(array):
        return True
    else:
        row,col = find_empty(array)


    for num in range(1,10):
        if is_valid(str(num),row,col,array):
            array[row][col]=str(num)

            if soduku_solver(array):
                return True

            array[row][col] = '.'

    return False



def is_valid(num,row,col,board):
    for i in board[row]:
        if i==num:
            return False
    for i in range(len(board)):
        if num==board[i][col]:
            return False
    for i in range(3*(row//3),3*(row//3)+3):
        for j in range(3*(col//3),3*(col//3)+3):
            if board[i][j]==num:
                return False
    return(True)

def find_empty(board):
    for i in range (len(board)):
        for j in range(len(board[0])):
            if board[i][j]=='.':
                return i,j
    return False



print("Below is the solved board:")
soduku_solver(board)
display_board(board)


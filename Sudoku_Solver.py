#map 1
'''board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]'''

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def solve():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for num in range(1,10):
                    if valid(y,x,num):
                        board[y][x] = num
                        solve()
                        board[y][x] = 0
                return
    print("\n the solution is: ")
    print("___________________________")
    print_board(board)
    input("\n Try more solutions?")

def valid(y, x, num):
    global board
    # col
    for i in range(0, 9):
        if board[y][i] == num:
            return False
    # row
    for i in range(0, 9):
        if board[i][x] == num:
            return False
    # box
    box_x = (x//3)*3
    box_y = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[box_y + i][box_x + j] == num:
                return False
    return True

def print_board(map):
    for i in range(len(map)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(map[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(map[i][j])
            else:
                print(str(map[i][j]) + " ", end="")

print_board(board)
print("___________________________")
solve()



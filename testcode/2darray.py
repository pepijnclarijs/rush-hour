# 1D array
board_size = 6
row = [0 for i in range(board_size)]
print(row)

# 2D array
rows, columns = (board_size, board_size)
board_array = [[ 0 for i in range(columns)] for j in range(rows)]
print(board_array)

# demonstrate the 2d-array as a board/grid
board_array = [[ 0 for i in range(columns)] for j in range(rows)]
board_array[0][0] = 1
for row in board_array:
    print(row)


#board_array == gamestate

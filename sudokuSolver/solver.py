grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 7, 2, 0, 0, 0],
    [0, 0, 0, 1, 5, 9, 0, 0, 0],
    [0, 0, 0, 8, 3, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def solve_grid(grd):
    find = find_zero(grd)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid_grid(grd, i, (row, col)):
            grd[row][col] = i

            if solve_grid(grd):
                return True

            grd[row][col] = 0

    return False


def valid_grid(grd, num, pos):
    for i in range(len(grd[0])):
        if grd[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(grd)):
        if grd[i][pos[1]] == num and pos[0] != i:
            return False

    square_x = pos[1] // 3
    square_y = pos[0] // 3

    for i in range(square_y * 3, square_y * 3 + 3):
        for j in range(square_x * 3, square_x * 3 + 3):
            if grd[i][j] == num and (i, j) != pos:
                return False

    return True


def print_grid(grd):
    for i in range(len(grd)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(grd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grd[i][j])
            else:
                print(str(grd[i][j]) + " ", end="")


def find_zero(grd):
    for i in range(len(grd)):
        for j in range(len(grd[0])):
            if grd[i][j] == 0:
                return i, j  # row, column

    return None


solve_grid(grid)
print_grid(grid)

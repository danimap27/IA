
def rows(square, magic_num):
    n = len(square)
    for i in range(n):
        sum_row = 0
        for j in range(n):
            sum_row += square[i][j]
        if sum_row != magic_num:
            return False
    return True

def columns(square, magic_num):
    n = len(square)
    for i in range(n):
        sum_col = 0
        for j in range(n):
            sum_col += square[j][i]
        if sum_col != magic_num:
            return False
    return True

def diagonals(square, magic_num):
    n = len(square)
    #left_to_right
    sum_diag = 0
    for i in range(n):
        sum_diag += square[i][i]
    if sum_diag != magic_num:
        return False
    #right to left
    sum_diag = 0
    for i in range(n):
        sum_diag += square[i][-(i+1)]
    return sum_diag == magic_num


# this is our main function
def magic_square(square):
    # find magic number
    magic_constant = 0
    for n in square[0]:
        magic_constant += n
    return ( rows(square, magic_constant) and columns(square, magic_constant) and diagonals(square, magic_constant) )
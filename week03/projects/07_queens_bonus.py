count = 0

def count_solution():
    global count
    count += 1
    return count

def show_possible(board, queen):
    count_solution()


def check_queen(board, row, col, queen):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, queen, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def find_all_possi(board, col, queen):
    if col == queen:
        show_possible(board, queen)
        return True

    res = False
    for i in range(queen):
        if check_queen(board, i, col, queen):
            board[i][col] = 1

            res = find_all_possi(board, col + 1, queen) or res

            board[i][col] = 0

    return False


def queen_bonus(queen):
    count = 0
    board = [[0 for x in range(queen)] for y in range(queen)]

    if find_all_possi(board, 0, queen) == False:
        return count_solution() -1

    return count


# print(queen_bonus(12))
count = 0

def count_solution():
    global count
    count += 1
    return count

def show_possible(board):
    count_solution()


def check_queen(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def find_all_possi(board, col):
    if col == 8:
        show_possible(board)
        return True

    res = False
    for i in range(8):
        if check_queen(board, i, col):
            board[i][col] = 1

            res = find_all_possi(board, col + 1) or res

            board[i][col] = 0

    return False


def queens():
    count = 0
    board = [[0 for x in range(8)] for y in range(8)]

    if find_all_possi(board, 0) == False:
        return count_solution() -1

    return count


# print(queens())

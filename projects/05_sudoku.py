def sudoku(board):
    check_row = 0
    for row in board:
        check_number = 0
        for number in row:
            check_number += 1
            if number < 1 or number > 9:                #checking for
                return "Invalid Format"
        if check_number != 9:
            return "Invalid Format"
        check_row += 1
    if check_row != 9:
        return "Invalid Format"
    else:
        for row in board:
            for number in row:
                check = row.count(number)                   #checking for duplicate numbers in row
                if check > 1:
                    return "Not Finished"
        row, column = 9, 9
        reversed_sudoku = [[0 for x in range(row)] for y in range(column)]
        for column_number in range(9):                             #assigning column numbers into new 2d array
            for row_number in range(9):
                reversed_sudoku[column_number][row_number] = board[row_number][column_number]
        for row in reversed_sudoku:                         #checking for duplicate numbers in row
            for number in row:
                check = row.count(number)                   #checking for duplicate numbers in row
                if check > 1:
                    return "Not Finished"
        row_count, column_count, first, second = 0, 0, 0, 0
        sum_in_region = 0
        while first <= 6 and second <=9:                                               #start checking for the region 3 x 3
            second += 3                                                                #second is used for counting the maximun range for the region checking
            row_count = 0                                                               #row count neeeds to be restarted because it can't exceed number 8
            for row in board:
                for column_count in range(first, second):                                   #column need to stay in range be tween 3 numbers (first - second = 3)
                    sum_in_region += board[row_count][column_count]
                if (row_count+1) % 3 == 0:                                         #when row reaches the value of 3, it finishes one 3x3 region hence i sum up all the value in that region which supposedly equals 45
                    if sum_in_region == 45:
                        sum_in_region = 0
                    else:
                        return "Not Finished"
                row_count += 1
            first += 3                                                                  #first is used for counting the minimum range for the region checking
        return "Finished"

# return "Finished"as expected
# print(sudoku([ [5, 3, 4, 6, 7, 8, 9, 1, 2],
# [6, 7, 2, 1, 9, 5, 3, 4, 8],
# [1, 9, 8, 3, 4, 2, 5, 6, 7],
# [8, 5, 9, 7, 6, 1, 4, 2, 3],
# [4, 2, 6, 8, 5, 3, 7, 9, 1],
# [7, 1, 3, 9, 2, 4, 8, 5, 6],
# [9, 6, 1, 5, 3, 7, 2, 8, 4],
# [2, 8, 7, 4, 1, 9, 6, 3, 5],
# [3, 4, 5, 2, 8, 6, 1, 7, 9]]))


# return "Not Finished" as expected
# print(sudoku([ [1, 1, 3, 5, 7, 9, 4, 6, 8],
# [4, 9, 1, 2, 6, 1, 3, 7, 5],
# [7, 5, 6, 1, 8, 4, 2, 1, 9],
# [6, 4, 4, 1, 5, 8, 7, 9, 2],
# [5, 2, 1, 7, 1, 1, 1, 1, 1],
# [9, 8, 7, 4, 2, 6, 5, 3, 1],
# [2, 1, 4, 9, 3, 5, 2, 2, 7],
# [3, 6, 5, 8, 1, 7, 9, 2, 4],
# [8, 7, 9, 6, 4, 2, 1, 5, 3]]))


# return "Invalid Format" as expected
# print(sudoku([ [0, 12, 3, 5, 7, 9, 4, 6, 8],
# [4, 9, 1, 2, 3, 7, 5],
# [7, 5, 6, 1, 8, 4, 2, 1, 9],
# [6, 4, 4, 1, 5, 8, 7, 9, 2],
# [5, 2, 1, 7, 1, 1, 1, 1, 1],
# [9, 8, 7, 4, 2, 6, 5, 3, 1],
# [2, 1, 4, 9, 3, 5, 2, 2, 7],
# [3, 6, 5, 8, 1, 7, 9, 2, 4],
# [8, 7, 9, 6, 4, 2, 1, 5, 3]]))


# return "Finished" as expected
# print(sudoku([ [9, 5, 2, 6, 7, 4, 1, 3, 8],
# [6, 8, 1, 9, 3, 2, 4, 5, 7],
# [3, 7, 4, 5, 1, 8, 2, 9, 6],
# [1, 9, 3, 8, 2, 6, 7, 4, 5],
# [2, 4, 5, 7, 9, 3, 6, 8, 1],
# [8, 6, 7, 4, 5, 1, 3, 2, 9],
# [5, 2, 6, 3, 8, 7, 9, 1, 4],
# [4, 1, 8, 2, 6, 9, 5, 7, 3],
# [7, 3, 9, 1, 4, 5, 8, 6, 2]]))


#return "Not Finished" as expected
# print(sudoku([[1, 3, 4, 6, 7, 8, 9, 5, 2],
#         [6, 7, 2, 1, 9, 5, 3, 4, 8],
#         [1, 9, 8, 3, 4, 2, 5, 6, 7],
#         [8, 5, 9, 7, 6, 1, 4, 2, 3],
#         [4, 2, 6, 8, 5, 3, 7, 9, 1],
#         [7, 1, 3, 9, 2, 4, 8, 5, 6],
#         [9, 6, 1, 5, 3, 7, 2, 8, 4],
#         [2, 8, 7, 4, 1, 9, 6, 3, 5],
#         [3, 4, 5, 2, 8, 6, 1, 7, 9]]))
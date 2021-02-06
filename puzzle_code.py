'''
Module for analising the status of a board
'''

def check_horizontal(board):
    '''
    Check if every row doesn't have any duplicates and numbers not in range (1, 9)
    >>> check_horizontal(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
        "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    '''

    for row in board:
        row = row.replace('*', '')
        row = row.replace(' ', '')
        if len(set(row))!= len(row):
            return False
        for elem in row:
            if elem > '9' or elem < '1':
                return False
    return True

# print(check_horizontal([
#  "**** ****",
#  "***1 ****",
#  "**  3****",
#  "* 4 1****",
#  "     9 5 ",
#  " 6  83  *",
#  "3   1  **",
#  "  8  2***",
#  "  2  ****"
# ]))
def check_vertical(board):
    '''
    Check if every column doesn't have any duplicates and numbers not in range (1, 9)
    >>> check_horizontal(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
        "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    '''
    columns = []
    for i in range(len(board)):
        column = ''
        for row in board:
            column += row[i]
        columns.append(column)

    return check_horizontal(columns)


def check_color(board):
    '''
    Check if every color doesn't have any duplicates and numbers not in range (1, 9)
    >>> check_horizontal(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
        "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    '''
    colors = []
    colorss = []
    columns = []
    for i in range(len(board)):
        column = ''
        for row in board:
            column += row[i]
        columns.append(column)

    for i in range(4, 9):
        board[i] = board[i].replace('*', '')
        color = board[i][-5:]
        colors.append(color)


    for i in range(5):
        columns[i] = columns[i].replace('*', '')
        color = columns[i][:4]
        colorss.append(color)
    colorss.reverse()
    for i in range(len(colors)):
        colors[i] = colors[i]+colorss[i]

    return check_horizontal(colors)






def validate_board(board):
    """
    Main function to check the status of the board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    >>> check_horizontal(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
        "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    """
    booleans = []
    booleans.append(check_horizontal(board))
    booleans.append(check_vertical(board))
    booleans.append(check_color(board))

    return all(booleans)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  2  ****"
]

def check_horizontal(board):

    for row in board:
        row = row.replace('*', '')
        row = row.replace(' ', '')
        if len(set(row))!= len(row):
            return False
        for el in row:
            if el > '9' or el < '1':
                return False
    
    return True


def check_vertical(board):
    columns = []
    for i in range(len(board)):
        column = ''
        for row in board:
            column += row[i]
        columns.append(column)
    
    return check_horizontal(columns)

    
def check_color(board):
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
    """
    booleans = []
    booleans.append(check_horizontal(board))
    booleans.append(check_vertical(board))
    booleans.append(check_color(board))
    
    return all(booleans)

print(validate_board(board))
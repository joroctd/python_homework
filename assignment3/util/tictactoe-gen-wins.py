def gen_winning_lines(board_size=3):
    winning_lines = []

    for i in range(board_size):
        row = [(i, j) for j in range(board_size)] # --
        winning_lines.append(row)
    
    for j in range(board_size):
        column = [(i, j) for i in range(board_size)] # |
        winning_lines.append(column)
    
    diag_down = [(i, i) for i in range(board_size)] # \
    diag_up = [(i, board_size - 1 - i) for i in range(board_size)] # /
    winning_lines.append(diag_down)
    winning_lines.append(diag_up)

    return winning_lines

print(gen_winning_lines())

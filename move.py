def move_board(board, height, width, direction):
    if direction == 'left':
        for row in board:
            while 0 in row:
                row.remove(0)
            while len(row) != width:
                row.append(0)
        for y in range(height):
            for x in range(width - 1):
                if board[y][x] == board[y][x + 1] and board[y][x] != 0:
                    board[y][x] *= 2
                    board[y].pop(x + 1)
                    board[y].append(0)

    elif direction == 'right':
        for row in board:
            while 0 in row:
                row.remove(0)
            while len(row) != width:
                row.insert(0, 0)
        for y in range(height):
            for x in range(width - 1, 0, -1):
                if board[y][x] == board[y][x - 1] and board[y][x] != 0:
                    board[y][x] *= 2
                    board[y].pop(x - 1)
                    board[y].insert(0, 0)

    if direction == 'up':
        for x in range(width):
            column = [board[y][x] for y in range(height)]
            while 0 in column:
                column.remove(0)
            while len(column) != height:
                column.append(0)
            for y in range(height - 1):
                if column[y] == column[y + 1] and column[y] != 0:
                    column[y] *= 2
                    column.pop(y + 1)
                    column.append(0)
            for y in range(height):
                board[y][x] = column[y]

    elif direction == 'down':
        for x in range(width):
            column = [board[y][x] for y in range(height)]
            while 0 in column:
                column.remove(0)
            while len(column) != height:
                column.insert(0, 0)
            for y in range(height - 1, 0, -1):
                if column[y] == column[y - 1] and column[y] != 0:
                    column[y] *= 2
                    column.pop(y - 1)
                    column.insert(0, 0)
            for y in range(height):
                board[y][x] = column[y]

    return board
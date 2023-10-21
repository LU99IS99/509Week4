def flood_fill(input_board, old, new, x, y):
    # If the coordinate is out of bounds or the value at (x, y) is not the old value, return.
    if x < 0 or x >= len(input_board[0]) or y < 0 or y >= len(input_board) or input_board[y][x] != old:
        return input_board

    # Convert the row string to a list for mutability.
    row = list(input_board[y])
    # Replace the old value with the new value.
    row[x] = new
    # Convert the row list back to a string and update the board.
    input_board[y] = "".join(row)

    # Recursive calls for north, south, east, and west.
    flood_fill(input_board, old, new, x+1, y)
    flood_fill(input_board, old, new, x-1, y)
    flood_fill(input_board, old, new, x, y+1)
    flood_fill(input_board, old, new, x, y-1)

    return input_board

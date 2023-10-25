def flood_fill(input_board, old, new, x, y):
    # Base cases to stop recursion
    if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board[0]):
        return input_board
    elif input_board[x][y] != old:
        return input_board

    # Update the current cell with the new value
    row = list(input_board[x])
    row[y] = new
    input_board[x] = ''.join(row)

    # Recursively check and fill neighboring cells
    flood_fill(input_board, old, new, x + 1, y)
    flood_fill(input_board, old, new, x - 1, y)
    flood_fill(input_board, old, new, x, y + 1)
    flood_fill(input_board, old, new, x, y - 1)

    return input_board

# Test cases
board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

newboard = [
    "......................",
    "......##########......",
    "...####........##.....",
    "....#............#....",
    "....###..........###..",
    "......###..........#..",
    "........###......##...",
    "..........#######.....",
]
modified_board = flood_fill(input_board=board.copy(), old=".", new="~", x=5, y=12)
modified_newboard = flood_fill(input_board=newboard.copy(), old=".", new="~", x=3, y=8)

for a in modified_newboard:
    print(a)

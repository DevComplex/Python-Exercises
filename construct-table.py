VERY_SMALL_INTEGER = -(2 ** 32)

def get_columns_max_word_sizes(grid, rows, cols):
    columns_max_word_sizes = []

    for i in range(rows):
        max_word_size = VERY_SMALL_INTEGER

        for j in range(cols):
            word_size = len(grid[i][j])

            if word_size > max_word_size:
                max_word_size = word_size

        columns_max_word_sizes.append(max_word_size)

    return columns_max_word_sizes

def get_column_widths(grid, rows, cols):
    columns_max_word_sizes = get_columns_max_word_sizes(grid, rows, cols)
    return [x + 2 for x in columns_max_word_sizes]

def get_left_and_right_spaces(column_widths, col, word_len):
    space = column_widths[col] - word_len
    space_on_each_side = space // 2

    left_space = space_on_each_side
    right_space = space_on_each_side

    if space % 2 == 1:
        left_space += 1

    return (left_space, right_space)


def get_row_str(grid, col, column_widths):
    rows = len(grid)
    row_str = ""

    for row in range(0, rows):
            column_str = ""
            word = grid[row][col]

            left_space, right_space = get_left_and_right_spaces(column_widths, row, len(word))

            # always add a left wall
            column_str += "|"

            column_str += (" " * left_space) + word + (" " * right_space)

            # only add a right wall if last column
            if row == rows - 1:
                column_str += "|"

            row_str += column_str

    return row_str

def construct_table(grid):
    rows = len(grid)
    cols = len(grid[0])

    column_widths = get_column_widths(grid, rows, cols)
    table_width = sum(column_widths) + len(column_widths) + 1 

    table = ["-" * table_width]

    for col in range(0, cols):
        table.append(get_row_str(grid, col, column_widths))
        table.append("-" * table_width)

    return "\n".join(table)


def main():
    grid = [
        ["space", "lol", "brah"],
        ["space", "lol", "C# is awesome"],
        ["space", "lol", "brah"],
        ["lmaofsdfs", "lol", "brah"],
        ["space", "lol", "brah"],
    ]

    table = construct_table(grid)

    print(table)

if __name__ == "__main__":
    main()

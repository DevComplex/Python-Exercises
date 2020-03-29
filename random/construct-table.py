VERY_SMALL_INTEGER = -(2 ** 32)

def get_max_word_size_of_each_col(grid, rows, cols):
    cols_max_word_sizes = []

    for i in range(rows):
        max_word_size = VERY_SMALL_INTEGER

        for j in range(cols):
            word_size = len(grid[i][j])

            if word_size > max_word_size:
                max_word_size = word_size

        cols_max_word_sizes.append(max_word_size)

    return cols_max_word_sizes

def get_cols_widths(grid, rows, cols):
    cols_max_word_sizes = get_max_word_size_of_each_col(grid, rows, cols)
    return [x + 2 for x in cols_max_word_sizes]

def get_left_and_right_spaces_of_word(cols_widths, col, word_len):
    space = cols_widths[col] - word_len
    left_space = right_space = space // 2

    if space % 2 == 1:
        left_space += 1

    return (left_space, right_space)

def get_table_row_str(grid, col, cols_widths):
    rows = len(grid)
    table_row_str = ""

    for row in range(0, rows):
            column_str = ""
            word = grid[row][col]

            left_space, right_space = get_left_and_right_spaces_of_word(cols_widths, row, len(word))

            # always add a left wall
            column_str += "|"

            column_str += (" " * left_space) + word + (" " * right_space)

            # only add a right wall if last column
            if row == rows - 1:
                column_str += "|"

            table_row_str += column_str

    return table_row_str

def construct_table(grid):
    rows = len(grid)
    cols = len(grid[0])

    cols_widths = get_cols_widths(grid, rows, cols)
    table_width = sum(cols_widths) + len(cols_widths) + 1

    table = ["-" * table_width]

    for col in range(0, cols):
        table.append(get_table_row_str(grid, col, cols_widths))
        table.append("-" * table_width)

    return "\n".join(table)

def main():
    grid = [
        ["apple", "pineapple", "orange"],
        ["pear", "grape", "plum"],
        ["nectarine", "tangerine", "kiwi"],
        ["lime", "lemon", "celery"],
        ["spinach", "tomato", "grapefruit"],
    ]

    table = construct_table(grid)

    print(table)

if __name__ == "__main__":
    main()

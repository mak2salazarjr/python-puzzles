"""
You are given a matrix of NxN (4≤N≤10).
You should check if there is a sequence of 4 or more matching digits. 
The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).
"""


def checkio(matrix):
    repeat = 4
    repeat_range = len(matrix) - repeat + 1

    for row, offset in [(row, offset)
                        for row in range(len(matrix))
                        for offset in range(repeat_range)]:
        # check row
        if len(set(matrix[row][offset:offset + repeat])) == 1:
            return True
        if row < repeat_range:
            # check '\' diagonal
            if len(set([matrix[row + i][offset + i] for i in range(repeat)])) == 1:
                return True
            # check '/' diagonal
            if len(set([matrix[row + i][offset + repeat - 1 - i] for i in range(repeat)])) == 1:
                return True
            # check columns
            for column in range(repeat):
                if len(set([matrix[row + i][offset+column] for i in range(repeat)])) == 1:
                    return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) is True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) is False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) is True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) is True, "Diagonal"
    assert checkio([
        [2, 6, 2, 2, 7, 6, 5],
        [3, 4, 8, 7, 7, 3, 6],
        [6, 7, 3, 1, 2, 4, 1],
        [2, 5, 7, 6, 3, 2, 2],
        [3, 4, 3, 2, 7, 5, 6],
        [8, 4, 6, 5, 2, 9, 7],
        [5, 8, 3, 1, 3, 7, 8]
    ]) is False, "Nothing here"
    assert checkio([
        [2, 6, 2, 3, 5, 2, 4, 8, 7],
        [5, 7, 8, 5, 9, 5, 7, 3, 4],
        [6, 4, 1, 2, 1, 6, 5, 8, 5],
        [9, 3, 1, 3, 5, 4, 6, 4, 8],
        [9, 6, 6, 8, 1, 9, 1, 2, 1],
        [5, 5, 5, 8, 6, 5, 3, 2, 5],
        [7, 5, 2, 9, 2, 9, 8, 2, 5],
        [5, 8, 1, 9, 1, 2, 6, 2, 2],
        [7, 5, 3, 6, 1, 6, 9, 5, 9]
    ]) is True, "Vertical"

# https://py.checkio.org/mission/skew-symmetric-matrix/
# Input: A square matrix as a list of lists with integers.
# Output: If the matrix is skew-symmetric or not as a boolean.
# Precondition: 0 < N < 5


def checkio(matrix):
    dimension = len(matrix)
    for row in range(dimension):
        for column in range(dimension):
            if matrix[row][column] != -matrix[column][row]:
                return False
    return True


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) is True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) is False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) is False, "3rd example"

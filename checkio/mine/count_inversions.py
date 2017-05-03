# https://py.checkio.org/mission/count-inversions/
# Output: The inversion number as an integer.
# Precondition: 2 < len(sequence) < 200
# len(sequence) == len(set(sequence))
# all(-100 < x < 100 for x in sequence)
from random import shuffle


def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    inversions = 0
    for left in sequence[:-1]:
        for right in sequence[sequence.index(left) + 1:]:
            if left > right:
                inversions += 1
    return inversions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    sequence_200 = [n for n in range(-100, 100)]
    shuffle(sequence_200)
    count_inversion(sequence_200)

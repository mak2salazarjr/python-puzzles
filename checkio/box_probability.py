"""
Input: The start sequence of the pearls as a string and the step number as an integer.
Output: The probability for a white pearl as a float.
Precondition: 0 < N ≤ 20
0 < |pearls| ≤ 20
"""


def checkio(marbles, step):
    def compute_p_white(n_white, n_black, step):
        pearls = n_white + n_black
        if step == 1:
            return n_white / pearls
        else:
            p_white_1 = p_white_2 = 0.0
            if n_white:
                p_white_1 = (n_white / pearls) * compute_p_white(n_white - 1, n_black + 1, step - 1)
            if n_black:
                p_white_2 = (n_black / pearls) * compute_p_white(n_white + 1, n_black - 1, step - 1)
            p_white = p_white_1 + p_white_2
            return p_white

    if step == 0:
        return 0.0
    white = sum([1 if marble == 'w' else 0 for marble in marbles])
    black = len(marbles) - white
    result = float('{0:.2f}'.format(compute_p_white(white, black, step)))
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"

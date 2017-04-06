"""
http://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number

Given a number n, write an efficient function to print all prime factors of n. 
For example, if the input number is 12, then output should be “2 2 3”. And if the 
input number is 315, then output should be “3 3 5 7”.
"""


def get_factors(number):
    """
    Returns a list of prime factors of 'number'
    :param number: the number to derive factors of
    :return: list of factors
    """
    result = []
    while number % 2 == 0:
        result.append(2)
        number //= 2

    for divisor in range(3, int(number ** 0.5), 2):
        while number % divisor == 0:
            result.append(divisor)
            number //= divisor

    if number != 1:
        result.append(number)

    return result


tests = (
    (1, []),
    (4, [2, 2]),
    (5, [5]),
    (24, [2, 2, 2, 3]),
    (12414, [2, 3, 2069]),
    (10987234987234, None),
)

if __name__ == '__main__':
    for test in tests:
        print(f'{test[0]} -> {get_factors(test[0])}')
        if test[1]:
            print(f'::: expected {test[1]}')

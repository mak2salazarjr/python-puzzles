"""
http://www.geeksforgeeks.org/check-if-two-given-strings-are-isomorphic-to-each-other/

Two strings str1 and str2 are called isomorphic if there is a one to one mapping 
possible for every character of str1 to every character of str2. And all occurrences 
of every character in ‘str1’ map to same character in ‘str2’

"""
from collections import namedtuple


def are_isomorphic(str1, str2):
    """
    Determines if two strings are 'isomorphic'
    
    :param str1: a string
    :param str2: a string
    :return: True if isomorphic, False if they are not
    """
    if len(str1) != len(str2):
        return False

    char_map = {}
    mapped = set()
    for c1, c2 in zip(str1, str2):
        if c1 in char_map:
            if c2 != char_map[c1]:
                return False
        elif c2 in mapped:
            return False
        else:
            char_map[c1] = c2
            mapped.add(c2)
    return True


Test = namedtuple('Test', 's1 s2 expected')

tests = (
    Test('aab', 'xxy', True),
    Test('a', 'bb', False),
    Test('aab', 'xyz', False),
         )

if __name__ == '__main__':
    for test in tests:
        print(f'{test.s1}, {test.s2} -> {are_isomorphic(test.s1, test.s2)}')
        print(f'{test.s2}, {test.s1} -> {are_isomorphic(test.s2, test.s1)}')
        print(f'Expected {test.expected}')

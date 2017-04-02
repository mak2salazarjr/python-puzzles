from collections import namedtuple


class Solution(object):
    def addBinary(self, *bin_strs):
        """
        Add binary strings
        :param bin_strs: zero or more strings representing a binary number
        :return: a string representation of the sum 
        """
        return '{:b}'.format(sum([int(bin_str, base=2) for bin_str in bin_strs]))


if __name__ == '__main__':
    Test = namedtuple('Test', 'data expect')
    add_binary_strings = Solution().addBinary

    tests = (Test(tuple(), '0'),
             Test(('0',), '0'),
             Test(('1010', '11'), '1101'),
             Test(('1' * 100, '1'), '1' + '0' * 100),
             Test(('10' * 100, '11'), '10' * 98 + '1101'),
             Test(('1111', '111', '101'), '11011'))

    for test in tests:
        result = add_binary_strings(*test.data)
        print(f'{test.data} -> {result}')
        if test.expect:
            assert result == test.expect

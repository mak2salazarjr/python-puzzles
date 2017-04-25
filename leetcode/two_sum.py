# https://leetcode.com/problems/two-sum/#/description


class Solution(object):
    @staticmethod
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        value_map = {value: index for index, value in enumerate(nums)}
        for index_1, value in enumerate(nums):
            index_2 = value_map.get(target - value)
            if index_2:
                return [index_1, index_2]


assert Solution.two_sum([3, 2, 4], 6), [1, 2]
assert Solution.two_sum([0, 4, 3, 0], 0), [0, 3]
assert Solution.two_sum([i*2 for i in range(10000)] + [1], 64), [0, 32]

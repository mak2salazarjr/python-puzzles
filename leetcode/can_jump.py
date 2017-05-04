# https://leetcode.com/problems/jump-game/
# Given an array of non-negative integers, you are initially positioned
# at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        furthest_pos = 0
        for pos, max_jump in enumerate(nums):
            if pos > furthest_pos:
                return False
            furthest_pos = max(furthest_pos, pos + max_jump)
        return True


tests = (
    ([3, 2, 1, 0, 4], False),
    ([2, 3, 1, 1, 4], True),
    ([1, 1, 1, 1, 1, 0, 5], False),
    ([0, 1], False),
    ([2, 0, 1, 3, 0, 0, 1], True),
    ([5, 0, 5, 0, 0, 0], True),
    ([4, 0, 2, 0, 0, 0], False),
    ([4, 0, 2, 0, 1, 0], True),
)

can_jump = Solution().canJump

if __name__ == '__main__':
    for test in tests:
        print('{} -> {}\n  expected: {}'.format(test[0], can_jump(test[0]), test[1]))

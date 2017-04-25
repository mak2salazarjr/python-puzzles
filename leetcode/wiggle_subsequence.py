# https://leetcode.com/problems/wiggle-subsequence/#/description


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        wiggles = 0
        wiggled_up = None
        for num1, num2 in zip(nums[:-1], nums[1:]):
            if num1 < num2:
                if not wiggled_up:
                    wiggles += 1
                    wiggled_up = True
            elif num1 > num2:
                if wiggled_up or wiggled_up is None:
                    wiggles += 1
                    wiggled_up = False
            else:
                continue
        return 1 if wiggles == 0 else wiggles + 1


solution = Solution().wiggleMaxLength

for test in (
        [84],
        [1, 1],
        [1, 7, 4, 9, 2, 5],
        [1, 17, 5, 10, 13, 15, 10, 5, 16, 8],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [0, 1, 2, 3, 2, 1, 5, 3, 2, 1, 8],
        [1] * 10,
        [0],
        [1, 2, 2],
):
    print(f'{test} -> {solution(test)}')

# https://leetcode.com/problems/next-greater-element-ii/#/description
class Solution(object):
    def nextGreaterElements(self, nums):
        if not nums:
            return []
        output = [-1] * len(nums)
        tail = []
        for index in range(len(nums)):
            try:
                if nums[index] < nums[index + 1]:
                    output[index] = nums[index + 1]
                    while tail and nums[tail[-1]] < nums[index + 1]:
                        output[tail.pop()] = nums[index + 1]
                else:
                    tail.append(index)
            except IndexError:  # expected for last element in list
                tail.append(index)

        # remove maximal element(s) from tail
        tail = [item for item in tail if item != tail[0]]
        for num in nums:
            while tail and nums[tail[-1]] < num:
                output[tail.pop()] = num
            if not tail:
                break

        return output

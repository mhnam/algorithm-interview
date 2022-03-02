'''
LeetCode 561 [Array Partition I]
'''
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        # trial 1
        # for i in range(len(nums)//2):
        #     sum += nums[i*2]

        # trial 2: same logic but faster way
        # for i, n in enumerate(nums):
        #     if not i % 2:
        #         sum += n
        # return sum

        # trial 3: simplier way
        return sum(sorted(nums)[::2])


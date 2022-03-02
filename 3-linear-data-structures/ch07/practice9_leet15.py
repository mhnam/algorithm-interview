'''
LeetCode #15 [3Sum]

* Two-pointers Algorithm
'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = list()
        nums.sort()

        for i in range(len(nums) - 2): # subtract two for left and right pointers
            if i > 0 and nums[i - 1] == nums[i]: # to rule-out the case where the first and the second are identical
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # if [nums[i], nums[left], nums[right]] not in result: # no duplicates
                    result.append([nums[i], nums[left], nums[right]])

                    # following can save operations
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result
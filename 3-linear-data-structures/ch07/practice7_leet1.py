'''
LeetCode #1 [Two Sum]

* Dictionary is more faster in terms of access
* Brute-Force?
'''
from typing import List

# using try-except statement
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Construct map
        nums_mapped = {}
        for i, num in enumerate(nums):
            nums_mapped[num] = i # value becomes key

        for i in range(len(nums)):
            try:
                if i != nums_mapped[target - nums[i]]:
                    return [i, nums_mapped[target - nums[i]]]
            except:
                continue

# using conditional statement
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Construct map
        nums_mapped = {}
        for i, num in enumerate(nums):
            nums_mapped[num] = i # value becomes key

        for i, num in enumerate(nums):
            if target-num in nums_mapped.keys() & i != nums_mapped[target-num]:
                return [i, nums_mapped[target-num]]
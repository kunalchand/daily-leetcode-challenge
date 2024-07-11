"""
LC. 442

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

Example 1:

Input: nums = [4,4,2,7,8,2,3,1]
Output: [2,3]

"""

from typing import List

"""
[4,-4,2,-7,8,2,-3,1]
           i


"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for index in range(len(nums)):
            value = abs(nums[index])
            if nums[value - 1] < 0:
                ans.append(value)
            else:
                nums[value - 1] *= -1

        return ans

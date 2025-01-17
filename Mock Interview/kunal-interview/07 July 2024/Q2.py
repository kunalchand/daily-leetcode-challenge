"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

       Z
[2,5,8,1,0,0,0,0,0,3,12]
               N

"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = -1
        nonZero = -1

        # No Zero Exists
        for index in range(len(nums)):
            if nums[index] == 0:
                zero = index
                break
        if zero == -1:
            return

        # No NonZero Exists
        for index in range(zero + 1, len(nums)):
            if nums[index] != 0:
                nonZero = index
                break
        if nonZero == -1:
            return

        # Both Exists
        while zero < len(nums) and nonZero < len(nums):
            nums[zero], nums[nonZero] = nums[nonZero], nums[zero]

            while zero < len(nums):
                if nums[zero] == 0:
                    break
                zero += 1

            while nonZero < len(nums):
                if nums[nonZero] != 0:
                    break
                nonZero += 1

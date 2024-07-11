"""
LC. 643

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

 [1,12,-5,-6,50,3] k = 4 O(k) O(1)
        L       R
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_average = window_sum / k

        left = 0
        for right in range(k, len(nums)):
            window_sum -= nums[left]
            left += 1
            window_sum += nums[right]

            window_average = window_sum / k
            max_average = max(max_average, window_average)

        return max_average

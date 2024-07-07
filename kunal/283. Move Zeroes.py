import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from dataclasses import dataclass
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, inf, sqrt
from typing import Deque, Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/move-zeroes/
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
